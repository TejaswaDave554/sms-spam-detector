# SMS Spam Detection using NLP

This project implements an SMS spam detector using Natural Language Processing (NLP) techniques. It analyzes SMS messages to classify them as either spam or legitimate (ham) messages.

## Project Overview

The SMS spam detector uses machine learning algorithms to analyze the content of text messages and determine if they are spam or not. The system has been trained on a dataset of labeled SMS messages to learn the patterns and characteristics of spam messages.

## Features

- Text preprocessing using NLTK
- Feature extraction using CountVectorizer
- Classification using Multinomial Naive Bayes
- Web interface for real-time spam detection
- Detailed visualization of data analysis

## Tech Stack

- Anaconda Navigator
- Jupyter
- Numpy
- Pandas
- NLTK (Natural Language Toolkit)
- Porter Stemmer
- Matplotlib
- Scikit-Learn
- Flask for web deployment

## Project Structure

```
sms-spam-detector/
├── .github/
│   └── workflows/      # CI/CD pipelines
├── data/               # Datasets
│   ├── Spam SMS Collection
│   └── spam_ham_dataset.csv
├── docs/               # Documentation
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── DEPLOYMENT.md
│   └── SECURITY.md
├── models/             # Trained models (not in git)
│   ├── cv-transform.pkl
│   └── spam-sms-mnb-model.pkl
├── notebooks/          # Jupyter notebooks
│   └── Spam_Detection_Using_NLP.ipynb
├── static/             # Static files (CSS, JS)
├── templates/          # HTML templates
├── tests/              # Test files
├── app.py              # Flask application
├── train_model.py      # Model training script
├── wsgi.py             # WSGI entry point
├── config.py           # Configuration
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose
├── Procfile            # Heroku deployment
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Setup and Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd sms-spam-detector
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m nltk.downloader stopwords punkt
   ```

4. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env and set SECRET_KEY
   ```

5. Train the model:
   ```bash
   python train_model.py
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open your browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. Enter an SMS message in the text box on the home page.
2. Click "Check Message" to analyze the message.
3. The system will display whether the message is classified as spam or not.
4. You can also learn more about SMS spam by clicking on the "Learn about SMS Spam Detection" link.

## Model Training

The model is trained using the following steps:

1. Data cleaning and preprocessing
2. Feature extraction using CountVectorizer
3. Training a Multinomial Naive Bayes classifier
4. Evaluating the model's performance

Detailed steps can be found in the Jupyter notebook `notebooks/Spam_Detection_Using_NLP.ipynb`.

## Deployment

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed deployment instructions for:
- Heroku
- Docker
- AWS Elastic Beanstalk
- Railway
- Render

## Security

See [docs/SECURITY.md](docs/SECURITY.md) for security features and best practices.

## Testing

```bash
pip install -r requirements-dev.txt
pytest tests/ -v
```

## Documentation

- [Deployment Guide](docs/DEPLOYMENT.md)
- [Security Policy](docs/SECURITY.md)
- [Contributing Guidelines](docs/CONTRIBUTING.md)
- [Changelog](docs/CHANGELOG.md)

## License

[MIT License](LICENSE)

## Acknowledgements

- The SMS Spam Collection dataset used for training the model
- NLTK for natural language processing tools
- Scikit-learn for machine learning algorithms
- Flask for web application development
