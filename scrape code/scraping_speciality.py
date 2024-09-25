import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://www.aucmed.edu/about/blog/a-complete-list-of-medical-specialties-and-subspecialties'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the ul tag with class "uhsul"
    div_element = soup.find('div', class_="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item")
    if div_element:
        # Find all p tags inside the div
        p_tags = div_element.find_all('p')
        
        # Find all h1 tags inside the div
        h2_tags = div_element.find_all('h2')
        
        li_tags = div_element.find_all('li')

        # Process the p tags
        for p_tag in p_tags:
            print("Paragraph Text:", p_tag.get_text())

        # Process the h1 tags
        for h2_tag in h2_tags:
            print("Heading Text:", h2_tag.get_text())
            
        for li_tag in li_tags:
            print("Heading Text:", li_tag.get_text())

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
