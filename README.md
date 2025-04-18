# Image Web Scraper for Philippine Medicinal Plant Image Classifier Model
This Web Scraper is for gathering images to be used on model training and testing the model/s that the Philippine Medicinal Plant Classifier. It uses Selenium to automate Google Chrome and Requests to grab and download the images.

this can also be used to scrape just about anything as long as its in Google (in the images tab)


# Needed Libraries and Dependencies
- Pillow (pip install Pillow)
- Selenium (pip install selenium)
- Requests (pip install requests)

# How to use
- Run the program webscraperCHROME.py
- Input the asked inputs
- Scan Length is how many image containers the program will use to try and download HD Images from
- Scan Delay is how duration before the scanner will move on to the next container after finishing the scan on the current container
- Scan Load Time is how long the scanner will wait for the HD image will generate before moving on

# What I learned
- web scraping techniques using web automation 
