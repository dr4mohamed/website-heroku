from django.shortcuts import render
from django.http import Http404
from pathlib import Path

dir = "pages/"

def select_page(request, page):
    try:
        content = open(dir + page).read()
    except FileNotFoundError:
        raise Http404("'{}' not found.".format(page))

    pagename = page
    links = ["Home", "Links", "Applications"]
    header = page
    context = {
            "pagename": pagename,
            "links": links,
            "header": header,
            "content": content,
            }
    return render(request, "index.html", context)

def index(request):
    return select_page(request, "Home")
