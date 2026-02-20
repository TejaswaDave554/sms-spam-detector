from app import app, init_nltk, load_model

# Initialize on startup
init_nltk()
load_model()

if __name__ == "__main__":
    app.run()
