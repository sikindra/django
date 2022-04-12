from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data={
        'title':'Home Page'
    }
    return render(request,"index.html",data)    


def checkout(request):
    data = {
        'title': 'checkout Page'
    }
    return render(request, "checkout.html", data)


def contact(request):
    data = {
        'title': 'contact Page'
    }
    return render(request, "contact.html", data)


def account(request):
    data = {
        'title': 'account Page'
    }
    return render(request, "account.html", data)
def login(request):
    data = {
        'title': 'login Page'
    }
    return render(request, "login.html", data)


def sales_off(request):
    data = {
        'title': 'sales'
    }
    return render(request, "sales_off.html")
def book(request):
    data = {
        'title': 'Book Page'
    }
    return render(request, "book.html", data)


def about(request):
    data = {
        'title': 'about Page'
    }
    return render(request, "about.html", data)


def feature(request):
    data = {
        'title': 'feature page'
    }
    return render(request, "feature.html", data)


def book_offer(request):
    data = {
        'title': 'book_offer page'
    }
    return render(request, "book_offer.html", data)
    

def bookDetails(request,book_id):
    return HttpResponse(book_id)