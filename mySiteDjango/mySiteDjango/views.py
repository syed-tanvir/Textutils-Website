from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext=request.POST.get("text", "default")
    removepun= request.POST.get("removepunc" , "off")
    fullcaps=request.POST.get("fullcaps", "off")
    newlineremove= request.POST.get("newlineremove", "off")
    spaceremove= request.POST.get("extraspace", "off")

    if removepun =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=''
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        #params={'Purpose': 'Remove Punctiation', 'analyzed_text':analyze }
        #return render(request, "analyze.html",params)
        djtext=analyze

    if(fullcaps == "on"):
        analyze=''
        for char in djtext:
            analyze = analyze + char.upper()

        #params={'Purpose': 'Remove Punctiation', 'analyzed_text':analyze }
        #return render(request, "analyze.html",params)
        djtext=analyze

    if(newlineremove == "on"):
        analyze=''
        for char in djtext:
            if char != "\n" and char!="\r":
                analyze = analyze + char

        #params={'Purpose': 'Remove Punctiation', 'analyzed_text':analyze }
        #return render(request, "analyze.html",params)
        djtext=analyze

    if(spaceremove == "on"):
        analyze=''
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyze = analyze + char

        djtext=analyze
    params={'Purpose': 'Text Util', 'analyzed_text':analyze }
    return render(request, "analyze.html",params)

    if(removepun !="on" and fullcaps != "on" and newlineremove != "on" and spaceremove != "on"):
         return HttpResponse("<h1>Please select any operation and try again.</h1>")


