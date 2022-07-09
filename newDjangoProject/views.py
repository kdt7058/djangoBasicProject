from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    a = request.GET.get('text','default')
    return HttpResponse("Index Page")

def about(request):
    return HttpResponse("""Hi Bot <a href="https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/">GG CLick</a>   """)

def space(request):
    return HttpResponse("space Page <a href='/'>back</a>")

def home(request):
    a = request.POST.get('punc text', 'default')
    b = request.POST.get('remove punc', 'off')
    c = request.POST.get('radio1', 'off')
    d = request.POST.get('radio2', 'off')
    e = request.POST.get('radio3', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    opstr = ""
    if b == "on":
        for ch in a:
            if ch not in punctuations:
                opstr += ch
    else:
        opstr=a
    if c == "on":
        capi = opstr.upper()
        opstr = ""
        opstr = capi

    if d == "on":
        newLine= ""
        for i in opstr:
            if i != "\n" and i!="\r":
                newLine += i
        opstr = ""
        opstr = newLine
    if e == "on":
        space= ""
        for index, i in enumerate(opstr):
            if opstr[index] == " " and opstr[index+1] == " ":
                pass
            else:
                space += i
        opstr = ""
        opstr = space

    params = {'inputtxt': a, 'outputtxt': opstr}

    return render(request, 'index.html', params)

def punc(request):
    return render(request, 'punc.html')

