import os.path
import pandas as pd
from bs4 import BeautifulSoup # pulling data out of HTML and XML files.
from newspaper import Article
import requests
from categorize_text import classify_text_domain

def categorize_articles(all_links):
    visited_links = {}  # Dictionary to track visited links and their domains

    for url in all_links:
        response = requests.get(url)
        web_page = response.text
        soup = BeautifulSoup(web_page, 'html.parser')
        for article_tag in soup.find_all('a', href=True):
            link = article_tag['href']
            # Check if the link starts with "https://timesofindia.indiatimes.com/" and contains "articleshow"
            if (link.startswith("https://timesofindia.indiatimes.com/") and "articleshow" in link and "etimes" not in link and "auto" not in link and "tv" not in link and "tv/hindi" not in link and "web-series" not in link and "life-style" not in link and "/education" not in link and "entertainment" not in link):

                # Check if the link has been visited before
                if link not in visited_links:
                    try:
                        article = Article(link)
                        article.download()
                        article.parse()
                        article.nlp()
                        text = article.text
                        domain = classify_text_domain(text)
                        
                        # Store the link and its domain in the visited links dictionary
                        visited_links[link] = domain
                        print(link, " is ", domain) 
                    except Exception as e:
                        print(f"Error downloading article from {link}: {e}")
                        continue  # Continue with the next iteration of the loop

    # Separate links based on their domains
    domain_lists = {
        'India': [],
        'World': [],
        'Business': [],
        'Technology': [],
        'Sports': []
    }

    for link, domain in visited_links.items():
        domain_lists[domain].append(link)

    
    return domain_lists





