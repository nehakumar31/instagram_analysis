# Sentiment Analysis
1. Trains a model with input as labelled Comments.
2. Target class has 4 categories: <br>
   Positive => Comment like "howw stunning 🌺🌺🌺🌺🌺🌺🌺🌺"<br>
               All requests are considered as positive. Comment like "please bring back pearberry" as they indicate user's interest in that brand<br>
               All inquiries are considered as positive. Comment like "with the aroma therapy prods be on sale too?" as they are indication os user's interest<br>
   Negative => Comment like "pathetic delivery and broken products"<br>
   Neutral => Comment like "😮😮😮😮😮" as this is not an indicative of surprise positive/negative<br>
              Comment like "magic charmer 💫"<br>
   Mixed => Comments having both good and bad/sarcasm like "this dress is beautiful. the new reboot is terrible." <br>
   
   End user would have to focus on labels - Negative and Mixed to work on improvement strategies. 
3. Metric used for evaluation is weighted f1-score to get balance of precision and recall considering imbalance too.
   

# Tech/Framework
1. Coding Language - python
2. For cleanup and data preparation, python modules: pyspellchecker, emoji, Pycld2, contractions, textblob, openpyxl, matplotlib
3. Python scikit machine learning algorithms, NLP nltk, tensorflow, tensorflow_addons, keras_self_attention

# Execution Details
1. Module has execution results of different trained models.
2. gridSearch was performed to tune hyper-parameters
3. Categories of Models:
    a) Preprocessing BOW - CountVectorizer/TFIds vectorizer<br>
       Algorithm => LogisticRegression, Multinomial NB, Complement NB<br>
    b) Preprocessing pretrained glove twitter embeddings and emoji embeddings<br>
       Algorithm => Logistic Regression, SVM, RandomForestClassifier<br>
    c) Preprocessing pretrained glove twitter embeddings and emoji embeddings<br>
       Algorithm => Dense Neural Network, Bidirectional LSTM, Bidirectional LSTM with custom attention layer, Bidirectional LSTM with keras attention layer.
 
