#This class, LLMComm, serves as an abstract base class (ABC) that defines a query_LLM function, allowing specialization of queries using other LLMs through definitions of other classes
#This adheres to the Dependency Inversion Principle and Open-Closed Principle of SOLID.

#abc allows for the use of abstract base classes
from abc import ABC, abstractmethod

class LLMComm(ABC):
    
    @abstractmethod
    def query_LLM(self, reviews):
        pass