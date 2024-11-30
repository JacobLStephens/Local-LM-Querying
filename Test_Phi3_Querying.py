#This file tests the Phi3Querying class for multiple edge cases

import pytest
from Phi3_Querying import Phi3Querying

#Creates a pytest fixture to create the querying class, passed to tests
@pytest.fixture
def Phi3_initializer():
    return Phi3Querying()

#Tests when an empty input list is given
def test_empty_query(Phi3_initializer):
    reviews = []
    result = Phi3_initializer.query_LLM(reviews)
    assert result == [] #Should return an empty list

#Tests when the input list is a single review
def test_single_query(Phi3_initializer):
    reviews = ["this is a single review"]
    result = Phi3_initializer.query_LLM(reviews)
    assert len(result) == 1