
# LLM Product Sentiment Collector

This project utilizes the Phi-3 LLM through Ollama as well as the web scraper BeautifulSoup4 and graphing software Matplotlib in order to:

- Scrape the review data from several products on ebay.
- Query Phi-3 in order to gather sentiments on the products.
- Display the sentiment data in bar graph format.

## Product Data Gathered

The product sentiments gathered were all from the "Playstation" family of video game consoles, specifically:

- Playstation 1
- Playstation 2
- Playstation 4
- Playstation 5

These sentiments were then compiled into a bar graph as seen below:
![Sentiments Graph](https://github.com/JacobLStephens/Local-LM-Querying/blob/Sentiments/Playstation%20Sentiments%20Graph.png)
This graph shows an overwhelmingly positive response to each product.

## Features

- Scrapes both the titles and reviews from the given ebay URLs using BeautifulSoup4.
- Uses Ollama to ask Phi-3 about sentiments on each review.
- Creates a stylized bar chart of the data using Matplotlib.
- Utilizes abstract base classes (abc) in order to allow for specialization of classes without direct modification, complying to SOLID principles.
- Uses specialty testing scripts through Pytest to strengthen class integrity.
- Allows for any number of products and keyword filtering through modular class design.
- requirements.yml file included for easy environment setup.

## Requirements/Setup

This program utilizes several python modules/dependencies, including:

- BeautifulSoup4
- requests
- lxml
- ollama
- matplotlib 
- abc 
- pytest 

All of these dependencies are included in the requirements.yml file, which can be utilized by the following steps:

### 1. Installing Conda
Miniconda, a lightweight environment manager, can be downloaded [here.](https://docs.anaconda.com/miniconda/miniconda-install/)

Note: this project is running on python version 3.13.0

### 2. Creating Your Environment
Using the requirements.yml file, all required dependancies can be downloaded with the following command:

`conda env create -n env_name  -f requirements.yml`

After activating you environment with `conda activate env_name`, you will have a complete environment ready to use for web scraping.

## Usage Information (Web Scraping)
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

## Usage Information (LLM Querying)
In order to create the Phi-3 sentiments, follow these steps:

### 1. Run the Web Scraper
Utilize the prior instructions to run the web scraper, getting access to the review files.

### 2. Change the File Names as Needed
Within the code, there are two arrays with specific file names. These are as follows:

`infilenames = ["PS1Reviews.txt", "PS2Reviews.txt", "PS4Reviews.txt", "PS5Reviews.txt"]`

`outfilenames = ["PS1Sentiments.txt", "PS2Sentiments.txt", "PS4Sentiments.txt", "PS5Sentiments.txt"]`

Simply change these names to your preferred input file and output file names.

### 3. Run the program

The final step is to run the program with the following command:

`python main.py`

and now you have a new file with all the sentiments!

## Usage Information (Chart Making)

In order to organize these sentiments into a bar chart, follow these steps:

### 1. Run the LLM Querying Program

Utilize the prior instructions to run the LLM querying program, getting access to the sentiment files.

### 2. Change the File Names as Needed

Within the code, there is one array containing specific file names:

`product_files = ["PS1Sentiments.txt", "PS2Sentiments.txt", "PS4Sentiments.txt", "PS5Sentiments.txt"]`

Simply change these names to your preferred input file.

### 3. Run the Program

The final step is to run the program with the following command:

`python Graph_Data.py`

and now you have a bar graph with all the sentiments!

-Created by Jacob Stephens-
