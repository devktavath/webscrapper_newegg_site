from bs4 import BeautifulSoup as soup
#BeautifulSoup is library to traverse DOM / best way to parse html text within python.
from urllib.request import urlopen as uReq
#we need web client to grab something from internet,we do this using urllib in python ...inside this library we have are importing the required module called 'request' which has a function urlopen(),but not all of that from urllib is not required!

my_url = 'https://www.newegg.com/global/in-en/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+cards'

uClient = uReq(my_url)
#it bascically opens up the connection and grabs the webpage or just download it from internet!
#execution of above line depends on internet speed & if we ever want to read it just do 'uClient.read()  ------>  but this is gonna crash console based on how big the size of the webpage'.so don't read that at this stage ,we'll check later once it is loaded inside BeautifulSoup,just save it in a variable at this stage

page_html = uClient.read()
#raw html is stored in page_html

uClient.close()
#this is an open internet connection ,i'm gonna close it when i'm done with it!

page_soup = soup(page_html, "html.parser")
#now parse the html as it is big jumbo pack sized in the raw html
# giving raw html input as attribute to function and other attribute as how to parse it i.e xml/html

containers = page_soup.findAll("div", {"class":"item-container"})
#parses/grabs each product ...can be used for graphic cards and other products too as newegg.com has pretty standard way of writing its html for products , findAll finds all "div" with a feed of object i.e we're looking for html 'class' selector with a name "item-container"
#check the len(container) if greater than 0 ,there exists products 
#products can be accessed by container[index],where index is 0 - len-1

filename = "products.csv"
f = open(filename,"w")

headers = "brand, product_name, price_of_product"

f.write(headers)
#store it in a csv file 

#using for loop just grab the required contents,container variables helps in looping ,within that travel to 'div' inside it- go to the 'div' again and grab the 'a' tag and inside it grab 'img' tag,here attribute of the tags can be grabbed as if they were stored in dictionary i.e with index as its attribute.
#to travel inside... do container.div.div.a.img["title"]

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    price_container = container.findAll("li",{"class":"price-current"})
    price_of_product = price_container[0].strong.text

    f.write("\n" + brand + "," + product_name.replace(",","|") + "," + price_of_product.replace(",",""))

f.close()
