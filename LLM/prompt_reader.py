# This program reads in prompts for the LLM Phi-3 mini from a prompts text file, feeding them into the LLM using the ollama module, 
# then gathering the responses and putting them into another text file. This is the beginning of a larger LLM project.
#// Created by Jacob Stephens //#

# Module that allows direct interaction between the program and Phi-3 mini via ollama
import ollama as ol

# open initial prompt file, use readlines to put into a list
infile = open("prompts.txt", "r") 
prompts = infile.readlines()
infile.close()

# open file to store answers, creates file if it does not exist
outfile = open("answers.txt", "w+")

# loops through every question, asking them one by one using the ollama modules "chat" function
for p in prompts:
    response = ol.chat(model='Phi3:mini', messages=[
        {
            'role': 'user',
            'content': p,
        },
    ])

# prints the responses and puts them into the specified file (still in for loop)
    print (response['message']['content'])
    outfile.write(response['message']['content'])
    outfile.write("\n")
