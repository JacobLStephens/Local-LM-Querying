#This class takes in the stripped sentiment data and returns a count of each in list format

class CountInstances():

    def count(self, data, keywords): 

        data_count = [] 

        for word in keywords:
            count = 0
            for line in data:
                index = line.find(word)
                if index != -1: #word is found
                    count = count + 1
                    
            data_count.append(count) #add the number of times a word is found to a list
            
        return data_count
