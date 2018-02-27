from bs4 import BeautifulSoup # initially we import the required package

import requests
search = input("Search for: ")

params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)#here we append the "q" parameter to the search

soup = BeautifulSoup(r.text,"html.parser")# by using Html parser we get the data

result=soup.find("ol",{"id":"b_results"})# from the list we find the items with an ID b_results. id is an html attribute

links=result.findAll("li",{"class":"b_algo"})# from the list find all the items with class b_algo

for item in links:
    item_text=item.find("a").text #we find the text from anchor tags
    item_href=item.find("a").attrs["href"]#we find the links from anchor tags
    
    if item_text and item_href:
        print(item_text)
        print(item_href)
     
