from imports import *

def prep_data(df):
    '''
    This function takes in a dataframe and return the dataframe with meaningless column dropped,
    and dummy variables for categorical feature concatenated.
    '''
    # Combine job requirements and skills
    df['requirements'] = df['requirements'] + df['skills']
    
    # Dummy variables for job level
    level_dummy = pd.get_dummies(df[['level']], dummy_na=False, drop_first=False)
    df = pd.concat([df, level_dummy], axis=1)
    
    # Dummy variables for role
    role_dummy = pd.get_dummies(df[['role']], dummy_na=False, drop_first=False)
    df = pd.concat([df, role_dummy], axis=1)
    df.rename(columns = {'level_Associate':'associate', 'level_Entry':'entry',
                              'level_Mid-Senior':'mid_senior', 'role_Data Analyst':'analyst',
                     'role_Data Engineer':'engineer', 'role_Data Science Manager': 'maganer',
                    'role_Data Scientist':'scientist'}, inplace = True)
    
    # Turning non-bachelor education levels to one category vs. bachelor
    df['edu_higher'] = df['edu_master']+df['edu_phd']
    df['edu_b_dmnt']=((df['edu_bachelor']+df['edu_other']) >= df['edu_higher'])
    df['label'] = df.edu_b_dmnt.map({False: 'h', True: 'b'})
    
    # Drop columns
    cols = ['link', 'edu_bachelor', 'edu_master', 'edu_phd', 'edu_other', 'edu_higher']
    df.drop(columns = cols, inplace = True)
    
    return df

def basic_clean(string):
    '''
    This function takes in a string and
    returns the string normalized.
    '''
    string = string.lower()
    string = unicodedata.normalize('NFKD', string)\
             .encode('ascii', 'ignore')\
             .decode('utf-8', 'ignore')
    # Removing white space
    string = re.sub(r'\s+', ' ',   string)
    # Removing anything that is not a-z, 0-9, a single quote, or whitespace
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    return string

def tokenize(string):
    '''
    This function takes in a string and
    returns a tokenized string.
    '''
    # Create tokenizer.
    tokenizer = nltk.tokenize.ToktokTokenizer()

    # Use tokenizer
    string = tokenizer.tokenize(string, return_str = True)

    return string

def stem(string):
    '''
    This function takes in a string and
    returns a string with words stemmed.
    '''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    
    # Use the stemmer to stem each word in the list of words we created by using split.
    stems = [ps.stem(word) for word in string.split()]
    
    # Join our lists of words into a string again and assign to a variable.
    string = ' '.join(stems)
    
    return string

def lemmatize(string):
    '''
    This function takes in string for and
    returns a string with words lemmatized.
    '''
    # Create the lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()

    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in string.split()]

    # Join our list of words into a string again and assign to a variable.
    string = ' '.join(lemmas)
    
    return string

def remove_stopwords(string, extra_words = [], exclude_words = []):
    '''
    This function takes in a string, optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))

    # Split words in string.
    words = string.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords

def prep_text(df, column, extra_words=[], exclude_words=[]):
    '''
    This function take in a df and the string name for a text column with 
    option to pass lists for extra_words and exclude_words and
    returns a df with the original text, stemmed text,
    lemmatized text, cleaned, tokenized, & lemmatized text with stopwords removed.
    '''
    df[column] = df[column].str.lower()
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df['stemmed'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(stem)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df['lemmatized'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(lemmatize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    return df[['clean', 'stemmed', 'lemmatized']]

def split(df):
    '''
    This function splits a dataframe into 
    train, validate, and test in order to explore the data and to create and validate models. 
    It takes in a dataframe and contains an integer for setting a seed for replication. 
    Test is 20% of the original dataset. The remaining 80% of the dataset is 
    divided between valiidate and train, with validate being .30*.80= 24% of 
    the original dataset, and train being .70*.80= 56% of the original dataset. 
    The function returns, train, validate and test dataframes. 
    '''
    train, test = train_test_split(df, test_size = .2, random_state=123)   
    train, validate = train_test_split(train, test_size=.3, random_state=123)
    
    return train, validate, test