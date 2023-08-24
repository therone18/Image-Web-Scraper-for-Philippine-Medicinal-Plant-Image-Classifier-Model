import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import io
from PIL import Image

driver= webdriver.Chrome()
search_url = "https://www.google.com/search?q=Verbenaceae++Lantana+camara+L.+&tbm=isch&ved=2ahUKEwjp1KqNw-WAAxUVzaACHV5xBU8Q2-cCegQIABAA&oq=Verbenaceae++Lantana+camara+L.+&gs_lcp=CgNpbWcQAzoKCAAQigUQsQMQQzoHCAAQigUQQzoICAAQgAQQsQM6BQgAEIAEOgcIIxDqAhAnUJIKWIwUYKkYaAFwAHgBgAHEA4gB-wiSAQkwLjMuMS4wLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=HgjfZOnNO5Wag8UP3uKV-AQ&bih=894&biw=1185&rlz=1C1ONGR_enPH1008PH1008"
driver.get(search_url)



def scrape_initilaization(max_images):
    thumbnails =[]
    foundimage_reached = False

    while foundimage_reached == False:
        if len(thumbnails) < max_images:
            driver.execute_script("window.scroll(0, document.body.scrollHeight);")
            thumbnails = driver.find_elements(By.CLASS_NAME, "Q4LuWd")
            thumbnails = list(dict.fromkeys(thumbnails))
            
        else:
            foundimage_reached = True
            print(foundimage_reached)

    return thumbnails


def download_image(download_path, url, filename):

    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path + filename

    with open(file_path, 'wb') as f:
        image.save(f, format='JPEG')

    print("Image Dowloaded")

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

                    if "http" in image_src:
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
    scan_length = int(input("Please Input Image Scan Length -> "))
    scan_delay = int(input("Please Input Image Scan Delay -> "))
    scan_loadtime = int(input("Please input Image Scan Load Wait Time -> "))
    image_download= ""
    #Found_HD_Images = start_scan(scan_delay, scan_length, scan_loadtime)
    while image_download== "":
        
        if image_download == "Y":
            print ("Starting Download")
            break
        else:
            Found_HD_Images = start_scan(scan_delay, scan_length, scan_loadtime)
            image_download = input((str(len(Found_HD_Images)) + " " + "HD Images Found, continue on downloading? Y/N -> ")) 



    print(len(start_scan(scan_delay, scan_length, scan_loadtime)))
 
start_scrape()

    
    
    