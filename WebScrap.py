import requests
import json
import threading
import time
import datetime

page = requests.get('http://wwwmobile.caiso.com/Web.Service.Chart/api/v3/ChartService/PriceContourMap1')

data = page.text.replace("\"", "")
data = data.replace("{", "\n")
data = data.replace("}", "\n")
data = data[data.index("l:3,m:[") + len("l:3,m:["):data.index("],d:")]
file = open("map.rtf", "w")
file.write(data)
file.close()


def generateJsonData():
    index = 1
    start = 0
    jsonData = []
    while (index <= 6126):
        try:
            tempDict = {}
            tempDict["index"] = index
            start = data[start:len(data) - 1].index(",c:[") + len(",c:[") + start
            end = data[start:len(data) - 1].index("],n:") + start
            position = data[start:end]
            i, j = position.split(",")
            tempDict["i"] = float(i)
            tempDict["j"] = float(j)
            start = end
            start = data[start:len(data) - 1].index(",a:") + len(",a:") + start
            end = data[start:len(data) - 1].index(",dk:") + start
            location = data[start:end]
            tempDict["Location"] = location
            start = end
            start = data[start:len(data) - 1].index(",dp:") + len(",dg:") + start
            end = data[start:len(data) - 1].index(",dg:") + start
            value = data[start:end]
            tempDict["value"] = float(value)
            start = end
            index += 1
            jsonData.append(tempDict)
        except ValueError:
            print("Value Error")
    fileName = str(datetime.datetime.now())
    fileName = fileName.replace(".", "_")
    fileName = fileName.replace(":", "_")
    fileName = fileName.replace(" ", "_")
    fileName = fileName.replace("-", "_")
    fileName += ".json"
    # print(fileName)
    file = open("static/json/currentData.json", "w")
    file.write('var data0' + ' = ')
    json.dump(jsonData, file)
    file.close()
    file = open("static/json/" + fileName, "w")
    file.write('var data' + ' = ')
    json.dump(jsonData, file)
    file.close()


class ThreadingApp(object):

    def __init__(self, interval=1):

        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            generateJsonData()
            print("new json file generated!")
            time.sleep(self.interval * 3600)
