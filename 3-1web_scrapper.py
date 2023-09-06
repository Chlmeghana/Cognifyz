import requests
from bs4 import BeautifulSoup
#requests library is used send a get request to the given website link
response=requests.get("https://www.thehindubusinessline.com/business-tech/chandrayaan-3-findings-show-moon-is-habitable/article67266138.ece")
#The response from the website is stored in "response" variable
a=BeautifulSoup(response.content,"html.parser")#html content of the response content is analysed and extracted using BeautifulSoup function 
title=a.title.text#That extracted data is stored in variable "a", that variable is used to extract the html content of the response such as title and paragraphs 
paras=a.find_all("p")
print(title)
for i in paras:
    print(i.text)