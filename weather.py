
import requests

def get_weather_picture(weather_symbol):
    if weather_symbol == 1: #Clear Sky
        picture = "https://www.smhi.se/polopoly_fs/1.12110.1490013119!/image/1.png_gen/derivatives/Original_259px/image/1.png"
    elif weather_symbol == 2: #Nearly Clear Sky
        picture = "https://www.smhi.se/polopoly_fs/1.27958.1490013412!/image/2.png_gen/derivatives/Original_259px/image/2.png"
    elif weather_symbol == 3: #Variable cloudiness
        picture = "https://www.smhi.se/polopoly_fs/1.12116.1490012816!/image/3.png_gen/derivatives/Original_259px/image/3.png"
    elif weather_symbol == 4: #Halfclear sky
        picture = "https://www.smhi.se/polopoly_fs/1.12114.1490013334!/image/4.png_gen/derivatives/Original_259px/image/4.png"
    elif weather_symbol == 5: #Cloudy sky
        picture = "https://www.smhi.se/polopoly_fs/1.12115.1490011576!/image/5.png_gen/derivatives/Original_259px/image/5.png"
    elif weather_symbol == 6: #Overcast
        picture = "https://www.smhi.se/polopoly_fs/1.12112.1490013826!/image/6.png_gen/derivatives/Original_259px/image/6.png"
    elif weather_symbol == 7: #Fog
        picture = "https://www.smhi.se/polopoly_fs/1.12123.1490013711!/image/7.png_gen/derivatives/Original_259px/image/7.png"
    elif weather_symbol == 8: #Rain showers
        picture = "https://www.smhi.se/polopoly_fs/1.12113.1490012836!/image/8.png_gen/derivatives/Original_259px/image/8.png"
    elif weather_symbol == 9: #Thunderstorm
        picture = "https://www.smhi.se/polopoly_fs/1.12121.1490013081!/image/9.png_gen/derivatives/Original_259px/image/9.png"
    elif weather_symbol == 10: #Light sleet
        picture = "https://www.smhi.se/polopoly_fs/1.12117.1490011557!/image/10.png_gen/derivatives/Original_259px/image/10.png"
    elif weather_symbol == 11: #Snow showers
        picture = "https://www.smhi.se/polopoly_fs/1.12119.1490013064!/image/11.png_gen/derivatives/Original_259px/image/11.png"
    elif weather_symbol == 12: #Rain
        picture = "https://www.smhi.se/polopoly_fs/1.12111.1490013845!/image/12.png_gen/derivatives/Original_259px/image/12.png"
    elif weather_symbol == 13: #Thunder
        picture = "https://www.smhi.se/polopoly_fs/1.12122.1490012556!/image/13.png_gen/derivatives/Original_259px/image/13.png"
    elif weather_symbol == 14: #Sleet
        picture = "https://www.smhi.se/polopoly_fs/1.12118.1490013710!/image/14.png_gen/derivatives/Original_259px/image/14.png"
    elif weather_symbol == 15: #Snowfall
        picture = "https://www.smhi.se/polopoly_fs/1.12120.1490013174!/image/15.png_gen/derivatives/Original_259px/image/15.png"
    else:
        print("nope it does not work")

    return picture
