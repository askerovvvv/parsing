# python3 -m venv venv
# source venv/bin/activate        

# pip install requests
# pip install beautifulsoup4
# pip installlxml


import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url).text
    return response                                                         



def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    catalog = soup.find("div", class_ = "listing search-page x-3")
    print(catalog)
    
    # title = mobiles[0].find("a", class_ = "product-title").text
    # img = mobiles[0].find("img", class_ = "ty-pict").get("data-ssrc")

#     for mobile in mobiles:
#         print(mobile)
#         try:
#             title = mobile.find("a", class_ = "product-title").text
#         except:
#             title = ""
#         try:
#             img = mobile.find("img", class_ = "ty-pict").get("data-ssrc")
#         except:
#             img = ""
#         data = {
#             "title":title,
#             "image": img,
#         }

#         write_csv(data)



# def write_csv(data):
#     with open("mobiles.csv", "a") as file:
#         writer = csv.writer(file,delimiter=",")
#         writer.writerow((data["title"],data["image"]))
        





def main():
    # url = "https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/smartfony-s-podderzhkoy-4g-ru/" 
    # html = get_html(url)
    # get_data(html)

    # for i in range(1,1000):
    url = f"https://www.mashina.kg/new/search"
    html = get_html(url)
    data = get_data(html)
    #     if data == False:
    #         break
    #     print(f"Парсинг {i} завершен!")
main()






