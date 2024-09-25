# # from selenium import webdriver

# # # Set up Chromium options
# # options = webdriver.ChromeOptions()
# # options.add_argument('--headless')  # Run in headless mode (no GUI)

# # # Path to your Chromium webdriver executable
# # chromedriver_path = '/chrome-win64/chrome'

# # # Initialize the WebDriver
# # driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# # # URL to scrape
# # url = 'https://www.nhs.uk/conditions/'

# # # Open the URL in the browser
# # driver.get(url)

# # # Find the ul tag with class "uhsul"
# # ul_element = driver.find_element_by_class_name('uhsul')

# # # Extract text from the ul element
# # 

# # # Print the text content of the ul element
# # print(ul_text)

# # # Close the WebDriver
# # driver.quit()
# import os
# from selenium import webdriver
# driver = webdriver.Chrome()
# url = 'https://www.nhs.uk/conditions/'
# driver.get(url)
# ul_element = driver.find_element(By.ID, "clickable")
# # ul_element = driver.find_element_by_class_name('uhsul')
# ul_text = ul_element.text
# print(ul_text)
# driver.quit()
