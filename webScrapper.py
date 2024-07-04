from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

#Get Title Of Product Of Flipkart
def getTitleFlipkart(soup): 
    try:
        title = soup.find("h1", attrs={'class':'yhB1nd'}).get_text(strip=True)

    except AttributeError:
        try:
            title = soup.find("h1", attrs={'class':'yhB1nd'}).get_text(strip=True)

        except:
            title=""

    return title

#Get Price Of Product Of Flipkart
def getPriceFlipkart(soup):
    try:
        price = soup.find("div", attrs={'class':'_30jeq3 _16Jk6d'}).string.strip()

    except AttributeError:
        try:
            price = soup.find("div", attrs={'class':'_30jeq3 _16Jk6d'}).string.strip()

        except:
            price=""

    return price

#Get Title Of Product Of Amazon
def getTitleAmazon(soup): 
    try:
        title = soup.find("span", attrs={'id':'productTitle'}).string.strip()

    except AttributeError:
        try:
            title = soup.find("span", attrs={'id':'productTitle'}).string.strip()

        except:
            title=""

    return title

#Get Price Of Product Of Amazon
def getPriceAmazon(soup):
    try:
        price = "₹" + soup.find("span", attrs={'class':'a-price-whole'}).string.strip()

    except AttributeError:
        try:
            price = "₹" + soup.find("span", attrs={'class':'a-price-whole'}).string.strip()

        except:
            price=""

    return price

#Main Function
if __name__ == '__main__':

    #User Agent
    HEADERS = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


    # #URLs
    print("Enter Amazon URL: ")
    amazonURL = input()
    print("Enter flipkart URL: ")
    flipkartURL = input()


    #HTTP Requests
    amazonPage = requests.get(amazonURL, headers=HEADERS)
    flipkartPage = requests.get(flipkartURL)


    # Soup Object Containing All Data
    soupAmazon = BeautifulSoup(amazonPage.content, "html.parser")
    soupFlipkart = BeautifulSoup(flipkartPage.text, "html.parser")
    

    #Dictionary To Contain Product Information
    d = {"Attributes":["Name", "Price"], "Amazon":[], "Flipkart":[]}
    d['Amazon'].append(getTitleAmazon(soupAmazon))
    d['Amazon'].append(getPriceAmazon(soupAmazon))
    d['Flipkart'].append(getTitleFlipkart(soupFlipkart))
    d['Flipkart'].append(getPriceFlipkart(soupFlipkart))

    #Print Product Data In Table Format
    print(tabulate(d, headers="firstrow", tablefmt="fancy_grid"))


   


    
