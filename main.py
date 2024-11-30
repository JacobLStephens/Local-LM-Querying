from Phi3_Querying import Phi3Querying
from Sentiment_Format import SentimentFormatting
from Filter import Filter

infilenames = ["PS1Reviews.txt", "PS2Reviews.txt", "PS4Reviews.txt", "PS5Reviews.txt"]
outfilenames = ["PS1Sentiments.txt", "PS2Sentiments.txt", "PS4Sentiments.txt", "PS5Sentiments.txt"]

query = Phi3Querying()
formatting = SentimentFormatting()
filtering = Filter()

keywords = ["Positive", "Negative", "Neutral"]
i = 0

for name in infilenames:
    reviews = formatting.readin(name)
    formatted_reviews = formatting.format(reviews)
    sentiments = query.query_LLM(formatted_reviews)
    filtered_sentiments = filtering.filter(sentiments, keywords)
    formatting.writeto(filtered_sentiments, outfilenames[i])
    i = i+1