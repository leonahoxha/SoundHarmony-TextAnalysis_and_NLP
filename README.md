SoundHarmony: Headphone Review Analysis
Project Overview
Choosing the right pair of headphones can be overwhelming with so many options available. In SoundHarmony, I analyzed 11 popular headphones by comparing user reviews on Reddit with article ratings. The goal was to determine which rating source—Reddit reviews or article ratings—aligns better with the technical specifications of the headphones and helps potential customers make more informed decisions.

Additionally, I conducted sentiment analysis using three models and performed LDA topic modeling to identify the most discussed topics in user reviews.

Key Objectives
Compare Reddit user reviews with article ratings for each headphone.
Assess correlations between review sources and technical specs.
Perform sentiment analysis using three models: RoBERTa, TextBlob, and VADER.
Conduct topic modeling (LDA) to uncover the most discussed themes in Reddit reviews.
Data Sources
Reddit Comments: Scraped from subreddits discussing the 11 headphone models.
Article Ratings: Sourced from reputable review websites.
Technical Specifications: Collected from official headphone brand websites.
Methods
Sentiment Analysis: Applied three models, with RoBERTa outperforming others in detecting sentiment from Reddit comments.
Weighted Rating (Weighted_Rate): Created a normalized rating for each headphone based on both the number of comments and sentiment.
Topic Modeling (LDA): Analyzed recurring themes in Reddit discussions, such as sound quality, comfort, and battery life.
Correlation Analysis: Assessed the relationship between user reviews and technical specs to measure alignment.
Tools & Technologies
Python for scripting and data analysis.
Pandas, NumPy for data manipulation.
Scikit-learn for machine learning models.
NLTK, spaCy for natural language processing.
RoBERTa, TextBlob, VADER for sentiment analysis.
Gensim for LDA topic modeling.
Matplotlib, Seaborn for data visualization.
Key Findings
RoBERTa provided the most accurate sentiment analysis for Reddit comments.
There was a weak correlation between Reddit reviews and technical specs, suggesting that user reviews are often influenced by subjective factors.
Article ratings had a stronger correlation with technical specifications, reflecting a more structured evaluation based on metrics.
LDA modeling revealed that user discussions focus on comfort, sound quality, and price.
Conclusion
The project emphasizes the need to consider both technical specifications and real user feedback when choosing headphones. While articles provide structured insights, Reddit reviews offer authentic user experiences that better reflect everyday use.

Future Enhancements
Include more headphone models and expand to other platforms like Amazon or Best Buy.
Improve sentiment analysis by training a custom model on a larger dataset of headphone reviews.
Implement real-time data scraping to keep up with new reviews and trends.
