import requests
from bs4 import BeautifulSoup

URL_ENDPOINT = "https://pizza-site-six.vercel.app"

res = requests.get(URL_ENDPOINT + "/recipes")
soup = BeautifulSoup(res.text, "html.parser")

anchor_list = soup.select("a[href^='/recipes/']")
for anchor in anchor_list:
    res = requests.get(URL_ENDPOINT+anchor["href"])
    soup = BeautifulSoup(res.text, "html.parser")

    #Name
    print(soup.h1.text)
    recipe_title = soup.h1.text

    #Image
    print(soup.img["src"])
    recipe_img = soup.img["src"]

ing_header = soup.find("h2", attrs={"class": "recipe-title"})

if ing_header:
    sibling = ing_header.find_next_sibling()
    if sibling:
        ingredients = sibling.find_all("li")
        for ing in ingredients:
            print(ing.text)
    else:
        print("No sibling found for ingredient header.")
else:
    print("No ingredient header found.")