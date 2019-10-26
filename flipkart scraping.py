#importing libraries
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#writing file with fetching data 
filename="F:\\mitv_reviews.csv"
f = open(filename, 'w', encoding="utf-8")
headers="rating,review,place,date,des\n"
f.write(headers)

#website URL
url= "https://www.flipkart.com/mi-led-smart-tv-4a-pro-108-cm-43-android/product-reviews/itmfbzck4mhggxxg?pid=TVSFBZCKAVGCUCME&page=1"

#here the loop iterates page 1 to 1023
#in each page contain 10 reviews
#the loop iterates and fetch data in each page and writing to a file
for i in range(1,1024):
    url1=url.replace("page=1","page="+ str(i))
    
    uClinet= uReq(url1)
    page_html= uClinet.read()
    uClinet.close()

    page_soup= soup(page_html, "html.parser")

    bags= page_soup.findAll("div",{"class":"col _390CkK _1gY8H-"})

    text=soup.prettify(bags[0])
    '''it will show the html code of one review
       then we can find the location of text in html code and after
       fetching the data
    '''                                             

    len(bags) #length of bag which contains html code of 14 reviews


    for bag in bags:
        #rating
        if(bag.findAll("div",{"class":"hGSR34 E_uFuv"})):
            rat= bag.findAll("div",{"class":"hGSR34 E_uFuv"})
            rating= rat[0].text
            
        elif(bag.findAll("div",{"class":"hGSR34 _1nLEql E_uFuv"})):
            rat= bag.findAll("div",{"class":"hGSR34 _1nLEql E_uFuv"})
            rating= rat[0].text
             
        elif(bag.findAll("div",{"class":"hGSR34 _1x2VEC E_uFuv"})):
            rat= bag.findAll("div",{"class":"hGSR34 _1x2VEC E_uFuv"})
            rating= rat[0].text
            
        else:
            rating=str("no rating")
            
        
        #review
        rev= bag.findAll("p")
        review= rev[0].text
        
        pla= rev[2].text
        place=pla.replace("Certified Buyer, ","")
        
        update_date= rev[3].text
        date=update_date.replace('days', 'below month')
        
    
        #description of review
        desc=bag.find_all("div",{"class":""})
        description=desc[0].text
        des=description.replace("READ MORE","")
        
    
        #print("rat:",rating)
        #print("review:",review)
        #print("place:",place)
        #print("date:",date)
        #print("desc:",des)
        
        #saving file
        f.write(rating + ',' + review + ',' + place + ',' + date + ',' + des + '\n')
        
f.close()

    