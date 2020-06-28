import Constants
import datetime

import errorHandling


def generateObject(commandObject):
    CTAPIObject = {}
    commandObjectKeys = commandObject.keys()

    hasTrendsAPIKeysCheck(commandObjectKeys)

    if commandObject[Constants.command_type].lower() == Constants.trend:
        for i in range(0, len(commandObjectKeys)):
            if commandObjectKeys[i] == Constants.days:
                dates = getDatesforCTAPI(commandObject[commandObjectKeys[i]])
                CTAPIObject[Constants.to_date] = dates[0]
                CTAPIObject[Constants.from_date] = dates[1]
            elif commandObject[commandObjectKeys[i]] is None or commandObject[commandObjectKeys[i]] == "":
                continue
            else:
                CTAPIObject[commandObjectKeys[i]] = commandObject[commandObjectKeys[i]]
    return CTAPIObject


def getDate(diff=0):
    today = datetime.datetime.now()
    DD = datetime.timedelta(days=diff)
    earlier = today - DD
    return earlier.date()


def getDatesforCTAPI(days):
    dates = []
    today = getDate()
    dates.append(today.strftime("%Y%m%d"))
    if days is None or days == "":
        dates.append(getDate(Constants.default_lookback_days).strftime("%Y%m%d"))
    else:
        dates.append(getDate(int(days)).strftime("%Y%m%d"))
    return dates


def hasTrendsAPIKeysCheck(keys):
    check = all(item in keys for item in Constants.trendsAPI_mandatory_keys)
    if not check:
        errorHandling.handleError(Constants.error_API_keys_mismatch)
