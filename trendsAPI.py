import requests
import time


def queryCall(eventName,accid,accpc,dfrom,dto,trendType,uniqueFlag):

    url = "https://api.clevertap.com/1/counts/trends.json"

    payload = "{\"event_name\":\"%s\",\"from\":%s,\"to\":%s,\"unique\":%s,\"groups\":{\"foo\":{\"trend_type\":\"%s\"}}}" % (eventName,dfrom,dto,uniqueFlag.lower(),trendType.lower())
    headers = {
        'X-CleverTap-Account-Id': "%s" % accid,
        'X-CleverTap-Passcode': "%s" % accpc,
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "687db015-6665-4a5b-9706-69f78b7a03e5"
    }

    print "Making the Trends Api Call for Event: " + eventName

    response = requests.request("POST", url, data=payload, headers=headers)

    if response.status_code != 200:
        return 0
    else:
        res = response.json()
        if res["status"] == "partial":
            reqid = res["req_id"]
            return reqid
        else:
            return 0

def partialCall(reqid,accid,accpc):
    url = "https://api.clevertap.com/1/counts/trends.json"

    querystring = {"req_id": "%s" % reqid}

    payload = ""
    headers = {
        'X-CleverTap-Account-Id':  "%s" % accid,
        'X-CleverTap-Passcode': "%s" % accpc,
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "21b84377-9fc4-4709-9836-65f13452160d"
    }

    print "Making the Trends Api Request ID Call"

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)


    if response.status_code != 200:
        return 0
    else:
        res = response.json()
        if res["status"]=="partial":
            return 0
        return res

def runTrendsAPI(command):
    eventName = getEventName(command)
    uniqueFlag = getUniqueFlag(command)
    accid = getAccountID(command)
    accpcode = getAccountPasscode(command)
    dfrom = getFromDate(command)
    dto = getToDate(command)
    trendType = getTrendType(command)


    if uniqueFlag == "E":
        uniqueFlag = "False"
    else:
        uniqueFlag = "True"

    ftFlag = True
    print "Doing for Event: " + eventName

    #  get req id
    reqID = queryCall(eventName,accid,accpcode,dfrom,dto,trendType,uniqueFlag)

    while reqID == 0:
        time.sleep(5)
        reqID = queryCall(eventName, accid, accpcode,dfrom,dto,trendType,uniqueFlag)


    retryFlag = True
    retryCount = 0


    while retryFlag and retryCount <=10:
        res = partialCall(reqID,accid,accpcode)
        if res == 0:
            retryFlag = True
            time.sleep(5)
            retryCount = retryCount + 1
        else:
            retryFlag = False


    if retryCount <=10:
        if res["status"] == "success":
            data = res["foo"]
        else:
            print "Non - Success Status returned "
            print res
    else:
        print "Too Many retries for Event: " + eventName

    print "Done for Event: " + eventName
    return data



def getEventName(data):
    return data["eName"]


def getFromDate(data):
    return data["fDate"]


def getToDate(data):
    return data["tDate"]


def getAccountID(data):
    return data["accid"]


def getAccountPasscode(data):
    return data["accpcode"]


def getTrendType(data):
    return data["tType"]


def getUniqueFlag(data):
    return data["uFlag"]
