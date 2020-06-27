import json
import time

from botocore.vendored import requests
import urllib


BLACK_COLOUR_HEX = '#000000'
WHITE_COLOUR_HEX = '#ffffff'

def lambda_handler(event, context):

    payload = convertBodytoJSON(event["body"])
    response_url = getURL(payload,"response_url")
    respondtoslack("Fetching data!",response_url)
    respondtoslack("Data Fetched!",response_url)

    return {
        'statusCode': 200
    }

def convertBodytoJSON(body):
    data = {}
    tokens = body.split("&")

    for token in tokens:
        kv = token.split("=")
        data[kv[0]] = kv[1]

    return data


def respondtoslack(data,url):

    payload = {
        "replace_original": True,
        "response_type": "in_channel",
        "text": data
    }

    headers = {
        'Content-Type': "application/json",
    }
    time.sleep(4)
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    print(response.text)


def getimageurlfromdata(data, type, axis):
    import leather
    import os
    import time

    dir = os.path.abspath(os.getcwd())
    fileName = "charts" + str(int(time.time())) + ".svg"
    filePath = dir + "/" + fileName
    leather.theme.default_series_colors = ['#196cf8']
    leather.theme.background_color = WHITE_COLOUR_HEX
    leather.theme.title_color = WHITE_COLOUR_HEX
    leather.theme.axis_title_color = BLACK_COLOUR_HEX
    leather.theme.tick_color = BLACK_COLOUR_HEX
    leather.theme.label_color = BLACK_COLOUR_HEX

    if type == "Line":
        chart = leather.Chart('Line')
        chart.add_line(data, x=x, y=y)
        chart.add_x_axis(None,None,axis["x"])
        chart.add_y_axis(None,None,axis["y"])
        chart.to_svg(fileName)
    elif type == "Histogram":
        chart = leather.Chart('Columns')
        chart.add_columns(data)
        chart.add_x_axis(None,None,axis["x"])
        chart.add_y_axis(None,None,axis["y"])
        chart.to_svg(fileName)

    return filePath


def x(row, index):
    return row['x']

def y(row, index):
    return row['q']['y'][0]

def getURL(payload,key):
    return urllib.unquote(payload["response_url"])