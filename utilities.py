import sys
from GoogleNews import GoogleNews
import datetime
from newspaper import Article
from newspaper import Config
import nltk
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import re, string

EN_STOPS = set(stopwords.words('english'))

def remove_noise(tokens):
    cleaned_tokens = []
    for token, tag in pos_tag(tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                    '(?:%[0-9a-fA-F][0-9a-fA-F]))+©','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        punctuation = string.punctuation + '–' + '”' + '“' + '’' + '\'ll' + 'i.e'

        if len(token) > 0 and token not in punctuation and token not in EN_STOPS:
            if not any(map(str.isdigit, token)):
                cleaned_tokens.append(token.lower())
    return cleaned_tokens






