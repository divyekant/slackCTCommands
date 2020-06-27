import json
import trendsAPI
from botocore.vendored import requests
import urllib

BLACK_COLOUR_HEX = '#000000'
WHITE_COLOUR_HEX = '#ffffff'


def lambda_handler(event, context):
    payload = convertBodytoJSON(event["body"])
    response_url = getURL(payload, "response_url")

    respondtoslack("Fetching data!", response_url)

    command = readCommand(getCommand(payload))

    CTData = trendsAPI.runTrendsAPI(command)
    line_data = convertCTDatatoLineData(CTData)

    print getimageurlfromdata(line_data, "Line")

    respondtoslack("Data Fetched!", response_url)

    return {
        'statusCode': 200
    }


def getCommand(data):
    t = urllib.unquote(data["text"]).replace("+"," ")
    return data["text"]


def readCommand(text):
    command = {}
    tokens = text.split("|")
    command["accid"] = tokens[0]
    command["accpcode"] = tokens[1]
    command["eName"] = tokens[2]
    command["fDate"] = tokens[3]
    command["tDate"] = tokens[4]
    command["tType"] = tokens[5]
    command["uFlag"] = tokens[6]
    return command


def convertCTDatatoLineData(CTData):
    line_data = []
    for key in CTData:
        row = {}
        row["x"] = key
        row["q"]["y"] = CTData[key]
        line_data.append(row)

    return line_data


def convertBodytoJSON(body):
    data = {}
    tokens = body.split("&")

    for token in tokens:
        kv = token.split("=")
        data[kv[0]] = kv[1]

    return data


def respondtoslack(data, url):
    payload = {
        "replace_original": True,
        "response_type": "in_channel",
        "text": data
    }
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)


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
        chart.add_x_axis(None, None, axis["x"])
        chart.add_y_axis(None, None, axis["y"])
        chart.to_svg(fileName)
    elif type == "Histogram":
        chart = leather.Chart('Columns')
        chart.add_columns(data)
        chart.add_x_axis(None, None, axis["x"])
        chart.add_y_axis(None, None, axis["y"])
        chart.to_svg(fileName)

    return filePath


def x(row, index):
    return row['x']


def y(row, index):
    return row['q']['y'][0]


def getURL(payload, key):
    return urllib.unquote(payload["response_url"])
