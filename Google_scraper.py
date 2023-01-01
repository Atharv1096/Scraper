from bs4 import BeautifulSoup
from selenium import webdriver
import csv

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("chromedriver", chrome_options=options)


data = input("Enter result you want to search: ")
data.replace(' ','+')
url = "https://www.google.com/search?q="+str(data)+"&start=0"
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

if soup.find('div', class_="Z0LcW t2b5Cf") != None:
    result = soup.find('div', class_="Z0LcW t2b5Cf").get_text()
elif soup.find('div', class_="Z0LcW t2b5Cf") == None and soup.find('div', class_="Z0LcW t2b5Cf CfV8xf")!=None:
    result = soup.find('div', class_="Z0LcW t2b5Cf CfV8xf")
    result = result.find('a').get_text()
elif soup.find('div', class_="Z0LcW t2b5Cf CfV8xf")==None and soup.find('div', class_="Z0LcW AZCkJd d2J77b t2b5Cf") != None:
    result = soup.find('div', class_="Z0LcW AZCkJd d2J77b t2b5Cf")
    result = result.find('div', class_="IZ6rdc").get_text()
elif soup.find('div', class_="Z0LcW AZCkJd d2J77b t2b5Cf") == None and soup.find('div', class_ = "Z0LcW t2b5Cf vMhfn")!=None:
    result = soup.find('div', class_="Z0LcW t2b5Cf vMhfn").get_text()


print(result)

answer = result

fields = ['question','answer']

row = [str(data), str(answer)]
filename = "dataset.csv"
with open(filename, 'a') as csvfile: #while writing to fresh new file replace 'a with 'w'
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(row)
    # writing the fields (CAUTION: RUN ONLY FIRST TIME below row)
    #csvwriter.writerow(fields) 
        
    # writing the data rows 
    