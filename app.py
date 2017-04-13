import os
import sys
import json
import urllib.request
import requests

token = ""

# set info
def setSearchIdsUrl(topico):
    topic = topico
    latitude = "-2.9183953"
    longitude = "-79.0362543"
    radio = "5000" #en metros
    return "https://graph.facebook.com/v2.8/search?q="+topic+"&type=place&center="+latitude+"%2C"+longitude+"&distance="+radio+"&access_token="+token

def setSearchPageUrl(id):
    topic = topico
    latitude = "-2.9183953"
    longitude = "-79.0362543"
    radio = "5000" #en metros
    return "https://graph.facebook.com/v2.8/"+id+"?fields=about%2Clocation%2Coverall_star_rating%2Cratings%7Brating%2Chas_rating%7D%2Cpicture%7Burl%7D%2Cname%2Chours&access_token="+token


# funtion that from a Url outputs jsonData
def getDataUrl(url):
    webURL = urllib.request.urlopen(url)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))



# list the ids of Pages
def listIdPages(data):
    for place in data['data']:
        print(place['id'])

# writes in a .txt file the id of the pages
def writeIdPages(data, fileId):
    i = 1
    # fileId = open('listIds.txt','w')
    for place in data['data']:
        fileId.write(place['id'] +": "+ place['name']+'\n')
        print(str(i) + "  " + place['id'] +": "+ place['name'])
        i = i+ 1

# listIdPages(getDataUrl(setSearchIdsUrl('pizza')))

# writeIdPages(getDataUrl(setSearchIdsUrl('pizza')))


# combine the url getting
# reads the list.txt file, search graph.api for every item in it
# then saves every ID found with the item search in a listIds.txt file
fileList = open('list.txt' , 'r')
data = fileList.read().replace('\n',',').replace(' ', '')
# data[:-1] deletes the last item in the vector
dataVector = data[:-1].split(',')
fileId = open('listIds.txt', 'w')
for topic in dataVector:
    # print (topic)

    url = setSearchIdsUrl(topic)
    dataUrl = getDataUrl(url)
    # listIdPages(dataUrl)
    writeIdPages(dataUrl,fileId)

fileList.close()
fileId.close()
