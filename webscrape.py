import webbrowser
import requests
import codecs
import threading
import datetime

# Multi-threaded mass html download

test_mode = True

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
        print("Attempt download " + each_url)
        if not test_mode:
            response = requests.get(each_url)
            if (response.status_code == 200):
                file_name = str(datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')) + each_url[8:].replace("/", "-")
                file = codecs.open(file_name + ".html", "w", encoding="utf8")
                file.write(response.text)
                file.close()
                print("Response okay", response.text[:100])
            else:
                print("Response error", each_url)

download_url_master_list_multithread(url_list_master)


#webbrowser.open()

#response = requests.get(url)
#print(type(response))
#print(len(response.text))

#file = open("test.html", "w")
#file.write(response.text)
#file.close()
