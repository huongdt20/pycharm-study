from django.shortcuts import render
from myApp import models
from datetime import datetime
from django.db.models import Max
# Create your views here.
def index(request):
    return render(request,'html1.html')
def contact(request):
    return render(request,'contact.html')
def lab411(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        MSSV = request.POST.get('MSSV')
        address = request.POST.get('address')
        b = models.lab411(mssv = MSSV, name = Name, address = address)
        b.save()
    return render(request, 'lab411.html')
def tl1(request):

    if request.method == "POST":
        name = request.POST.get('Name')
        mssv = request.POST.get('MSSV')
        address = request.POST.get('Address')
        if name != "" and mssv != "" and address:
            a = models.Tl1(name = name, mssv = mssv, address = address)
            a.save()
    b = models.Tl1.objects.all()
    return render(request, 'Tl1.html',{'a':b})

def post(request):
    if request.method == 'POST':
        content = request.POST.get('post')
        post__ = models.Post(content=content, time_post=datetime.now())
        post__.save()
    return  render(request, 'postHome.html')

def test(request):
    if request.method == 'POST':
        gioi_tinh = request.POST.get('gioi_tinh')
        a = models.test(text=gioi_tinh)
        a.save()
    return render(request,'test.html')
def test1(request):
    if request.method == "POST":
        uni = request.POST.get('radio1')
        unit = models.mone(unit = uni)
        unit.save()
    c = models.mone.objects.all()
    return render(request, 'lab411.html',{'unit':c})
def select(request):
    global unit1
    if request.method == "POST":
         sel = request.POST.get('select')
         unit1 = models.mone(unit = sel)
         unit1.save()
    d = models.mone.objects.all()
    return render(request, 'new.html',{'unit1':d})