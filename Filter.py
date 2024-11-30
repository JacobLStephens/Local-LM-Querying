class Filter():

    def filter(self, data, keywords):

        data_stripped = [] 

        for word in keywords:
            for line in data:
                index = line.find(word)
                if index != -1:
                    data_stripped.append(word)
                
            
        return data_stripped
