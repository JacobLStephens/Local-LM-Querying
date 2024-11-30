# This program utilizes the review data scraped from the Web_scraper.py program, feeding it into Phi-3 using ollama in order to get a list of sentiments on a product.
# This program also utilizes 3 seperate classes: Phi3Querying, SentimentFormatting, & Filter, in order to read in, polish, query, and output a list of sentiments.

# Phi3Querying and SentimentFormatting are based on abstract base classes (LLM_Comm & Format_Reviews respectively), allowing for creation of different modules based on other 
# LLMs or formatting styles, in accordance with the Dependency Inversion Principle and Open-Closed Principle of SOLID.

##Created by Jacob Stephens##

#Import necessary classes
from Phi3_Querying import Phi3Querying
from Sentiment_Format import SentimentFormatting
from Filter import Filter

#Create lists of infile and outfile names
infilenames = ["PS1Reviews.txt", "PS2Reviews.txt", "PS4Reviews.txt", "PS5Reviews.txt"]
outfilenames = ["PS1Sentiments.txt", "PS2Sentiments.txt", "PS4Sentiments.txt", "PS5Sentiments.txt"]

#Instantiate classes
query = Phi3Querying()
formatting = SentimentFormatting()
filtering = Filter()

#List of keywords for use in the filter class
keywords = ["Positive", "Negative", "Neutral"]
i = 0 #count for outfile

#Loop for each file given
for name in infilenames:
    reviews = formatting.readin(name) #Read in the file
    formatted_reviews = formatting.format(reviews) #Format the file, allowing for proper questioning
    sentiments = query.query_LLM(formatted_reviews) #Gather sentiments from LLM
    filtered_sentiments = filtering.filter(sentiments, keywords) #Remove extraneous information
    formatting.writeto(filtered_sentiments, outfilenames[i]) #Write to the matching outfile, based on i value
    i = i+1 #iterate to next outfile