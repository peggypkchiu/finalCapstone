# import pandas, spacy and textblog
import pandas as pd
import spacy
from textblob import TextBlob
# load the spacy model "en_core_web_md"
nlp = spacy.load("en_core_web_md")
# read data file, clean up data by removing "na" in column "reviews.text"
dataframe = pd.read_csv("amazon_product_reviews.csv")
clean_data = dataframe.dropna(subset=["reviews.text"])
reviews_data = dataframe["reviews.text"]

# create a function for predicting sentiment
def analyze_polarity(text):
    # Preprocess the text with spacy
# analyze sentiment with TextBlob
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    return polarity

# count number of review with positive/negative/neutral comment, and calculate average of polarity score for all reviews
positive = 0
negative = 0
neutral = 0
total_polarity_score = 0
for ind_review in reviews_data:
    ind_polarity_score = analyze_polarity(ind_review)
    if ind_polarity_score > 0:
        positive += 1
    elif ind_polarity_score < 0:
        negative += 1
    else: neutral += 1
    total_polarity_score += ind_polarity_score
total = positive + negative + neutral
avg_polarity_score = total_polarity_score/ total
percentage_positive = (positive / total * 100)
percentage_negative = (negative / total * 100)
percentage_neutral = (neutral / total * 100)

# print outcome of sentiment analysis, and round up the average polarity score
print(f"""From Amazon Product Reviews,
Total number of reviews: {total}, in which 
Number of review with positive comment: {positive}, which is {percentage_positive:.2f} of total reviews;
Number of review with negative comment: {negative}, which is {percentage_negative:.2f} of total reviews;
Number of review with neutral comment: {neutral}), which is {percentage_neutral:.2f} of total reviews.
Total polarity of sentiment: {total_polarity_score:.2f}.
On average, polarity of sentiment for all reviews (between -1 "most negative" to +1 "most positive score"): {avg_polarity_score:.2f}""")
