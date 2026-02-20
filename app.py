from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import os
import logging
from functools import lru_cache
from threading import Lock
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(32))
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024  # 16KB max request size

# Security headers
csp = {
    'default-src': "'self'",
    'style-src': ["'self'", 'https://stackpath.bootstrapcdn.com'],
    'script-src': ["'self'", 'https://code.jquery.com', 'https://cdn.jsdelivr.net', 'https://stackpath.bootstrapcdn.com'],
    'font-src': ["'self'", 'https://stackpath.bootstrapcdn.com']
}
Talisman(app, content_security_policy=csp, force_https=os.environ.get('FLASK_ENV') == 'production')

# Rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# Thread-safe model loading
model_lock = Lock()
_model = None
_cv = None
_nltk_ready = False

def init_nltk():
    """Initialize NLTK data once"""
    global _nltk_ready
    if not _nltk_ready:
        try:
            nltk.data.find('corpora/stopwords')
            nltk.data.find('tokenizers/punkt')
            _nltk_ready = True
        except LookupError:
            logger.info("Downloading NLTK data...")
            nltk.download('stopwords', quiet=True)
            nltk.download('punkt', quiet=True)
            _nltk_ready = True

@lru_cache(maxsize=1000)
def preprocess_text(text):
    """Cached text preprocessing"""
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

def load_model():
    """Thread-safe model loading"""
    global _model, _cv
    
    with model_lock:
        if _model is None or _cv is None:
            try:
                model_path = os.environ.get('MODEL_PATH', 'models/spam-sms-mnb-model.pkl')
                cv_path = os.environ.get('CV_PATH', 'models/cv-transform.pkl')
                
                with open(model_path, 'rb') as f:
                    _model = pickle.load(f)
                with open(cv_path, 'rb') as f:
                    _cv = pickle.load(f)
                    
                logger.info("Model and vectorizer loaded successfully")
                return True
            except FileNotFoundError as e:
                logger.error(f"Model files not found: {e}")
                return False
            except Exception as e:
                logger.error(f"Error loading model: {e}")
                return False
    return True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@limiter.limit("10 per minute")
def predict():
    try:
        message = request.form.get('message', '').strip()
        
        if not message:
            return render_template('result.html', prediction='Error', message='Please enter a message'), 400
        
        if len(message) > 1000:
            return render_template('result.html', prediction='Error', message='Message too long (max 1000 characters)'), 400
        
        if not load_model():
            return render_template('model_missing.html'), 503
        
        processed_message = preprocess_text(message)
        vectorized_message = _cv.transform([processed_message]).toarray()
        prediction = _model.predict(vectorized_message)
        prediction_proba = _model.predict_proba(vectorized_message)
        
        confidence = prediction_proba[0][1] if prediction[0] == 1 else prediction_proba[0][0]
        confidence_percent = int(confidence * 100)
        confidence_str = f"{confidence:.2%}"
        
        result = 'Spam' if prediction[0] == 1 else 'Not Spam'
        return render_template('result.html', prediction=result, message=message, confidence=confidence_str, confidence_percent=confidence_percent)
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return render_template('result.html', prediction='Error', message='Invalid input'), 400
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return render_template('result.html', prediction='Error', message='An error occurred'), 500

@app.route('/about')
def about():
    return render_template('spam.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    status = {
        'status': 'healthy',
        'model_loaded': _model is not None and _cv is not None
    }
    return jsonify(status), 200 if status['model_loaded'] else 503

@app.errorhandler(429)
def ratelimit_handler(e):
    return render_template('result.html', prediction='Error', message='Rate limit exceeded. Please try again later.'), 429

@app.errorhandler(413)
def request_entity_too_large(e):
    return render_template('result.html', prediction='Error', message='Request too large'), 413

if __name__ == '__main__':
    init_nltk()
    load_model()
    
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
