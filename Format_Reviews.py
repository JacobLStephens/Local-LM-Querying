#This class, Format_reviews, serves as an abstract base class (ABC) that defines file & data manipulation functions, 
#allowing specialization of data formatting through definitions of other classes
#This adheres to the Dependency Inversion Principle and Open-Closed Principle of SOLID.

from abc import ABC, abstractmethod

class FormatReviews(ABC):

    @abstractmethod
    def readin(self, infilename):
        pass

    @abstractmethod
    def format(self, data):
        pass

    @abstractmethod
    def writeto(self, data, outfilename):
        pass