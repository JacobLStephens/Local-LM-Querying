#This script utilizes matplotlib to organize the sentiments collected from the main script into a bar graph.
#(note: I kept this script seperate from main.py due to the large overhead associated with querying the LLM, allowing this to run seperately allows for quick graph creation)

#import necessary modules
import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25
fig = plt.subplots(figsize = (12, 8))

Negative = []
Positive = []
Neutral = []

