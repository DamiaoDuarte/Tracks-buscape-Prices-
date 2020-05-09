import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = "https://www.buscape.com.br/celular/smartphone-apple-iphone-11-64gb-ios?_lc=88&q=iphone%2011"

#headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}

def check_price():
    #response = requests.get(URL, headers=headers)
    response = requests.get(URL)

    soup = BeautifulSoup(response.content, "html.parser")


    title = soup.findAll("h1", {"class":"product-name"})
    title = title[0].text
    price = soup.findAll("a", {"class":"price-label"})
    #price = float(price [0:5])
    #converted_price = [float(item) for item in price]
    price = price[0].text.strip()
    send_mail()

    #if (price < '1.700'):
        #send_mail()

    #print(title.strip())
    #print(price)

    #if(price > '1.700'):
        #send_mail()    

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("your email", "password")

    subject = "Price fell down!"
    body = "https://www.buscape.com.br/celular/smartphone-apple-iphone-11-64gb-ios?_lc=88&q=iphone%2011"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "Email from XXXXX",
        "Email to XXXXX",
        msg
    )
    print(">>>>> HEY.. EMAIL HAS BEEN SENT!<<<<<<")

    server.quit()

while(True):
    check_price()
    time.sleep(300)
