from urllib import request, error
from bs4 import BeautifulSoup

with request.urlopen('https://akipress.org') as resp:
    data = resp.read()
    #link= []
    turmush=[]
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('a', attrs={'class': 'newslink'})
    for item in items:
        title = item.get_text()
        link = item.get('href')
        if "turmush" in link:
            with request.urlopen( 'http:' + link) as  page:
                data2 = page.read()
                soup2 = BeautifulSoup(data2, 'html.parser')
                des = soup2.find_all('p')
                for i in des:
                    text = i.get_text()
                    with open(title + '.txt' , 'a', encoding = 'utf') as file:
                        file.write(text)
                        print("done")       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''#print(link)
        if 'turmush' in link:
            with request.urlopen(link) as res:
                dat = res.read ()
                sop = BeautifulSoup(dat, 'html.parser')
                it = sop.find_all('a')

print(it)
print(link)


with request.urlopen('//www.turmush.kg/ru/news:1817155?from=portal&place=last') as res:
    dat = res.read()
    sop = BeautifulSoup (dat , 'html.parser')
    it = sop.find_all('p')
    print(it)'''