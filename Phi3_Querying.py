#This class interacts directly with the Phi-3 model, asking questions about the reviews that were formatted by the SentimentFormatting class. It returns Phi-3's answers.

#Utilizes an abc, allows for other classes with different LLM models
from LLM_Comm import LLMComm
import ollama as ol

class Phi3Querying(LLMComm):

    def query_LLM(self, reviews):
        sentiments = []
        for r in reviews:
            response = ol.chat(model='Phi3:mini', messages=[ #Interfacing with Phi-3 via ollamas
            {
                'role': 'user',
                'content': r,
            },
        ])
            sentiments.append(response['message']['content'])
        return sentiments