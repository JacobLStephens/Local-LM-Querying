# This program uses the BeautifulSoup4 & requests modules to scrape the data for 5 different iterations of the Playstation on Ebay, 
# pulling out the reviews on for each of them and storing them back in seperate files.
# This program is a part of a larger LLM project.

##Created by Jacob Stephens##

#import the BeautifulSoup & requests modules
import requests
from bs4 import BeautifulSoup

# This function reads in a list of urls read in from a different function,
# then uses BeautifulSoup & requests to look through the html, pulling out both the title of the reviews as well as ther contents.
# The review titles and contents are then retrurned as a list.
def scrape_data(urls):
    reviews = []

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        review_sections = soup.find_all('div', class_='ebay-review-section')
        
        #no more reviews
        if not review_sections:
            break

        #break the reviews into parts
        for review in review_sections:
            title_tag = review.find('h3', itemprop='name')
            body_tag = review.find('p', itemprop='reviewBody')

            if title_tag and body_tag:
                title = title_tag.get_text(strip=True)
                body = body_tag.get_text(strip=True)
                reviews.append(f"Title: {title} Comment: {body}\n")

    #return list of reviews and titles
    return reviews

# This function reads in a filename, then reads that file line by line and puts it into a list to be used in the scrape_data function
def read_urls(filename):
    infile = open(filename, 'r')
    urls = infile.readlines()
    infile.close()
    return urls

# This function reads in the outfilename & infilename, then invokes the data scraping function to get a list of data to put into the new file.
def write_reviews(outfilename, infilename):
    outfile = open(outfilename, 'w+', encoding = 'utf-8')
    reviews = scrape_data(read_urls(infilename))
    for review in reviews:
        outfile.write(review)

# Main code block, invoke write_reviews for each file
write_reviews("PS1Reviews.txt", "PS1URLs.txt")
write_reviews("PS2Reviews.txt", "PS2URLs.txt")
write_reviews("PS4Reviews.txt", "PS4URLs.txt")
write_reviews("PS5Reviews.txt", "PS5URLs.txt")

