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