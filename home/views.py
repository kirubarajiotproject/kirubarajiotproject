from django.shortcuts import render
import random
import serial
from django.http import JsonResponse
def getData():
    print("------Reading collection starts now------")
    sr = serial.Serial("COM3",9600)
    st = list(str(sr.readline(),'utf-8'))
    sr.close() 
    print("------Reading collection ends successfully------")
    return (str(''.join(st[:-2]))).split('|')[:-1]

def getData5():
    n = random.randint(1,100)
    return n

def index(request):
    return render(request, 'home/index.html')

def home(request):
        return render(request,'home/home.html')

def ajax_data(request):
    data = getData()
    data = {'data1': data[0], 'data2': data[1], 'data3': data[2], 'data4': data[3], 'data5': getData5()}
    return JsonResponse(data)