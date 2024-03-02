import json , requests
import random

def sed_data(data):
    url='http://127.0.0.1:8000/api/add/'
    r=requests.post(url ,json=data)
    return r.status_code

with open('db.json'  , 'r') as file:

    data=json.load(file)

appe=data['Apple']

yil = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2013,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
y = random.choice(yil)

oy=[1,2,3,4,5,6,7,8,9,10,11,12]
o = random.choice(oy)

kun = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
k = random.choice(kun)

d=f'{k}"."{o}"."{y}'

for i,v in appe.items():
    item = {
        "price":float(v["price"]),
        "img_url":v["img_url"],
        "color":v["color"],
        "ram": v["RAM"],
        "memory":v["memory"],
        "name":v["name"],
        "model":v["company"],
        "data": d
    }
    print(sed_data(item))