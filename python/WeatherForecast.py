import requests


def WeatherForecast(message):
    returnValue = None
    if "天気" in message:
        data = requests.get(
            "https://weather.tsukumijima.net/api/forecast?city=360010"
        ).json()
        dateLabel = 0
        if "明日" in message:
            dateLabel = 1
        month = data["forecasts"][dateLabel]["date"][5:7]
        if month[:1] == "0":
            month = month[1:]
        day = data["forecasts"][dateLabel]["date"][8:10]
        if day[:1] == "0":
            day = day[1:]
        returnValue = (
            data["forecasts"][dateLabel]["dateLabel"]
            + "（"
            + month
            + "月"
            + day
            + "日）の天気は、"
            + data["forecasts"][dateLabel]["detail"]["weather"]
            + "\n朝の降水確率は"
            + data["forecasts"][dateLabel]["chanceOfRain"]["T06_12"]
            + "\n昼の降水確率は"
            + data["forecasts"][dateLabel]["chanceOfRain"]["T12_18"]
            + "\n夜の降水確率は"
            + data["forecasts"][dateLabel]["chanceOfRain"]["T18_24"]
        )
    return returnValue
