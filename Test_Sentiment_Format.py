#This file tests the SentimentFormatting class functionality on a sample data set, including reading, formatting, and writing the data

import pytest
import os
from Sentiment_Format import SentimentFormatting

#sample data
TEST_INFILE = 'test_input.txt'
TEST_OUTFILE = 'test_output.txt'
DATA = ["test1", "test2", "test3"]
FORMATTED_DATA = [
    "Please tell me whether this comment: test1 is positive, negative, or neutral, only outputting one of those 3 words. ONLY output Positive, Negative, or Neutral.",
    "Please tell me whether this comment: test2 is positive, negative, or neutral, only outputting one of those 3 words. ONLY output Positive, Negative, or Neutral.",
    "Please tell me whether this comment: test3 is positive, negative, or neutral, only outputting one of those 3 words. ONLY output Positive, Negative, or Neutral.",
]

#Creates a pytest fixture to create the formatting class, passed to tests
@pytest.fixture
def formatting_initializer():
    return SentimentFormatting()

#Tests successfully reading in a file by checking data against DATA set
def test_reading_file(formatting_initializer):
    with open(TEST_INFILE, "w+", encoding="utf8") as fl:
        fl.writelines(line + "\n" for line in DATA)

    data = formatting_initializer.readin(TEST_INFILE)

    if os.path.exists(TEST_INFILE):
        os.remove(TEST_INFILE)

    assert data == [line + "\n" for line in DATA] #Should be the same

#Test the formatting feature
def test_formatting(formatting_initializer):
    formatted_data = formatting_initializer.format(DATA)
    assert formatted_data == FORMATTED_DATA #Should be the same

#Test writing to the outfile
def test_writing_outfile(formatting_initializer):
    formatting_initializer.writeto(FORMATTED_DATA, TEST_OUTFILE)

    with open(TEST_OUTFILE, "r", encoding="utf8") as fl:
        data = fl.readlines()
    
    if os.path.exists(TEST_OUTFILE):
        os.remove(TEST_OUTFILE)

    assert data == [line + "\n" for line in FORMATTED_DATA] #Should be the same