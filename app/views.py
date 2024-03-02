from django.http import HttpRequest , HttpResponse ,JsonResponse
import json
from.models import smartfon 




# Create your views here.

def add(reqeust : HttpRequest):
    if reqeust.method=='POST':
        d=reqeust.body.decode('UTF-8')
        datas=json.loads(d)
        price  =datas['price'],
        img_url=datas['img_url'],
        color  =datas['color'],
        ram    =datas['RAM'],
        memory =datas['memory'],   
        name   =datas['name'],
        model  =datas['company'],
        data   =datas['data']

        produk=smartfon.objects.create(
          price  =price,
          img_url=img_url,
          color  =color,
          ram    =ram,
          memory =memory,
          name   =name,
          model  =model,
          data   =data  
        )
        produk.save()

        return JsonResponse({'salom': 'salom'})
def get(reqeust : HttpRequest , pk) -> JsonResponse:
    if reqeust.method=='GET':
    
        datas=smartfon.objects.get(id=pk)
        a={
        "price"  :datas.price,
        "img_url":datas.img_url,
        "color"  :datas.color,
        "ram "   :datas.ram,
        "memory" :datas.memory,
        "name"   :datas.name,
        "model"  :datas.model,
        "data"   :datas.data,


        }



        return  JsonResponse({pk : a})
def get_all(reqeust : HttpRequest) -> JsonResponse:
    data=smartfon.objects.all()
    
    a=[]
    for i in data:
    
        a.append(i.to_dict())
    # print(a , "salom")

    return JsonResponse({"smartfon " : a})
def delete(reqeust : HttpRequest , pk):
    a=smartfon.objects.filter(id=pk).delete()

    return JsonResponse({"smartfon_delete" : "oK"})
def updete(reqeust : HttpRequest):



    pass


def get_name(reqeust : HttpRequest , name ):

    data=smartfon.objects.filter(name_contains = name)
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)


def get_color(reqeust : HttpRequest , color):
    data=smartfon.objects.filter(name_contains = color)
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)



def get_data(reqeust : HttpRequest , data):
    data=smartfon.objects.filter(pub_date__range=data)
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)


def get_andwith(reqeust : HttpRequest , sendwith):
    data=smartfon.objects.filter(pub_date__range=data)
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)



def get_in(reqeust : HttpRequest , price1 , price2):
    data = smartfon.objects.filter(name_in=[price1 , price2])
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)


def get_price(reqeust : HttpRequest , price):
    data = smartfon.objects.filter()


