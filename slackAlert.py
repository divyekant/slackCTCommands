import json
import urllib

import requests


def simpleMessagetoChannel(data, url):
    payload = {
        "response_type": "in_channel",
        "text": data
    }
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)


def simpleMessage(data, url):
    payload = {
        "text": data
    }
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)


def messagewithChart(chart, url):
    payload = {
        "replace_original": True,
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "Trends"
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


def getQuickChartURL(chart):
    return "https://quickchart.io/chart?bkg=white&c=" + urllib.quote(json.dumps(chart))
