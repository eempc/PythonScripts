import requests
import codecs
import threading
import datetime
import os

# Multi-threaded mass html text download (no images)

test_mode = False

# Make sublist 0
url_sublist_0 = []
url_sublist_0.append("https://en.wikipedia.org/wiki/Main_Page")

# Make sublist 1
url_sublist_1  = []
url_sublist_1.append("https://www.google.com")

# Make master list of the above sublists
url_list_master = []
url_list_master.append(url_sublist_0)
url_list_master.append(url_sublist_1)

def download_url_master_list_multithread(url_list_of_lists):
    for sublist in url_list_of_lists:
        thread = threading.Thread(target=download_url_list, args=[sublist])
        thread.start()

def download_url_list(url_list):
    for each_url in url_list:
        # Get a name for the file
        file_name = str(datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')) + " " + each_url[8:].replace("/", "-") + ".html"
        relative_path = os.path.join("Webscrape", file_name)

        print("Attempt download " + each_url + " to " + relative_path)
        if not test_mode:
            response = requests.get(each_url)
            if (response.status_code == 200):
                # Open the new file ready to be written with encoding to utf8
                file = codecs.open(relative_path, "w", encoding="utf8")
                file.write(response.text)

                # Split the file up in case it is huge (non-utf, non-codecs)
                #file = open(file_name, "w")
                #for chunk in response.iter_content(100000):
                    #file.write(chunk)

                file.close()
                print("Response okay", response.text[:100])
            else:
                print("Response error", each_url)

download_url_master_list_multithread(url_list_master)
