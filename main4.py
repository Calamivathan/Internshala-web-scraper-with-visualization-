from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.parse
import execjs

# URL of the webpage
url = "https://internshala.com/internships/"

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open the webpage
driver.get(url)

# Wait for the page to load (adjust wait time as needed)
time.sleep(2)

try:
    # Find the select element with specified attributes
    select_element = driver.find_element(By.CSS_SELECTOR, 'select[name="select_category"].form-control.chosen-select.default-chosen')
    
    # Initialize a list to store the selected options
    selected_options = []
    
    # Iterate over all option elements and select them
    options = select_element.find_elements(By.TAG_NAME, 'option')
    for option in options:
        selected_options.append(option.get_attribute('value'))
    
    # Print the selected options
    print("Selected options:", selected_options)
    
    # Write the selected options to list_p.py file
    with open('Your_directory_location\Functions\list_p.py', 'w') as f:
        f.write("selected_options = " + str(selected_options))

except Exception as e:
    print("Error occurred:", e)

finally:
    # Close the browser
    driver.quit()

# Define the JavaScript function
js_function = """
function make_string_seo_friendly(a, c) {
    c && (a = decodeURIComponent(a));
    a = a.replace(/[^0-9a-zA-Z,]/g, "-");
    a = a.replace(/--+/g, "-");
    a = a.replace(/-,/g, ",");
    return a = a.replace(/^-|-$|^(-)+|(-)+$/g, "")
}
"""

# Create a JavaScript context
context = execjs.compile(js_function)

# Initialize a list to store the processed strings
processed_strings = []

# Iterate over the data
for item in selected_options:
    # Decode the URI component
    decoded_item = urllib.parse.unquote(item)
    
    # Call the JavaScript function with the item and decode flag
    processed_item = context.call("make_string_seo_friendly", item, True)
    
    # Append the processed item to the list
    processed_strings.append(processed_item)
    # print(processed_item)

# Write the processed strings to list_p.py file
with open('Your_directory_location\Functions\list_p.py', 'w') as f:
    f.write("\nprocessed_strings = " + str(processed_strings))
