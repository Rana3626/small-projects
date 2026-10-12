import re

#opening and reading the file:
with open ("sample.txt",'r') as file: 
    text=file.read()




#extraction   
email= re.findall(r"([A-Za-z0-9\._]+@\w+\.\w+)" ,text)
phone=re.findall(r"\+?[0-9]{10,15}",text)
url=re.findall(r"(?<!@)\b(?:https?://)?(?:www\.)?[A-Za-z0-9-]+\.(?:com|org|net|co)(?:/\w+)?",text)
date=re.findall(r"\d{1,2}/\d{1,2}/\d{4}",text)

#printing results:
print("Regex Data Extractor")
print("--------------------------------------------")

if email:
    print(f"{len(set(email))} Emails found: ")
    for i in set(email):
        print(i)
        
print("\n********************************************")       

if phone:
    print(f"{len(set(phone))} Phone numbers found: ")
    for i in set(phone):
        print(i)
        
print("\n********************************************")       

if url:
    print(f"{len(set(url))} Urls found: ")
    for i in set(url):
        print(i)
        
print("\n********************************************")       
if date:
    print(f"{len(set(date))} Dates found: ")
    for i in set(date):
        print(i)
