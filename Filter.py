#This class takes in the data from Phi3Querying and strips it of extraneous information, returning just the one word sentiments

class Filter():

    def filter(self, data, keywords): #takes in the raw sentiments data and a list of words to extract

        data_stripped = [] 

        for word in keywords:
            for line in data:
                index = line.find(word)
                if index != -1: #word is found
                    data_stripped.append(word) #add it to a list
                
            
        return data_stripped
