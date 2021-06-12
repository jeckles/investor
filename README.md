# investor

investor is short project exploring sentiment analysis of stock related news articles. This project consists of the following files:

* utilities.py
* databuilder.py
* dataprocessor.py
* bert.py

## utilities.py

The utilities.py file contains a function for cleaning and tokenizing a text block. It returns an array of tokenized text, void of certain stopwords, punctionation, and extraneous symbols.

## databuilder.py
 
The databuilder.py file downloads certain company's stock news articles from the past year, adds them to a pandas dataframe, and writes them to a csv file.

## dataprocessor

The dataprocessor.py file does some preprocessing on the data produced by running the databuilder.py file and determines a sentiment score for each article. It does this by using the [Loughran McDonald Master Dictionary](https://sraf.nd.edu/textual-analysis/resources/#Master%20Dictionary). It counts the number of positive words and negative words, subtracts the difference and marks the sentiment as either positive (1) or negative (0) accordingly. 

## bert.py

The bert.py file uses the pre-trained BERT Tokenizer and Sequence Classifier from the [transformers library](https://huggingface.co/transformers/) to eventually predict the overall sentiment of stock related news articles.
