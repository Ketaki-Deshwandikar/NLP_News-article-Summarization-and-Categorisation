# for text summarisation
from transformers import BartForConditionalGeneration, BartTokenizer
#BartTokenizer: This class is responsible for tokenizing input text into numerical sequences that can be understood by the BART model.
#  BartForConditionalGeneration: This class represents the BART model itself, tailored for conditional text generation tasks. 
#It's capable of taking tokenized input and generating text, making it useful for
# tasks like text summarization, translation, and text generation based on given prompts.
#BART : Bidirectional and Auto-Regressive Transformer
from newspaper import Config, Article, Source
import textwrap
import re

def text_summarizer(text):
    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)
                                                    #means that the encoded tokens will be returned as PyTorch tensors  like containers for numerical data
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=125, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    formatted_summary = "\n".join(textwrap.wrap(summary, width=80))
    
    # Replace multiple spaces with a single space
    formatted_summary = re.sub(r'\s+', ' ', formatted_summary)
    
    return formatted_summary

def text_summarizer_old(text):
    

    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)

    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=125, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    formatted_summary = "\n".join(textwrap.wrap(summary, width=80))
    return formatted_summary



