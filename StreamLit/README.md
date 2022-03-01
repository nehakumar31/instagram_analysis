# StreamLit
1. StreamLit app to predict comment sentiment. It uses BidirectionalLSTM trained model generated as an output of 
module: Sentiment Analysis/Model_NeuralNetwork_Pipeline.ipynb

# Tech/Framework
1. Coding Language - python
2. Python StreamLit

# Execution Details
1. Environment requirements are specified in env_requirements.txt file
2. Copy the below mentioned embeddings used in Neural Network training to dir: SentimentPrediction/embeddings/<br>
   emoji_embeddings_100d.txt<br>
   glove.twitter.27B.100d.txt
3. Copy the below mentioned output files of trained model: Sentiment Analysis/Model_NeuralNetwork_Pipeline.ipynb to dir: SentimentPrediction/model<br>
   BidirectionalLSTM.h5 <br>
   classes.pkl <br>
   tokenizer.pkl
4. To execute, in dir: SentimentPrediction/ , run command: streamlit run StreamLitApp.py
   


