from dotenv import load_dotenv
from flask import Flask
from flask import render_template
from datetime import datetime
import requests
import json
import os

load_dotenv()

app = Flask(__name__, template_folder='templates')

API_KEY = os.getenv("API_KEY", None)

@app.template_filter('datetime')
def date(timestamp):
    """
    Returns the date formatted string for the given timestamp.
    """
    return datetime.strptime(timestamp, '%Y %m %d %H:%M:%S')

data = [
        {
            "source": {
                "id": "None",
                "name": "Lifehacker.com"
            },
            "author": "Allie Chanthorn Reinmann",
            "title": "Embrace These Cold Soups All Summer Long",
            "description": "It’s that special time of year when 10 a.m. greets you with a temperature of 84°F and 79% humidity, at least that’s the case here in New York City. There’s nothing in the world that could make me put a steaming hot breakfast into this already sweaty, still-in…",
            "url": "https://lifehacker.com/embrace-these-cold-soups-all-summer-long-1850606372",
            "urlToImage": "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/fa057f5bb2cfbc38a7542e55bd072942.jpg",
            "publishedAt": "2023-07-05T19:00:00Z",
            "content": "Its that special time of year when 10 a.m. greets you with a temperature of 84°F and 79% humidity, at least thats the case here in New York City. Theres nothing in the world that could make me put a … [+2783 chars]"
        },
        {
            "source": {
                "id": "the-verge",
                "name": "The Verge"
            },
            "author": "Ash Parrish",
            "title": "All the news from Ubisoft Forward 2023",
            "description": "Ubisoft Forward 2023 is set to feature news and updates on all of Ubisoft’s popular franchises, including Prince of Persia, The Division, and of course, Assassin’s Creed.",
            "url": "https://www.theverge.com/2023/6/12/23757993/ubisoft-forward-2023-news-annoucements-trailers",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/0qKnWNzFgBSxB_Zw3QWZ1Ij2inY=/0x0:1000x563/1200x628/filters:focal(500x282:501x283)/cdn.vox-cdn.com/uploads/chorus_asset/file/24720797/6520421_bd.jpeg",
            "publishedAt": "2023-06-12T16:00:00Z",
            "content": "Filed under:\r\nByAsh Parrish, a reporter who has covered the business, culture, and communities of video games for seven years. Previously, she worked at Kotaku. \r\nUbisofts Summer Game Fest presentati… [+1764 chars]"
        },
        {
            "source": {
                "id": "engadget",
                "name": "Engadget"
            },
            "author": "Lawrence Bonk",
            "title": "Amazon’s ‘Hey Disney!’ experience comes to all Echo devices",
            "description": "Amazon and Disney have partnered to create an interactive experience that combines Alexa’s voice assistant features with Disney’s robust stable of characters. The appropriately-named “Hey Disney!” is now available on any Echo device and represents the very fi…",
            "url": "https://www.engadget.com/amazons-hey-disney-experience-comes-to-all-echo-devices-130009651.html",
            "urlToImage": "https://s.yimg.com/uu/api/res/1.2/9WG42lai7HbEg.00roL.mw--~B/Zmk9ZmlsbDtoPTYzMDtweW9mZj0wO3c9MTIwMDthcHBpZD15dGFjaHlvbg--/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2023-05/f41ea8d0-f985-11ed-be2a-9040aab9e9dc.cf.jpg",
            "publishedAt": "2023-06-15T13:00:09Z",
            "content": "Amazon and Disney have partnered to create an interactive experience that combines Alexas voice assistant features with Disneys robust stable of characters. The appropriately-named Hey Disney! is now… [+1493 chars]"
        },
        {
            "source": {
                "id": "wired",
                "name": "Wired"
            },
            "author": "Dell Cameron",
            "title": "The US Is Openly Stockpiling Dirt on All Its Citizens",
            "description": "A newly declassified report from the Office of the Director of National Intelligence reveals the federal government is buying troves of data about Americans.",
            "url": "https://www.wired.com/story/odni-commercially-available-information-report/",
            "urlToImage": "https://media.wired.com/photos/64874ce9f2de86183cf5b4ae/191:100/w_1280,c_limit/stockpile_data_sec_GettyImages-1413768537.jpg",
            "publishedAt": "2023-06-12T19:23:56Z",
            "content": "The United States government has been secretly amassing a large amount of sensitive and intimate information on its own citizens, a group of senior advisors informed Avril Haines, the director of nat… [+3418 chars]"
        },
        {
            "source": {
                "id": "the-verge",
                "name": "The Verge"
            },
            "author": "David Pierce",
            "title": "So where are we all supposed to go now?",
            "description": "As apps like Reddit and Twitter die out, and Instagram and Facebook and TikTok turn to entertainment, it’s the end of a social era on the web. And we’re left wondering if there will be anywhere left for us all to hang out.",
            "url": "https://www.theverge.com/2023/7/3/23782607/social-web-public-apps-end-reddit-twitter-mastodon",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/nqgJRJCkAkPue64Fr7vB85U2wDE=/0x0:4288x2848/1200x628/filters:focal(2144x1424:2145x1425)/cdn.vox-cdn.com/uploads/chorus_asset/file/24767998/868706204.jpg",
            "publishedAt": "2023-07-03T16:00:00Z",
            "content": "So where are we all supposed to go now?\r\nSo where are we all supposed to go now?\r\n / Its the end of a social era on the web. Thats probably a good thing. But I already miss the places that felt like … [+8995 chars]"
        },
        {
            "source": {
                "id": "the-verge",
                "name": "The Verge"
            },
            "author": "Andrew Webster",
            "title": "Netflix Tudum 2023: all the biggest news and trailers",
            "description": "Netflix’s Tudum event takes place at 1:30PM PT / 4:30PM ET, and the livestream will feature updates and trailers for The Witcher, One Piece, Avatar: The Last Airbender, Bridgerton, Stranger Things, and more.",
            "url": "https://www.theverge.com/2023/6/17/23761280/netflix-tudum-2023-trailers-news-announcements",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/BPI_giwPrI6YTUIG9xIy1dDTxAM=/0x0:2040x1360/1200x628/filters:focal(1020x680:1021x681)/cdn.vox-cdn.com/uploads/chorus_asset/file/23951363/STK072_VRG_Illo_N_Barclay_2_netflix.jpg",
            "publishedAt": "2023-06-17T19:30:00Z",
            "content": "Filed under:\r\nByAndrew Webster, an entertainment editor covering streaming, virtual worlds, and every single Pokémon video game. Andrew joined The Verge in 2012, writing over 4,000 stories.\r\nIn whats… [+2078 chars]"
        },
        {
            "source": {
                "id": "engadget",
                "name": "Engadget"
            },
            "author": "Daniel Cooper",
            "title": "The Morning After: All the cool things Netflix showed off over the weekend",
            "description": "Tudum, Netflix’s in-house mix of Comic Con and shareholder presentation, took place this weekend. The company used the moment to tease plenty of forthcoming projects, including its live-action remakes of One Piece\r\n and \r\"nAvatar: The Last Airbender\r\n. It also…",
            "url": "https://www.engadget.com/the-morning-after-all-the-cool-things-netflix-showed-off-over-the-weekend-111523740.html",
            "urlToImage": "https://s.yimg.com/uu/api/res/1.2/ifyABJHJYXxs3j7IHAC.hw--~B/Zmk9ZmlsbDtoPTYzMDtweW9mZj0wO3c9MTIwMDthcHBpZD15dGFjaHlvbg--/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2023-06/4d47f060-0e8a-11ee-9dff-cd2fc483c235.cf.jpg",
            "publishedAt": "2023-06-19T11:15:23Z",
            "content": "Tudum, Netflixs in-house mix of Comic Con and shareholder presentation, took place this weekend. The company used the moment to tease plenty of forthcoming projects, including its live-action remakes… [+3829 chars]"
        },
        {
            "source": {
                "id": "engadget",
                "name": "Engadget"
            },
            "author": "Igor Bonifacic",
            "title": "Netflix shares teaser for World War II drama ‘All The Light We Cannot See’",
            "description": "Between all the trailers Netflix shared yesterday during its Tudum event for properties like One Piece\r\n and 3 Body Problem\r\n, you may have missed some of the more grounded dramas the company was promoting at the same time. One of those was its upcoming adapt…",
            "url": "https://www.engadget.com/netflix-shares-teaser-for-world-war-ii-drama-all-the-light-we-cannot-see-211706050.html",
            "urlToImage": "https://s.yimg.com/uu/api/res/1.2/AWrrPSW.sBi7XqAhVLQzqg--~B/Zmk9ZmlsbDtoPTYzMDtweW9mZj0wO3c9MTIwMDthcHBpZD15dGFjaHlvbg--/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2023-06/4d5b0d30-0e1c-11ee-9d19-9d12c18ad20c.cf.jpg",
            "publishedAt": "2023-06-18T21:17:06Z",
            "content": "Between all the trailers Netflix shared yesterday during its Tudum event for properties like One Piece\r\n and 3 Body Problem\r\n, you may have missed some of the more grounded dramas the company was pro… [+1475 chars]"
        }
    ]


@app.route("/")
def index():
    # url = f"https://newsapi.org/v2/everything?q=all&apiKey={API_KEY}"
    # url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={Api_key}"
    # response = requests.get(url)
    # data = response.json()
    # news_article = data["articles"]
    # article = [article for article in news_article]
    article = data
    return render_template('index.html', article=article)


if __name__ == '__main__':
    app.run()


