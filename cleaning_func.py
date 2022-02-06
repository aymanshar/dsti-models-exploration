# clean the text file
# import string 
import string
# import regular expression
import re
# import nltk
import nltk
from nltk.stem import PorterStemmer
nltk.download('stopwords')
nltk.download('wordnet')

#create cleaning function
def clean_text_punc(txt):
  '''this function to clean the text from punctuation, to use .apply(lambda x : clean_text_punc(x)'''
  clean_text="".join([c for c in txt if c not in string.punctuation])
  return clean_text
  
#create cltokenized function if needed
def tokenized_aslist(txt):
    '''this function to tokenize the sentences to list of words, to use .apply(lambda x : tokenized_aslist(x)'''
    tokens=re.split('\W+',txt)
    tokens=[word for word in tokens]
    return tokens

def tokenized(txt):
    '''this function to tokenize the sentences to list of words and join those words back to be a sentences, to use .apply(lambda x : tokenized(x)'''
    tokens=re.split('\W+',txt)
    tokens=" ".join([word for word in tokens])
    return tokens

# create function to remove the stop words
def remove_stopwords(text):
    '''this function to remove stop words and join those words back to be a sentences, to use .apply(lambda x : remove_stopwords(x)'''
    to_skip=['you','are']
    stopwords=set(nltk.corpus.stopwords.words('english')).difference(to_skip)
    tokens_stop=re.split('\W+',text)
    text_clean=" ".join([word for word in tokens_stop if word not in stopwords])
    return text_clean

# create stemming function
def stem_data(txt):
    '''this function to stem converting words to the root word and join words back to be a sentences, to use .apply(lambda x : stem_data(x)'''
    ps=PorterStemmer()
    tokens_stem=re.split('\W+',txt)
    text=" ".join([ps.stem(word) for word in tokens_stem])
    return text
    
# creating  function for lemmatizer
def lemma_data(txt):
    '''this function to lemmatize converting words to the root word using dic and join words back to be a sentences, to use .apply(lambda x : lemma_data(x)'''
    word_lemma =nltk.WordNetLemmatizer()
    tokens_lemmatize=re.split('\W+',txt)
    text=" ".join([word_lemma.lemmatize(word) for word in tokens_lemmatize])
    return text    

def predict(test):
    '''this function to pass prediction value it will print violent if value is 0 or good if 1'''
    if (test[0]==0):
        print('violent')
    elif (test[0]==1):
        print('good')
    else:
        print('unable to predict')