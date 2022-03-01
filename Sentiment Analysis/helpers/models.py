# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 23:29:43 2022

@author: nehkumar
"""

#pre-processing
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
#from sklearn.model_selection import cross_val_score

#model
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import ComplementNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import Pipeline

#evaluation
from sklearn.metrics import f1_score, make_scorer

def compute_f1_score(true, pred):
  return f1_score(y_true=true, y_pred=pred, average='weighted')

custom_scorer = make_scorer(compute_f1_score)


#function to perform grid search CV
def gridsearch_cv(estimator, hyper_params, X_train, y_train):
    folds = RepeatedStratifiedKFold(n_splits=5, random_state = 100, n_repeats=3)
    grid_cv = GridSearchCV(estimator = estimator,
                      param_grid = hyper_params,
                      cv = folds,
                       verbose = True,
                       return_train_score = True,
                       scoring=custom_scorer,
                       n_jobs=-1
                      )

    grid_cv.fit(X_train, y_train)
    return grid_cv

def logistic_regression_grid(pipeline_elements, hyper_params, X, y):
    hyper_params['model__C'] = [0.0001, 0.001, 0.01, 0.1, 0.5, 1, 2, 5, 10,12,15,20]
    model = LogisticRegression(multi_class='multinomial', solver='lbfgs', class_weight='balanced', random_state=100)
    pipeline_elements.append(('model', model))
    estimator = Pipeline(pipeline_elements)
    grid_cv = gridsearch_cv(estimator, hyper_params, X, y)

    evaluate(grid_cv, X, y)
    return grid_cv

def logistic_regression_pipeline(pipeline_elements, model_params, X, y):
    model = LogisticRegression(multi_class='multinomial', solver='lbfgs', class_weight='balanced', C=model_params['C'], random_state=100)
    pipeline_elements.append(('model', model))
    estimator = Pipeline(pipeline_elements)
    estimator.fit(X, y)
    
    evaluate(estimator, X, y)
    return estimator

def logistic_regression(X, y, params):
    model = LogisticRegression(multi_class='multinomial', solver='lbfgs', class_weight='balanced', C=params['C'], random_state=100)
    model.fit(X, y)
    
    evaluate(model, X, y)
    return model

def multinomial_naivebayes_grid(pipeline_elements, hyper_params, X, y):
    hyper_params['model__alpha'] = [0, 0.001, 0.01, 0.1, 1]
    model = MultinomialNB()
    pipeline_elements.append(('model', model))
    estimator = Pipeline(pipeline_elements)
    grid_cv = gridsearch_cv(estimator, hyper_params, X, y)

    evaluate(grid_cv, X, y)
    return grid_cv

def multinomial_naivebayes_pipeline(pipeline_elements, model_params, X, y):
    model = MultinomialNB(alpha=model_params['alpha'])
    pipeline_elements.append(('model', model))
    estimator = Pipeline(pipeline_elements)
    estimator.fit(X, y)
    
    evaluate(estimator, X, y)
    return estimator


def complement_naivebayes_grid(pipeline_elements, hyper_params, X, y):
    hyper_params['model__alpha'] = [0, 0.001, 0.01, 0.1, 1]
    hyper_params['model__norm'] = [True, False]
    model = ComplementNB()
    pipeline_elements.append(('model', model))
    estimator = Pipeline(pipeline_elements)
    grid_cv = gridsearch_cv(estimator, hyper_params, X, y)

    evaluate(grid_cv, X, y)
    return grid_cv

def complement_naivebayes_pipeline(pipeline_elements, model_params, X, y):
    model = ComplementNB(alpha=model_params['alpha'], norm=model_params['norm'])
    pipeline_elements.append(('model', model))
    estimator = Pipeline(pipeline_elements)
    estimator.fit(X, y)
    
    evaluate(estimator, X, y)
    return estimator

def svm_grid(pipeline_elements, hyper_params, X, y):
    hyper_params['model__C'] = [0.0001, 0.001, 0.01, 0.1, 0.5, 1, 2, 5, 10]    
    hyper_params['model__gamma'] = ['scale','auto']
    model = SVC(class_weight='balanced', random_state=100)
    pipeline_elements.append(('model', model))
    estimator = Pipeline(pipeline_elements)
    grid_cv = gridsearch_cv(estimator, hyper_params, X, y)

    evaluate(grid_cv, X, y)
    return grid_cv
    
    
def svm(X, y, params):
    model = SVC(class_weight='balanced', random_state=100, C=params['C'], kernel=params['kernel'],
                degree=params['degree'], gamma=params['gamma'])
    model.fit(X, y)
    
    evaluate(model, X, y)
    return model    

def rf_classifier_fit(pipeline_elements, hyper_params, X, y):
    hyper_params['model__n_estimators'] = range(50,200,50)
    hyper_params['model__criterion'] = ['gini','entropy']
    hyper_params['model__max_depth'] = range(3,15,2)
    hyper_params['model__min_samples_split'] = range(500,1501,500)
    hyper_params['model__min_samples_leaf'] = range(100,201,50)    
    model = RandomForestClassifier(class_weight='balanced', random_state=100, max_features='sqrt', n_jobs=-1)
    
    pipeline_elements.append(('model', model))
    estimator = Pipeline(pipeline_elements)
    grid_cv = gridsearch_cv(estimator, hyper_params, X, y)

    evaluate(grid_cv, X, y)
    return grid_cv

def rf_classifier(X, y, params):
    model = RandomForestClassifier(class_weight='balanced', 
                                   n_estimators=params['n_estimators'], max_depth=params['max_depth'], min_samples_split=params['min_samples_split'],
                                   min_samples_leaf=params['min_samples_leaf'],
                                   random_state=100)
    model.fit(X, y)
    
    evaluate(model, X, y)
    return model
    
    
def evaluate(model, X, y, label="train"):
    y_pred = model.predict(X)
    print("{0} F1 Score: {1}".format(label, compute_f1_score(y, y_pred)))
    
    
    