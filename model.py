from imports import *
from prepare import prep_data, basic_clean, lemmatize, remove_stopwords, split, clean, clean_skills

def model_data(train, validate, test):
    '''
    This function transform text columns into individual features and put them into a dataframe
    Then concatenate with the feautures from original train dataset
    It will perform the same process for train, validate and test then return the transformed datasets
    '''
    tfidf = TfidfVectorizer(max_features = 6, ngram_range=(2, 2))
    r_words_train = tfidf.fit_transform(train.requirements)
    r = pd.DataFrame(r_words_train.todense(), columns=tfidf.get_feature_names_out())
    cols = ['analyst', 'engineer','scientist']
    newdf = pd.DataFrame(train[cols])
    r = r.set_index(newdf.index)
    X_train_b=pd.concat([r,newdf], axis =1)

    r_words_validate = tfidf.transform(validate.requirements)
    r = pd.DataFrame(r_words_validate.todense(), columns=tfidf.get_feature_names_out())
    cols = ['analyst', 'engineer','scientist']
    newdf = pd.DataFrame(validate[cols])
    r = r.set_index(newdf.index)
    X_validate_b=pd.concat([r,newdf], axis =1)

    r_words_test = tfidf.transform(test.requirements)
    r = pd.DataFrame(r_words_test.todense(), columns=tfidf.get_feature_names_out())
    cols = ['analyst', 'engineer','scientist']
    newdf = pd.DataFrame(test[cols])
    r = r.set_index(newdf.index)
    X_test_b=pd.concat([r,newdf], axis =1)
    y_train = train.label
    y_validate = validate.label
    y_test = test.label

    return X_train_b, y_train, X_validate_b, y_validate, X_test_b, y_test

def baseline(train):
    '''
    This function generates a baseline prediction of the training dataset
    '''
    train['baseline_pred'] = 'g'
    baseline_accuracy = (train.label == train.baseline_pred).mean()
    print(f'Baseline prediction accuracy from train dataset is: {baseline_accuracy:.2%}')

def decision_tree(X_train_b, y_train):
    '''
    This function generates a decision tree classifier and fit the model on train dataset
    It then print out the accuracy of the decision tree model
    '''
    # Create the tree
    tree2 = DecisionTreeClassifier(max_depth=3, random_state=123)

    # Fit the model on train
    tree2 = tree2.fit(X_train_b, y_train)

    # Print the accuracy
    print('Accuracy of Decision Tree classifier on training set: {:.3f}'
      .format(tree2.score(X_train_b, y_train)))

def random_forest(X_train_b, y_train):
    '''
    This function generates a random forest classifier and fit the model on train dataset
    It then print out the accuracy of the random forest model
    '''
    # Make the model
    forest3 = RandomForestClassifier(max_depth=3, random_state=123)

    # Fit the model on train
    forest3.fit(X_train_b, y_train)

    # Print the accuracy
    print('Accuracy of Random Foreset classifier on training set: {:.3f}'
      .format(forest3.score(X_train_b, y_train)))

def logistic_regression(X_train_b,y_train):
    '''
    This function generates a logtistic regression classifier and fit the model on train dataset
    It then print out the accuracy of the logistic regression model
    '''
    # Make the model
    logit2 = LogisticRegression(random_state = 123, C = 0.01)

    # Fit the model on train
    logit2.fit(X_train_b, y_train)

    # Print accuracy
    print('Accuracy of Logistic Regression classifier on training set: {:.3f}'
        .format(logit2.score(X_train_b, y_train)))

def xg(x_train, y_train):
    '''
    This function generates a xgboost classifier and fit the model on train dataset
    It then print out the accuracy of the model
    '''
    # Fit model to training data
    model = XGBClassifier()
    
    model.fit(x_train, y_train)

    y_pred = model.predict(x_train)

    print('Accuracy of XGBoost classifier on training set: {:.3f}'
        .format(model.score(x_train, y_train)))

def evaluation(X_train_b, y_train, X_validate_b, y_validate):
    '''
    This function takes in the x and y train and validate,
    generates a decision tree and random forest classifiers,
    then fit decision tree model and random forest model on train dataset
    and print out the accuracy of the models on validatea dataset
    '''
    tree2 = DecisionTreeClassifier(max_depth=3, random_state=123)
    # Fit the model on train
    tree2 = tree2.fit(X_train_b, y_train)
    # Use the model
    # We'll evaluate the model's performance on train, first
    y_predictions = tree2.predict(X_train_b)
    print('Accuracy of Decision Tree classifier on validate set: {:.3f}'
      .format(tree2.score(X_validate_b, y_validate)))
    
     # Make the model
    forest3 = RandomForestClassifier(max_depth=3, random_state=123)

    # Fit the model on train
    forest3.fit(X_train_b, y_train)

    # Print out accuracy
    print('Accuracy of Random Foreset classifier on validate set: {:.3f}'
      .format(forest3.score(X_validate_b, y_validate)))
    
def xg_evaluate(X_train_b, y_train, X_validate_b, y_validate):
    '''
    This function create a xgboost classifier and fit eh model on train
    It then prints out the accuracy on validate dataset
    '''
    # Fit model to training data
    model = XGBClassifier()
    model.fit(X_train_b, y_train)
    print('Accuracy of XGBoost classifier on validate set: {:.3f}'
        .format(model.score(X_validate_b, y_validate)))

def test_evaluate(X_train_b, y_train, X_test_b, y_test):
    '''
    This function is the final model evalution
    It generates the classifier on training set and print out the accuracy on test
    '''
    tree2 = DecisionTreeClassifier(max_depth=3, random_state=123)

    # Fit the model on train
    tree2 = tree2.fit(X_train_b, y_train)
    print('Accuracy of Decision Tree classifier ont test set: {:.3f}'
      .format(tree2.score(X_test_b, y_test)))
