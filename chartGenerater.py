import datetime
import Constants


def generateChart(CTData, cType):
    chart = {}
    if cType.lower() == Constants.trend:
        CTData = runDataCleaner(CTData, Constants.trend)
        chart = generateLineChart(CTData)
    return chart


def generateLineChart(data):
    line_data = []
    value_data = []
    for key in sorted(data):
        line_data.append(key)
        value_data.append(data[key])
    options = {
        "scales": {
            "xAxes": [{
                "gridLines": {
                    "color": "rgba(0, 0, 0, 0)"
                },
                "ticks": {
                    "fontSize": 10
                }

            }],
            "yAxes": [{
                "scaleLabel": {
                    "display": "true",
                    "labelString": 'Event Count'
                },
                "ticks": {
                    "fontSize": 10
                }
            }]
        }
    }
    chart = {
        "type": 'line',
        "data": {
            "labels": line_data,
            "datasets": [{
                "label": "Event Trend",
                "data": value_data
            }]
        },
        "options": options
    }

    chart = setChartDataSetStyle(chart, Constants.trend)

    return chart


def setChartDataSetStyle(chart, cType):
    if cType.lower() == Constants.trend:
        style = Constants.chart_trend_style
        for key in style:
            chart["data"]["datasets"][0][key] = style[key]

    return chart


def runDataCleaner(data, cType):
    cleanData = {}
    if cType.lower() == Constants.trend:
        sortedDates = sortDates(data)
        for date in sortedDates:
            cleanData[date] = data[date]
    return cleanData


def sortDates(data):
    dates = []

    for date in data:
        dates.append(date)

    # Sort the list in ascending order of dates
    dates.sort(key=lambda date: datetime.datetime.strptime(date, '%Y%m%d'))

    return dates
