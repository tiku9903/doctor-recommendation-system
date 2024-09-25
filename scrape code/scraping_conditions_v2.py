import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://www.nhs.uk/conditions/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    div_element = soup.find('div', class_="nhsuk-card__content nhsuk-card__content--feature")

    if div_element:
        div_text = div_element.get_text()
        print(div_text)
    else:
        print("No relevant div element found.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
