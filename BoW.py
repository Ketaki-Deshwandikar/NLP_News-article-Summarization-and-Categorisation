from bs4 import BeautifulSoup # for webscraping and parsing HTML and XML files
from textblob import TextBlob # for processing textual data and its analysis like pos tagging
from newspaper import Config, Article, Source
import requests
import nltk #text processing tasks like tokenization, part-of-speech tagging, named entity recognition, text classification, sentiment analysis
from nltk import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from sklearn.feature_extraction.text import CountVectorizer #matrix of token counts
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem import WordNetLemmatizer
import pandas as pd #is used for data manipulation and analysis tasks, such as loading, cleaning, transforming, 
                    #and analyzing text data stored in tabular formats (like CSV files or databases)


nltk.download('stopwords')
nltk.download('punkt')# used for sentence tokenization

def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return ' '.join(tokens)

def generate_BoW(text_list):
    # Preprocess the text data
    preprocessed_texts = [preprocess_text(text) for text in text_list]

    # Initialize CountVectorizer object with custom preprocessing and additional stop words
    vectorizer = CountVectorizer(preprocessor=preprocess_text, stop_words='english')

    # Fit the vectorizer to the preprocessed text data and transform it into a bag of words representation
    bag_of_words = vectorizer.fit_transform(preprocessed_texts)

    # Get the feature names (words) from the vectorizer
    feature_names = vectorizer.get_feature_names_out()

    # Create a dictionary to store the word frequencies
    bow = {}
    for i, word in enumerate(feature_names):
        bow[word] = bag_of_words[:, i].sum()

    return bow

def collect_text_from_url(url):
    response = requests.get(url)
    india_web_page = response.text
    soup = BeautifulSoup(india_web_page, 'html.parser')
    article_links = []
    article_text = []
    article_summary = []

    for article_tag in soup.find_all('a', href=True):
        link = article_tag['href']
        # Check if the link starts with "https://timesofindia.indiatimes.com/" and contains "articleshow"
        if (link.startswith("https://timesofindia.indiatimes.com/") and "articleshow" in link and "etimes" not in link and "auto" not in link and "tv" not in link and "tv/hindi" not in link and "web-series" not in link and "life-style" not in link and "/education" not in link):

            article = Article(link)
            article.download()
            article.parse()
            article.nlp()
            text = article.text
            article_text.append(text)

    return article_text

def save_BoW_to_csv(bow, filename):
    df = pd.DataFrame(list(bow.items()), columns=['Word', 'Frequency'])
    df.to_csv(filename, index=False)
    print("Done - ", filename)

# Collect text from URLs
india_text = collect_text_from_url("https://timesofindia.indiatimes.com/india")
world_text = collect_text_from_url("https://timesofindia.indiatimes.com/world")
business_text = collect_text_from_url("https://timesofindia.indiatimes.com/business")
tech_text = collect_text_from_url("https://timesofindia.indiatimes.com/technology")
sports_text = collect_text_from_url("https://timesofindia.indiatimes.com/sports")

# Generate bags of words
india_bow = generate_BoW(india_text)
world_bow = generate_BoW(world_text)
business_bow = generate_BoW(business_text)
tech_bow = generate_BoW(tech_text)
sports_bow = generate_BoW(sports_text)

# Save bags of words to CSV files
save_BoW_to_csv(india_bow, "india_bow.csv")
save_BoW_to_csv(world_bow, "world_bow.csv")
save_BoW_to_csv(business_bow, "business_bow.csv")
save_BoW_to_csv(tech_bow, "tech_bow.csv")
save_BoW_to_csv(sports_bow, "sports_bow.csv")
