from django.http import HttpRequest , HttpResponse ,JsonResponse
import json
from.models import smartfon 




# Create your views here.

def add(reqeust: HttpRequest) :
    if reqeust.method == 'POST':
            data = json.loads(reqeust.body.decode('utf-8'))
            s = ''
            mom = ''
            for i in data['RAM']:
                if i.isdigit():
                    s+=i
                else:
                    break
            for i in data['memory']:
                if i.isalpha():
                     continue
                else:
                     mom+=i
            n = eval(mom)
            product = smartfon.objects.create(
                price=data['price'],
                img_url=data['img_url'],
                color=data['color'],
                ram=int(s),
                memory=int(n),
                name=data['name'],
                model=data['company']
            )
            product.save()
            return JsonResponse({'status': 'OK'})
    else:
            return HttpResponse("Method error")
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
def updete(request:HttpRequest,id:int):
    if request.method == "POST":
            data = request.body.decode('utf-8')
            data = json.loads(data)
            item = smartfon.objects.filter(id=id) 
            item.update(
                name  = data['name'],
                model = data['model'],
                color = data['color'],
                ram   = data['ram'],
                memory = data['memory'],
                price  = data['price'], 
                img_url = data['url'], 
            )
            obj = smartfon.objects.all()
            ruyxat = []
            for item in obj:
                ruyxat.append(item.to_dict())
            return JsonResponse({"smartphes":ruyxat}, safe=False)


def get_name(reqeust : HttpRequest , name ):

    data=smartfon.objects.filter(name__contains = name)
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)



def lst_models(request: HttpRequest) -> JsonResponse:
    """get all models"""
    try:
        product = smartfon.objects.all()
        data = []
        for i in product:
            data.append(i.to_dict()['model'])
        data = list(set(data))
    except:
        return JsonResponse({"data":"not found"})
    return JsonResponse(data=data, safe=False)


def get_color(reqeust : HttpRequest , color):
    data=smartfon.objects.filter(name__contains = color)
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)




def get_madel(reqeust : HttpRequest , model):
    data=smartfon.objects.filter(name__contains = model)
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)



def get_in(reqeust : HttpRequest , price1 , price2):
    data = smartfon.objects.filter(__in=[price1 , price2])
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)


def get_price(reqeust : HttpRequest , price):
    data = smartfon.objects.filter(price__in=price)
    r=[]
    for i in data:
        r.append(i.to_dict())

    return JsonResponse(r , safe=False)


