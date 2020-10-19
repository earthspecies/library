from seleniumwire import webdriver 
import pandas as pd
from progressbar import ProgressBar
import requests
import os

#url is a 'best of' cuts from the watkins database
#download path is where you want the metadata/sound data to be downloaded
url = "https://whoicf2.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BA2A"
download_path = "/home/oliver/Desktop/watkins_data/sperm_whale/"

try:
    os.mkdir(download_path)
except FileExistsError:
    pass #if the path already exists, do nothing

"""
This script is for downloading data from the Watkins database, specifically from
the 'best of' cuts. A url of the subpage in the 'best of' cuts, and a download path 
are given. For each soundfile, there is useful metadata, so we have to download both. 

First we scrape the page looking for the urls of the wav files and metadata, then 
the functions 'download_metadata_csv' and 'download_wav' are used to download the
metadata and sound files respectively from a list of urls. 
"""

#load driver with preferences and open url
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : download_path}
chromeOptions.add_experimental_option("prefs",prefs)
swdriver = webdriver.Chrome(chrome_options=chromeOptions)
swdriver.get(url)

#finding where the table lives and getting a list of the elements
table_body_elements = swdriver.find_elements_by_xpath("/html/body/div[4]/div/div/table/tbody/tr")
print('Found {} sound file links on this page... \n'.format(len(table_body_elements)-1))
print("Scraping for URL pairs...")
progress = ProgressBar(len(table_body_elements)-1, fmt = ProgressBar.FULL)
sound_metadata_url_pairs = []

#grabbing the urls for each sound and metadata occuring on the table in the page
for row in table_body_elements[1:]:
    progress.current += 1
    progress.__call__()
    
    #grabbing the href for the sound file
    sound_el = row.find_elements_by_xpath(".//td[4]/a")[0]
    #print("Found sound data at: {}".format(download_el.get_attribute("href")))
    temp_sound_url = str(sound_el.get_attribute("href"))
    
    #each file in the watkins db has a unique identifyer, here's one way to grab it:
    temp_file_id = str(temp_sound_url).split("/")[-1].split(".")[0]
    
    #grabbing the href for the metadata for the .wav file (has the same format for all, with replaced id)
    temp_metadata_url = "https://cis.whoi.edu/science/B/whalesounds/metaData.cfm?RN={}".format(temp_file_id)
    
    sound_metadata_url_pairs.append([temp_sound_url, temp_metadata_url])

progress.done()
print('\nDone!')

def download_metadata_csv(url, driver):
    #Opens the url with the driver and looks for a table
    #Grabs the outerhtml of the metadata table, and returns a df if the format is good

    driver.get(url)
    tbl = swdriver.find_element_by_xpath("/html/body/table[2]").get_attribute('outerHTML')
    fname = str(url).split("=")[-1]+"metadata.csv"
    metadata_df = None
    
    try:
        metadata_df = pd.read_html(tbl)[0]
    except:
        raise Exception("Pandas couldn't read the HTML!")
    
    metadata_df.to_csv(download_path+fname)

def download_wav(url, driver):
    #Opens the url with the driver, and downloads the file via requests

    fname = str(url).split("/")[-1]
    r = requests.get(url, allow_redirects = True)
    with open(download_path+fname, 'wb') as f:
        f.write(r.content)


print("\nDownloading sound and metadata...")
progress = ProgressBar(len(sound_metadata_url_pairs), fmt = ProgressBar.FULL)

for x in sound_metadata_url_pairs:
    progress.current += 1
    progress.__call__()
    
    wav_url, metadata_url = x[0], x[1]
    try:
        download_wav(wav_url, swdriver)
        download_metadata_csv(metadata_url, swdriver)
    except:
        print("Failed at: {}".format(wav_url))
        pass #if either of these fails, then we shouldn't download the other

print("\nDone!")
    
    
swdriver.close()



