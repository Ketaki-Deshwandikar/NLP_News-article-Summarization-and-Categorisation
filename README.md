# NLP_News-article-Summarization-and-Categorisation
 This project is mainly implemented using 4 techniques of NLP that are as follows 
 1.Bag of Words using countVectorizer from sklearn library  
 2. Text Summarisation using BART Model 
 3. Text to Speech conversion using gTTS API 
 4.parse() and nlp() methods. 
 The news articles for processing are fetched using the technique of "WEB-SCRAPING"." 
 Libraries:

1.os.path: This library provides functions to interact with the filesystem paths. It is used for checking file existence and truncating files.
2.csv: The csv library is used for reading and writing CSV files, commonly used for storing tabular data. It is utilized for saving the scraped news articles into CSV format.
3.requests: This library enables sending HTTP requests to web servers and handling their responses. It is used for making HTTP requests to fetch web pages in the web scraping process.
4.pandas: Pandas is a powerful library for data manipulation and analysis. It is used for reading and processing CSV files containing scraped news articles.
5.nltk.corpus: This part of the Natural Language Toolkit (NLTK) provides access to a variety of natural language corpora and lexical resources. It is used for accessing the stopwords corpus for text preprocessing.
6.gtts: The Google Text-to-Speech (gTTS) library is used for converting text to speech. It is employed to generate audio summaries of news articles.
7.streamlit: Streamlit is a Python library used for creating interactive web applications for data science and machine learning projects. It is utilized to build the user interface for displaying summarized news articles and converting them to audio.
8.bs4 (BeautifulSoup): This module is part of the BeautifulSoup library, used for web scraping HTML and XML documents. It is used to parse HTML content and extract relevant information from web pages.
newspaper: This module provides functionalities for web scraping news articles from various online sources. It is used to download and parse news articles from specified URLs.

Functions:

1.text_summarizer: This function generates summarized versions of text using pre-trained models. It is used to create concise summaries of news articles.
2.categorize_articles: This function categorizes news articles based on their content or domain. It organizes scraped articles into different categories like India, World, Business, Technology, and Sports.
3.preprocess_text: This function preprocesses raw text data by tokenizing, removing punctuation, and filtering out stopwords. It is used as part of the text processing pipeline before summarization or categorization.
4.similarity_score: This function calculates the similarity score between a given text and a bag of words (BoW). It is used to classify text domains by comparing them with predefined BoW models.
5.classify_text_domain: This function determines the domain of a text (e.g., India, World, Business) based on its content. It is used to classify news articles into different categories.
6.start: This function serves as the entry point of the project. It orchestrates the execution of various tasks such as scraping news articles, summarizing them, categorizing them, and saving them to CSV files. Additionally, it handles the initialization of the Streamlit app.
7.Text to audio conversion of summarized articles is done for better user experience and convenience.


