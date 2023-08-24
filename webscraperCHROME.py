import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import io
from PIL import Image

driver= webdriver.Chrome()
search_url = "https://www.google.com/search?sca_esv=559310888&rlz=1C1ONGR_enPH1008PH1008&sxsrf=AB5stBhMA_Aut7fIUnqZ_YZYZ8DlmvJ05g:1692768474036&q=Alliaceae+Allium+odorum+L.&tbm=isch&source=lnms&sa=X&ved=2ahUKEwikttP8hfKAAxV8bmwGHU0iAZUQ0pQJegQIDhAB&biw=1920&bih=894&dpr=1"
download_path = "D:/Workstuff/Thesis/Alliaceae Allium odorum L/"
driver.get(search_url)


def scrape_initilaization(max_images):
    thumbnails =[]
    foundimage_reached = False

    while foundimage_reached == False:
        if len(thumbnails) < max_images:
            current_thumbnail_len = len(thumbnails)

            driver.execute_script("window.scroll(0, document.body.scrollHeight);")
            load_more_button = driver.find_elements(By.CLASS_NAME, "LZ4I")

            thumbnails = driver.find_elements(By.CLASS_NAME, "Q4LuWd")
            thumbnails = list(dict.fromkeys(thumbnails))

            if len(load_more_button) > 0:
                print("Loading More Images...")
                print(len(thumbnails))
                driver.find_element("xpath", """//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input""")
                time.sleep(5)

            
                   
        else:
            foundimage_reached = True
           
    return thumbnails

def download_image(download_path, url, filename):
    successful_download = True
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + filename

        with open(file_path, 'wb') as f:
            image.save(f, format='JPEG')

        print("Image Dowloaded")
    except:
        successful_download = False

    return successful_download

def start_scan(delay, max_images, load_time):
    

    thumbnails = scrape_initilaization(max_images)

    image_saved = []
    i = 0

    for img in thumbnails[len(image_saved):max_images]:
            try:
                HD_image = False
                img.click()
                time.sleep(delay)
                load_counter = 0

                while HD_image == False:
                    imageElement = driver.find_element("xpath", """//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]""")
                    image_src = imageElement.get_attribute("src")

                    if "http" in image_src and "encrypted-tbn0" not in image_src:
                        HD_image = True
                        print(image_src)
                        image_saved.append(image_src)
                    else:
                        
                        load_counter += 1
                        time.sleep(1)
                        if load_counter == load_time:
                            break
                        else: 
                         continue
                #print(image_src)

                i+=1
                print(i)
            except:
                continue
            
    return image_saved
            #r48jcc pT0Scc iPVvYb

                #//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]

def start_scrape():
    unsuccessful_download_counter = 0
    scan_length = int(input("Please Input Image Scan Length -> "))
    scan_delay = int(input("Please Input Image Scan Delay -> "))
    scan_loadtime = int(input("Please input Image Scan Load Wait Time -> "))
    image_download= ""
    Found_HD_Images = start_scan(scan_delay, scan_length, scan_loadtime)
    i = 0

    while image_download == "":
        image_download = input((str(len(Found_HD_Images)) + " " + "HD Images Found, Input new scan parameters? Y/N -> ")) 

        if image_download == "Y":
            print("Starting New Scan...")
            scan_length = int(input("Please Input Image Scan Length -> "))
            scan_delay = int(input("Please Input Image Scan Delay -> "))
            scan_loadtime = int(input("Please input Image Scan Load Wait Time -> "))
            Found_HD_Images = start_scan(scan_delay, scan_length, scan_loadtime)
            image_download = ""
            continue
        elif image_download == "N":
            print("Proceding with image download")
            break
        else:
            image_download = ""
            continue
 
    for link in Found_HD_Images:
        if download_image(download_path, link, str(i) + ".jpg") == False:
            unsuccessful_download_counter += 1

        i += 1

    print("Image Scraping Completed. " + str(unsuccessful_download_counter) + " Images Unsuccessfuly Downloaded")

 
start_scrape()
driver.quit()

    
    
    