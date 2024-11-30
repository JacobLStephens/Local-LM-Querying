from LLM_Comm import LLMComm
import ollama as ol

class Phi3Querying(LLMComm):

    def query_LLM(self, reviews):
        sentiments = []
        for r in reviews:
            response = ol.chat(model='Phi3:mini', messages=[
            {
                'role': 'user',
                'content': r,
            },
        ])
            sentiments.append(response['message']['content'])
        return sentiments