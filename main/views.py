from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from main.models import Category, Product



def index_page(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})



#TODO: sdelat' spisok produktov
#TODO: avtorizaciya
#TODO: filtraciya, poisk, paginaciya
#TODO: korzina
#TODO: zakazy
#TODO: otpravku pisem
#TODO: deploy
#TODO: verstka