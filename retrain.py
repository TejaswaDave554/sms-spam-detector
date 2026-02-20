#!/usr/bin/env python3
import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from database import get_feedback_data
from train_model import preprocess_text

def retrain_model():
    """Retrain model with original data + user feedback"""
    
    # Load original dataset
    print("Loading original dataset...")
    df_original = pd.read_csv('data/spam_ham_dataset.csv')
    df_original = df_original[['label', 'text']].rename(columns={'text': 'message'})
    df_original['label'] = df_original['label'].str.lower()
    df_original['label'] = df_original['label'].map({'ham': 0, 'spam': 1})
    
    # Get user feedback
    print("Loading user feedback...")
    feedback_data = get_feedback_data()
    
    if len(feedback_data) < 10:
        print(f"Not enough feedback data ({len(feedback_data)} samples). Need at least 10.")
        return
    
    df_feedback = pd.DataFrame(feedback_data, columns=['message', 'label'])
    
    # Combine datasets
    df_combined = pd.concat([df_original, df_feedback], ignore_index=True)
    print(f"Total samples: {len(df_combined)} (Original: {len(df_original)}, Feedback: {len(df_feedback)})")
    
    # Preprocess
    print("Preprocessing messages...")
    df_combined['cleaned_message'] = df_combined['message'].apply(preprocess_text)
    
    # Train
    print("Training model...")
    cv = CountVectorizer()
    X = cv.fit_transform(df_combined['cleaned_message']).toarray()
    y = df_combined['label'].values
    
    model = MultinomialNB()
    model.fit(X, y)
    
    # Save
    print("Saving updated model...")
    os.makedirs('models', exist_ok=True)
    pickle.dump(cv, open('models/cv-transform.pkl', 'wb'))
    pickle.dump(model, open('models/spam-sms-mnb-model.pkl', 'wb'))
    
    print("Model retrained successfully!")

if __name__ == '__main__':
    retrain_model()
