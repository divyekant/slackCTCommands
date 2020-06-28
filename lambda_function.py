import json
import time

import trendsAPI
from botocore.vendored import requests
import urllib
import requests
import createChart
import screenshot

BLACK_COLOUR_HEX = '#000000'
WHITE_COLOUR_HEX = '#ffffff'


def lambda_handler(event, context):
    payload = convertBodytoJSON(event["body"])
    response_url = getURL(payload, "response_url")

    respondtoslack("Fetching data!", response_url)

    command = readCommand(getCommand(payload))

    CTData = trendsAPI.runTrendsAPI(command)

    respondtoslack(json.dumps(CTData), response_url)

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


def respondtoslackwithChart(data, url):
    payload = {
        "replace_original": True,
        "response_type": "in_channel",
        "text": data
    }
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)


def getQuickChartURL(data):
    return "https://quickchart.io/chart?bkg=white&c=%7B%0A%20%20type%3A%20%27bar%27%2C%0A%20%20data%3A%20%7B%0A%20%20%20%20labels%3A%20%5B%27Week%201%27%2C%20%27Week%202%27%2C%20%27Week%203%27%2C%20%27Week%204%27%5D%2C%0A%20%20%20%20datasets%3A%20%5B%7B%0A%20%20%20%20%20%20label%3A%20%27Retweets%27%2C%0A%20%20%20%20%20%20data%3A%20%5B12%2C%205%2C%2040%2C%205%5D%0A%20%20%20%20%7D%2C%20%7B%0A%20%20%20%20%20%20label%3A%20%27Likes%27%2C%0A%20%20%20%20%20%20data%3A%20%5B80%2C%2042%2C%20215%2C%2030%5D%0A%20%20%20%20%7D%5D%0A%20%20%7D%0A%7D"


def respondtoslack(data, url):
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
                "image_url": getQuickChartURL(data),
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

def formatLineData(CTData):
    line_data = []
    for key in CTData:
        line_data.append(CTData[key])
