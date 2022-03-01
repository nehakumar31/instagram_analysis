# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:38:08 2022

@author: nehkumar
"""

from NeuralNetworkPrediction import *
import streamlit as st


class StreamLitApp:
    """Interface for SentimentPrediction"""
    def __init__(self):        
        st.write("Instagram comments sentiment analysis...")
        self.sentiment_predictor = SentimentPredictor()  
    
    def construct_app(self):
        text = st.text_area('Enter the comment')         
        if st.button("Predict"):
            print("Predict sentiment of comment: {}".format(text))
            predicted_probs = self.sentiment_predictor.predict(text)
            print("Predicted probabilities: ", predicted_probs)
            predicted_sentiment = max(predicted_probs, key= lambda x: predicted_probs[x])
            st.success("Sentiment: {0}".format(predicted_sentiment))
            st.success("Predicted probabilities: {0}".format(predicted_probs))
        

if __name__ == '__main__':
    sa = StreamLitApp()
    sa.construct_app()
    
    