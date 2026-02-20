#!/usr/bin/env python3
# Simple script to train the SMS spam detection model

print("Starting SMS spam detector model training...")

try:
    import pandas as pd
    import pickle
    import string
    import os
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.metrics import accuracy_score, classification_report

    print("Successfully imported ML libraries")
except ImportError as e:
    print(f"Error importing required libraries: {e}")
    print("Please install the required libraries:")
    print("pip install pandas scikit-learn")
    exit(1)

# Check if NLTK is available, if not use a simpler approach
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer

    # Download NLTK data
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)

    # Text preprocessing function with NLTK
    def preprocess_text(text):
        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = ''.join([char for char in text if char not in string.punctuation])

        # Tokenize
        tokens = nltk.word_tokenize(text)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]

        # Stemming
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(word) for word in tokens]

        # Join the tokens back into a single string
        return ' '.join(tokens)

    USING_NLTK = True
    print("Using NLTK for text preprocessing")

except ImportError:
    # Simpler preprocessing function without NLTK
    def preprocess_text(text):
        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = ''.join([char for char in text if char not in string.punctuation])

        # Split into words
        words = text.split()

        # Join the words back into a single string
        return ' '.join(words)

    USING_NLTK = False
    print("NLTK not available. Using simple text preprocessing")

try:
    # Check if the dataset file exists
    dataset_path = 'data/spam_ham_dataset.csv'
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset file '{dataset_path}' not found")
        exit(1)

    # Load the dataset
    print("Loading dataset...")
    df = pd.read_csv(dataset_path)
    
    # Keep only label and text columns, rename text to message
    df = df[['label', 'text']].rename(columns={'text': 'message'})
    
    # Convert label to lowercase if needed
    df['label'] = df['label'].str.lower()

    # Display basic info
    print(f"Dataset loaded: {df.shape[0]} messages")
    print(f"Spam messages: {df[df['label'] == 'spam'].shape[0]}")
    print(f"Ham messages: {df[df['label'] == 'ham'].shape[0]}")

    # Preprocess data
    print("Preprocessing messages...")
    df['cleaned_message'] = df['message'].apply(preprocess_text)

    # Convert labels to binary
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    # Create a CountVectorizer
    print("Extracting features...")
    cv = CountVectorizer()

    # Fit and transform the preprocessed messages
    X = cv.fit_transform(df['cleaned_message']).toarray()
    y = df['label'].values

    print(f"Feature extraction complete. Feature shape: {X.shape}")

    # Train the model
    print("Splitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training model...")
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Evaluate the model
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")

    print("Classification report:")
    print(classification_report(y_test, y_pred, target_names=['Ham', 'Spam']))

    # Save the model and vectorizer
    print("Saving model and vectorizer...")
    os.makedirs('models', exist_ok=True)
    pickle.dump(cv, open('models/cv-transform.pkl', 'wb'))
    pickle.dump(model, open('models/spam-sms-mnb-model.pkl', 'wb'))

    print("\nModel training completed successfully!")
    print("Files created:")
    print("  - models/cv-transform.pkl")
    print("  - models/spam-sms-mnb-model.pkl")
    print("\nYou can now run the Flask application to use the model.")

except Exception as e:
    print(f"An error occurred during model training: {e}")
    exit(1)
