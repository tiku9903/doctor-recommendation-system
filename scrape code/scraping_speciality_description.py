import requests
from bs4 import BeautifulSoup
import re
import csv

# Function to remove special characters
def remove_special_characters(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

# URL to scrape
url = 'https://www.aucmed.edu/about/blog/a-complete-list-of-medical-specialties-and-subspecialties'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div element with specified class
    div_element = soup.find('div', class_="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item")
    if div_element:
        # Open a text file to append data
        with open("output.txt", "a", encoding="utf-8") as file:
            # Find all h2 tags inside the div
            h2_tags = div_element.find_all('h2')

            # Iterate through each h2 tag
            for index, h2_tag in enumerate(h2_tags):
                # Write h2 tag text to file as a heading
                file.write(f"\nHeading {index + 1}: {h2_tag.get_text()}\n")

                # Find the next sibling of h2 tag
                next_sibling = h2_tag.find_next_sibling()

                # Iterate through siblings until the next h2 tag
                while next_sibling and next_sibling.name != 'h2':
                    if next_sibling.name == 'p':
                        # Write the text content of p tag to the file
                        file.write(f"Paragraph Text: {remove_special_characters(next_sibling.get_text())}\n")
                    elif next_sibling.name == 'ul':
                        # Find all li tags inside the ul tag
                        li_tags = next_sibling.find_all('li')
                        # Write the text content of each li tag to the file
                        for li_tag in li_tags:
                            file.write(f"List Item Text: {remove_special_characters(li_tag.get_text())}\n")
                    # Move to the next sibling
                    next_sibling = next_sibling.find_next_sibling()
    else:
        print("No div element with specified class found on the page.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


