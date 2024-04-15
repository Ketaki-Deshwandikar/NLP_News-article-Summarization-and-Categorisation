import os
import nltk
nltk.download('stopwords')
from main3 import start
files = [
    "C:/Users/Ketaki/Desktop/NLP PROJECT/nlp/NLP_Project-main/project/india.csv",
    "C:/Users/Ketaki/Desktop/NLP PROJECT/nlp/NLP_Project-main/project/world.csv",
    "C:/Users/Ketaki/Desktop/NLP PROJECT/nlp/NLP_Project-main/project/tech.csv",
    "C:/Users/Ketaki/Desktop/NLP PROJECT/nlp/NLP_Project-main/project/business.csv",
    "C:/Users/Ketaki/Desktop/NLP PROJECT/nlp/NLP_Project-main/project/sports.csv"
]

for filepath in files:
    # Check if the file exists
    if os.path.exists(filepath):
        # Open the file in binary write mode
        with open(filepath, "wb") as f: #f : file object
            # Truncate the file
            f.truncate()
        print(f"File '{filepath}' truncated successfully.")
    else:
        print(f"File '{filepath}' does not exist.")

start()