# This file is created by mine ----Komal-----
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name': 'komal', 'place': 'Mars'}
    return render(request, 'index.html')


# def about(request):
#     return HttpResponse("about page")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # print(removepunc)
    # print(djtext)

    # Check which checkbox is on
    if removepunc == "on":
        # analyzed = djtext

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose': 'Removed punctuations!',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # Analyse the text
        # return HttpResponse('''Remove Punctuations <a href='/'>Back</a>''')
        # return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed To Uppercase!',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Removed New Lines!', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Removed Extra Space!', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(removepunc != "on" and newlineremove != "on" and fullcaps != "on" and extraspaceremover != "on"):
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)


def removepunc(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    # Analyse the text
    return HttpResponse('''Remove Punctuations <a href='/'>Back</a>''')


def capitilize(request):
    return HttpResponse("Capitilize first")


def newlineremove(request):
    return HttpResponse("New line remove")


def spaceremover(request):
    return HttpResponse("space remover")


def charcount(request):
    return HttpResponse("Char Count")
