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
Spam-SMS-Classifier
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
│   ├── index.html      # Home page
│   ├── result.html     # Result page
│   └── spam.html       # Information about spam
├── app.py              # Flask application
├── cv-transform.pkl    # Saved CountVectorizer
├── Procfile            # For Heroku deployment
├── README.md           # This file
├── requirements.txt    # Python dependencies
├── Spam SMS Collection # Dataset file
├── spam-sms-mnb-model.pkl # Saved model
└── Spam_Detection_Using_NLP.ipynb # Jupyter notebook
```

## Setup and Installation(after unzipping the folder)

1. Clone this repository:
   ```
   git clone <repository-url>
   cd sms-spam-detector
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Jupyter notebook to train the model:
   ```
   jupyter notebook Spam_Detection_Using_NLP.ipynb
   ```

5. Run the Flask application:
   ```
   python app.py
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000/` to use the application.

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

Detailed steps can be found in the Jupyter notebook `Spam_Detection_Using_NLP.ipynb`.

## Deployment

The application can be deployed to Heroku using the provided Procfile. Make sure you have the Heroku CLI installed and run:

```
heroku login
heroku create your-app-name
git push heroku main
```

## License

[MIT License](LICENSE)

## Acknowledgements

- The SMS Spam Collection dataset used for training the model
- NLTK for natural language processing tools
- Scikit-learn for machine learning algorithms
- Flask for web application development
