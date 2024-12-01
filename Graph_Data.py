#This script utilizes matplotlib to organize the sentiments collected from the main script into a bar graph.
#(Note: I kept this script seperate from main.py due to the large overhead associated with querying the LLM, allowing this to run seperately allows for quick graph creation)

#Import necessary modules & classes
import numpy as np
import matplotlib.pyplot as plt
from Count_Instances import CountInstances #Used to count the number of a certain keyword, specialty made for this script
from Sentiment_Format import SentimentFormatting

#Setup graph sizing
barWidth = 0.25
fig = plt.subplots(figsize = (12, 8))

#Instantiate variables
product_files = ["PS1Sentiments.txt", "PS2Sentiments.txt", "PS4Sentiments.txt", "PS5Sentiments.txt"]
keywords = ["Positive", "Negative", "Neutral"]
Negative = []
Positive = []
Neutral = []

#Instantiate classes
counting = CountInstances()
formatting = SentimentFormatting()

#Count up the number of each sentiment
for product in product_files:
    sentiments = formatting.readin(product)
    num_sentiments = counting.count(sentiments, keywords)
    Positive.append(num_sentiments[0])
    Negative.append(num_sentiments[1])
    Neutral.append(num_sentiments[2])

#
bar1 = np.arange(len(Negative))
bar2 = [x + barWidth for x in bar1]
bar3 = [x + barWidth for x in bar2]

plt.bar(bar1, Negative, color = "r", width = barWidth, edgecolor = "black", label = "Negative")
plt.bar(bar2, Positive, color = "b", width = barWidth, edgecolor = "black", label = "Positive")
plt.bar(bar3, Neutral, color = "y", width = barWidth, edgecolor = "black", label = "Neutral")

plt.xlabel("Product", fontweight = "bold", fontsize = 15)
plt.ylabel("Number of Sentiments", fontweight = "bold", fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Negative))], ["PS1", "PS2", "PS4", "PS5"])

plt.legend()
plt.show()