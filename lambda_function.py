import CTAPIConverter
import Constants
import chartGenerater
import errorHandling
import trendsAPI
import urllib
import slackAlert
import commandInterpreter


def lambda_handler(event, context):
    payload = convertBodytoJSON(event["body"])

    response_url = getURL(payload, "response_url")
    errorHandling.setErrorURL(response_url)

    slackAlert.simpleMessage("Fetching data!", response_url)

    command = getCommand(payload)

    commandObject = commandInterpreter.getCommandKeys(command)

    CTAPIObject = CTAPIConverter.generateObject(commandObject)

    CTData = trendsAPI.fetchData(CTAPIObject)

    chart = chartGenerater.generateChart(CTData,commandObject[Constants.command_type])

    slackAlert.messagewithChart(chart, response_url)

    return {
        'statusCode': 200
    }


def getCommand(data):
    t = urllib.unquote(data["text"]).replace("+", " ")
    return t


def convertBodytoJSON(body):
    data = {}
    tokens = body.split("&")

    for token in tokens:
        kv = token.split("=")
        data[kv[0]] = kv[1]

    return data


def getURL(payload, key):
    return urllib.unquote(payload[key])
