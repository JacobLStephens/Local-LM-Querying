
# Ebay Product Reviews Web Scraper
This project utilizes the BeautifulSoup4 and requests modules in order to automatically scrape product titles and reviews from given Ebay Urls.




## Products Scraped
The products scraped were all from the "Playstation" family of video game consoles, specifically:

- Playstation 1
- Playstation 2
- Playstation 4
- Playstation 5


## Features

- Scrapes both the titles and reviews from the given ebay URLs.
- Supports creation of multiple .txt files for different products.
- Accepts any number of URLs within an input file.
- requirements.yml file included for easy environment setup.




## Requirements/Setup

This program utilizes several python modules/dependencies, including:
- BeautifulSoup4
- requests
- lxml

All of these dependencies are inlcuded in the requirements.yml file, which can be utilized by the following steps:

### 1. Installing Conda
Miniconda, a lightweight environment manager, can be downloaded [here.](https://docs.anaconda.com/miniconda/miniconda-install/)

Note: this project is running on python version 3.13.0

### 2. Creating Your Environment
Using the requirements.yml file, all required dependancies can be downloaded with the following command:

`conda env create -n env_name  -f requirements.yml`

After activating you environment with `conda activate env_name`, you will have a complete environment ready to use for web scraping.


## Usage Information
Now that you have your environment setup, you can scrape your reviews in just a few simple steps:

### 1. Create a URL File

Create a URL.txt file containing all of the URLs for the product pages you wish to scrape. Please note that you will need a URL for each page of reviews you want to use, and a seperate URL.txt file for each different product you wish to scrape.

### 2. Change the File Names as Needed
Within the code, there are several function calls with specific file names. These are as follows:

`write_reviews("PS1Reviews.txt", "PS1URLs.txt")`
`write_reviews("PS2Reviews.txt", "PS2URLs.txt")`
`write_reviews("PS4Reviews.txt", "PS4URLs.txt")`
`write_reviews("PS5Reviews.txt", "PS5URLs.txt")`

These are formatted with the output file as the first variable, and the input file containing the URLs as the second variable. Simply change these names to your preferred output file name and your chosen URL file name.

### 3. Run the Program

The final step is to run the program with the following command:

`python Web_scraper.py`

and now you have a new file with all the comments and titles!

-Created by Jacob Stephens as part of a larger LLM project-