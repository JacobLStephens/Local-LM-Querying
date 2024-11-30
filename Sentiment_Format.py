#This class serves to manipulate the review data. It reads in the review data from the webscraper, formats the data to be presented to the LLM, and writes the filtered data to the outfile.

#Utilizes an abc, allows for different classes with other formatting styles
from Format_Reviews import FormatReviews

class SentimentFormatting(FormatReviews):

    #Reads in the file
    def readin(self, infilename):
        infile = open(infilename, "r", encoding="utf8")
        data = infile.readlines()
        infile.close()
        
        return data

    #Formats the data to prompt the LLM properly
    def format(self, data):
        formatted_data = []
        for line in data:

            line = "Please tell me whether this comment: " + line + " is positive, negative, or neutral, only outputting one of those 3 words. ONLY output Positive, Negative, or Neutral."
            formatted_data.append(line)
        
        return formatted_data
    
    #Writes the finished data to an outfile
    def writeto(self, data, outfilename):
        outfile = open(outfilename, "w+", encoding="utf8")
        for line in data:
            outfile.write(line)
            outfile.write("\n")
