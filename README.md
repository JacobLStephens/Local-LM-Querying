LLM PROJECT

This a project in which a Local Language Model (phi3 mini) is fed a file of prompts, with the responses then copied to another file. It is the first step in a larger LM project.

The project, as it currently stands, consists of the following:
1. A text file containing prompts, prompts.txt. This file holds the questions to be fed to the LLM.
2. A python file prompt_reader.py. This file reads in prompts.txt, makes contanct with the LLM, and puts its answers into a new file, answers.txt.
3. A text file containing answers, answers.txt. This file holds the answers the LLM gave to the prompts. It is replaced with new answers when the program is run.
4. A yaml file requirements.yaml. This file contains information on the environment used as well as the modules required to run prompt_reader.py.

Along with the modules in requirements.yaml, this program requires ollama and phi3 mini.
Ollama can be downloaded from their official website [here]([url](https://ollama.com/))
Once Ollama is downloaded, phi3 mini can be downloaded by running the following terminal command: ollama run phi3:mini

(This project is a work in progress, and will be updated as it evolves)
