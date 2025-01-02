import requests
import random


API = "https://api.dicebear.com/7.x/"


STYLES = [
    "adventurer",
    "avataaars",
    "bottts",
    "icons",
    "identicon",
    "pixel-art",
    "shapes",
    "thumbs",
]


def get_avatar():
    style = random.choice(STYLES)
    url = API + style + "/svg"
    response = requests.get(url)
    if response.status_code == 200:
        svg_content = response.content.decode('utf-8')
        return svg_content
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")
        return None
    

def get_user_data(new_user): 
    return {
        "email" :new_user.email,
        "first_name" : new_user.first_name,
        "last_name" : new_user.last_name,
        "image" : new_user.user_profile_image
    }
    