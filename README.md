# Instagram_analysis
Fetch and perform analysis on InstagramData centered around 4 types of beauty entities - <br><br>
**Brands:** These are entities that make and sell their own brand(s) of beauty products (i.e @maccosmetics) <br>
**Retailers:** These are entities that sell multiple beauty brands (i.e @sephora) <br>
**Publishers:** These are entities that publish content related to the beauty industry (i.e @allure) <br>
**Influencers:** These are individuals that promote beauty brands and products (i.e @cutcreaser) <br>

# Objective
To detect entities that are fast growing on internet with the help of use cases - <br><br>
**Sentiment Analysis:** Sentiment prediction of comments posted on media/posts of an Instagram profile <br>
**Network Analysis:** Determine spread of an entity with various network metrics like betweeness, centrality, closeness etc. Computation of these metrics consider relation between beauty entities and the suggested profiles for each. Instagram suggestion algorithm pays attention to all forms of engagement likes, comments, and time spent on a given profile. This approach reflects real interest/engagement of people with any entity than just looking at percent of followers increase as followers may or may not be real.

# Future Work 
Continue on network analysis using Instagram profile details like posts, comments on each post with weightage being assigned.
![image](https://user-images.githubusercontent.com/65956949/157179313-b41b5bc7-9f70-420b-b23f-786833df3ddd.png)


# Flow/Sequence
![image](https://user-images.githubusercontent.com/65956949/155954566-8f257d28-c29e-4c4a-a929-0f8e70cb1069.png)


# Tech & Framework
Nodejs for data scraping and writes profile data to its own json file<br>
Python modules like pyspellchecker, emoji, textblob, contractions, etc. for intermediary clean-up and data preparation<br>
Python scikit-learn machine learning, NLP modules like nltk, tensorflow, tensorflow_addons, keras_self_attention for sentiment analysis<br>
Python NetworkX for network analysis<br>
Python streamlit for display of results

# Installation
Packages needed for Environment readiness for each module is specified in env_requirements.tx file in respective directories

# Execution
Execute the modules in the order specified in the flow chart. The output of a module is an input to the next. Steps and instructions to run each module is specifed in the respective directory.

