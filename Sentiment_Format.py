from Format_Reviews import FormatReviews

class SentimentFormatting(FormatReviews):

    def readin(self, infilename):
        infile = open(infilename, "r", encoding="utf8")
        data = infile.readlines()
        infile.close()
        
        return data

    def format(self, data):
        formatted_data = []
        for line in data:

            line = "Please tell me whether this comment: " + line + " is positive, negative, or neutral, only outputting one of those 3 words. ONLY output Positive, Negative, or Neutral."
            formatted_data.append(line)
        
        return formatted_data
    
    def writeto(self, data, outfilename):
        outfile = open(outfilename, "w+", encoding="utf8")
        for line in data:
            outfile.write(line)
            outfile.write("\n")
