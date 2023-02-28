"""
    Title: Data Analytics Lab 3: Data Collection (Questions 1 - 8)
    Author: Aaron Goldstein
    Date: 2/25/2023
    Github: https://github.com/Windz-GameDev

    The purpose of this program is to make a simple API query, and to find matching headlines based on certain
    keywords from the Google News website. The functionality for querying an API, and finding matching headlines by keywords
    is contained in their respective functions, and examples for how to call those functions can also be found in this program.
    Beautiful soup is the tool used for the web scraping functionality in this program.
"""

import requests
from bs4 import BeautifulSoup

"""
  This function takes an API resource, and query parameters as input, and uses them to print the
  response status code, the response headers, and the response content in key-value pairs.
"""


def queryAPI(apiResource, queryParams):
    serverResponse = requests.get(apiResource, params=queryParams)
    print("\n-----------------------------------")
    print("API Query Information:")
    print("-----------------------------------\n")
    print("Status Code: ", serverResponse.status_code)
    print("Response Headers: ", serverResponse.headers)
    if 'application/json' in serverResponse.headers.get('content-type', '').lower():  # make sure the content is stored as JSON before printing it as such
        print("Response Content: ", serverResponse.json())
    else:
        print("Response Content: ", serverResponse.content)  # Otherwise, display the raw response content


"""
  Takes a list of headlines, and variable length argument of keywords as input. It then
  uses this input to return a list of only the headlines that contain each keyword inside their text. 
"""


def find_headline_by_keyword(headlines, *keywords):
    foundMatchingHeadlines = []
    for currentHeading in headlines:
        isMatchingHeadline = True  # assume heading is matching until proven otherwise
        for keyword in keywords:
            if not (keyword.lower() in currentHeading.text.lower()):  # if any keyword does not match the heading's text, it is not a matching heading, therefore the heading will not be appended to matching headings list.
                isMatchingHeadline = False  # identify that the heading is not matching
                break  # no longer need to check other keywords if one is not matching
        if isMatchingHeadline:  # if all keywords matched, append the heading to the matching headlines list
            foundMatchingHeadlines.append(currentHeading)
    return foundMatchingHeadlines


"""
  Testing our queryAPI function. 
  Here we are providing the api resource https://api.datamuse.com/, and 
  the query parameter https://api.datamuse.com/words?rel_rhy=forgetful. 
  As a result, this call will be used to find words that rhyme with forgetful.
"""

queryAPI("https://api.datamuse.com/words", {"rel_rhy": "forgetful"})

"""
   This following section of code is intended to answer question 10. 
  
   The code below uses the findAll() function from beautiful soup, to scrape all headlines from the google news website existing under
   the h4 heading. Afterwards, it loops through all the headings retrieved, printing each, then finds matching headings to certain keywords
   with a function call, then prints each matching headline.
"""

response = requests.get("https://news.google.com/")  # Returns a response object, containing the html content in the content attribute.
soup = BeautifulSoup(response.content, "html.parser")  # Creates a beautiful soup object that parses the html, and provides a data structure that can be searched and manipulated in the following code.
headings = soup.findAll('h4')  # Finds all the headlines under the h4 heading

print("\n-----------------------------------")
print("All Headlines")
print("-----------------------------------\n")

for heading in headings:  # Prints each headline on the page 
    print(heading.text)

# Provide our keywords and return the result of the function call to a matching headlines list
matchingHeadlines = find_headline_by_keyword(headings, "Supreme", "Court")
print("\n-----------------------------------")
print("Matching Headlines")
print("-----------------------------------\n")
for matchingHeadline in matchingHeadlines:
    print(matchingHeadline.text)


print("\n")
