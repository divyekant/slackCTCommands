import json
import time

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
    chart = generateLineChart(CTData)

    respondtoslackwithChart(chart, response_url)

    return {
        'statusCode': 200
    }


def getCommand(data):
    t = urllib.unquote(data["text"]).replace("+"," ")
    return t


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

def generateLineChart(data):

    line_data = []
    value_data = []
    for key in data:
        line_data.append(key)
        value_data.append(data[key])

    chart = {
        "type": 'line',
        "data": {
            "labels": line_data,
            "datasets": [{
                "label": 'My Second dataset',
                "data":value_data
            }]

        }
    }
    return chart

def getQuickChartURL(chart):
    return "https://quickchart.io/chart?bkg=white&c=" + urllib.quote(json.dumps(chart))


def respondtoslackwithChart(chart, url):
    payload = {
        "replace_original": True,
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "Latest data"
                },
                "block_id": "quickchart-image",
                "image_url": getQuickChartURL(chart),
                "alt_text": "Chart showing latest data"
            }
        ]
    }

    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

def getURL(payload,key):
    return urllib.unquote(payload[key])

def getfileName():
    return "page" + str(int(time.time()))
