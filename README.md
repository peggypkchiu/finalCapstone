finalCapstone: sentiment_analysis

Description of the project: The dataset is related to Amazon product reviews.  In the project, we predict the sentiments from customer reviews by calculating the polarity score of each individual review, and the percentage of reviews with different views.  Also, we conclude the result with total and average overall sentiment score on Amazon products.

Details of the preprocessing steps: The dataset has been limited to the “review” column to enhance efficiency for running data, and also cleaned up by dropping “na” review to enhance accuracy by considering existing comments only.

Evaluation of results: In the project, we totally collected 34,660 customer’s reviews.  Overall, 89.91% of customers have positive comments, 4.32% of customers have negative comments, and 5.77 % of customers have neutral comments on Amazon products.  We measured sentiment of each review by using a polarity score, which ranged from -1 (most negative), to +1 (most positive).  After detailed analysis from all customer’s’ reviews, the total polarity score of sentiment is 13083.14.  On average, the polarity score of sentiment is 0.38, which reflects positive overall comments from customers on Amazon products.

Insights into the models strength and limitations: The model’s strengths are considering all customers’ comments, calculating the percentage of reviews with different views from customers, and evaluating the results by average and total scores to reflect overall results.  The limitations are calculating all polarity scores and total average, and did not exclude comments/ polarity scores with inconsistent data gathered from the same customer e.g. content in "review" v.s. provided "reviews.rating", which may distort overall results.

Install the project: enter the following command "git clone https://github.com/peggypkchiu/finalCapstone.git" into the terminal of your local system.

Usage of the project: further analysis other data in data file and explore function to analyse sentiment for Amazon product reviews.
