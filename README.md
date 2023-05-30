# Confluence Dead Pages Search

This code utilizes Selenium, a web automation library, to perform automated actions on a website. The purpose of the code is to navigate through the pages of the directory, visit each space, and determine if the space is alive or dead based on its title.

The code reads the username and password from a file called "credentials.txt" and uses them to log in to the website. It then proceeds to iterate through the pages of the directory, visiting each space and checking its title. If the title is "Page Not Found," the space is considered dead, and its link is added to the dead_spaces list. Otherwise, it is considered alive.

The code uses Selenium's WebDriver to interact with the website, locating elements by their CSS selectors and performing actions such as sending keys and clicking buttons. It also utilizes the WebDriverWait class to wait for specific elements to be present before proceeding.

# Setup and Installation:
 
# 1. Install Selenium: pip install selenium
Download the appropriate ChromeDriver executable for your operating system and place it in the specified location (chrome_driver_path variable).
Create a file called "credentials.txt" and enter your username and password on separate lines.
Usage:

# 2. Run the code using a Python interpreter.

The code will open a headless Chrome browser and log in to the website using the provided credentials.
It will then navigate through the pages of the directory, visiting each space and checking if it is alive or dead based on its title.
The status of each space will be printed to the console, and the links of dead spaces will be stored in the dead_spaces list.
The code will continue to navigate through the pages until all pages have been processed.
After the execution, you can access the list of dead space links in the dead_spaces list.

# 3. Customization:

Modify the chrome_driver_path variable to specify the path to the ChromeDriver executable on your system.
Adjust the CSS selectors and element IDs in the code to match the structure of the website if necessary.
You can add additional logic or actions based on your specific requirements.

# 4. Dependencies:

Selenium: The code relies on the Selenium library to automate web interactions. Ensure that it is installed (pip install selenium).

# Note:

The code assumes that the website structure remains unchanged. If there are any changes to the website's HTML structure or CSS selectors, the code may need to be updated accordingly.
Use this code responsibly and in compliance with the website's terms of service.
Confluence's usage of AJAX technology may require additional script execution to interact with elements correctly. Modify the script execution as necessary to handle AJAX interactions.
