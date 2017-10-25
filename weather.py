
import requests

def get_weather_picture(weather_symbol):
    if weather_symbol == 1: #Clear Sky
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/1.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 2: #Nearly Clear Sky
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/2.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 3: #Variable cloudiness
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/3.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 4: #Halfclear sky
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/4.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 5: #Cloudy sky
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/5.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 6: #Overcast
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/6.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 7: #Fog
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/7.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 8: #Rain showers
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/8.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 9: #Thunderstorm
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/9.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 10: #Light sleet
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/10.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 11: #Snow showers
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/11.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 12: #Rain
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/12.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 13: #Thunder
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/13.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 14: #Sleet
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/14.png?v=1506930628138&proxy=wpt-abc"
    elif weather_symbol == 15: #Snowfall
        return "https://www.smhi.se/startpage/images/WPT-icons/weathersymbols/80x60/day/15.png?v=1506930628138&proxy=wpt-abc"
    else:
        print("nope it does not work")
