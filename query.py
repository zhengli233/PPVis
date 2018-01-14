import numpy as np
import sys
from numpy.fft import fft
from flask import Flask, render_template, request, url_for, jsonify
from flask_cors import CORS, cross_origin
import json
import pandas as pd
import random
import WebScrap as w

app = Flask(__name__)
# read data
df = pd.read_csv('static/simulation_day.csv')
df_pre = pd.read_csv('static/prediction_day.csv')
webscrap = w.ThreadingApp()
df_NN = pd.read_csv('static/NB.csv')


# find the data according to the index of the location
# start from 1

# UTC Jan-01-2017's timestamp is date.fromtimestamp(1483303764.493)
start = 1483228800


def getLocData(index):
    data_new = []
    #x = df['V1'] == X
    #y = df['V2'] == Y
    #data_loc = df[x & y].values.reshape(-1, 1)[3:]
    data_loc = df[df['V0'] == index].values.reshape(-1, 1)[3:]
    print(data_loc)
    for x, d in enumerate(data_loc):
        # x is the day start from 1
        data_new.append({"x": x + 1, "value": d})
    return data_new


@app.route('/', methods=["GET", "POST"])
def index():
 #   data_new = []
 #   data_NN = df_NN.values
 #   for i, d in enumerate(df_NN.values):
  #      data_new.append({"Index": i + 1, "NN": d[4:-1].tolist()})
    # print(data_new)
    return render_template('pvis.html')


@app.route('/data_history', methods=["GET", "POST"])
def data_history():
    index = request.args.get('index')
    print(index)
    # for texst
    prediction = "1"
    index = int(index)
    prediction = int(prediction)
    data = []
    data_pre = []
    data_loc = df[df['V0'] == index].values[0]
    Lat = data_loc[1]
    Lon = data_loc[2]
    Location = data_loc[3]
    for i, d in enumerate(data_loc[4:]):
        data.append([(start + i * 24 * 3600) * 1000, d])
    series = [{"type": 'area', "name": 'Power Price', "data": data}]
    if prediction:
        # for test need to change
        data_loc_pre = df_pre[df_pre['V0'] == index].values[0]
        for i, d in enumerate(data_loc_pre[4:]):
            data_pre.append([(start + i * 24 * 3600) * 1000, d])
        series.append({"type": 'line', "name": 'Predicted Power Price', "data": data_pre})

    return render_template('index.html', Index=index, Lat=Lat, Lon=Lon, Location=Location, series=series)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
    #a = np.array(random.sample(set(range(6000)), 2000))
    #np.save('a.npy', a)
'''
    df = pd.read_csv('static/simulation_month.csv')
    for i in range(12):
        data_new = []
        col = 'V' + str(i + 4)
        d_m = df[["V0", "V1", "V2", "V3", col]].values
        for j, d in enumerate(d_m):
            data_new.append({"index": j + 1, "i": d[1], "j": d[2], "Location": d[3], "value": d[4]})
        f = open('month' + str(i + 1) + '.json', 'w')
        f.write('var datamonth' + str(i + 1) + ' = ')
        json.dump(data_new, f)
'''
# month ==0 means all month, location = "ALL" means all locations

# print(getDayData(356))
# print(getDayData(1))
# print(getLocData(1))
#data_new = []
#data_day = df[["V0", "V1", "V2", "V3", "V4"]].values
# for index, d in enumerate(data_day):
#    # index start from 1
#    data_new.append({"index": index + 1, "i": d[1], "j": d[2], "Location": d[3], "value": d[4]})

#  with open('testdata.js', 'w') as f:
#     json.dump(data_new, f)
