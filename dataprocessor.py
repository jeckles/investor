import pandas as pd
import numpy as np
import math
import utilities
import nltk

def process():

    df = pd.read_csv('dataset.csv')

    df = df.drop(columns='Unnamed: 0')

    tokenized_text = []
    for text in df['text']:
        if type(text) is str:
            tokens = nltk.word_tokenize(text)
            cleaned_tokens = utilities.remove_noise(tokens)
            tokenized_text.append(cleaned_tokens)
        else:
            tokenized_text.append(None)

    dictionary = pd.read_csv('LoughranMcDonald_MasterDictionary_2018.csv')
    dictionary = dictionary[['Word', 'Negative', 'Positive']]
    lowercase = dictionary['Word'].str.lower()
    dictionary['Word'] = lowercase

    dictionary_words = list(dictionary['Word'])

    # now, get overall sentiment of each article
    sentiments = []
    for word_vec in tokenized_text:
        sentiment = 0
        if word_vec != None:
            for word in word_vec:
                try:
                    index = dictionary_words.index(word)
                    sentiment = sentiment + dictionary['Positive'][index] - dictionary['Negative'][index]
                except Exception:
                    pass
            if sentiment > 0:
                sentiments.append(1)
            elif sentiment < 0:
                sentiments.append(-1)
            else:
                sentiments.append(0)
        else:
            sentiments.append(0)

    df['sentiment'] = sentiments
    
    df.to_csv('processed_dataset.csv', index=False)

if __name__ == '__main__':
    process()