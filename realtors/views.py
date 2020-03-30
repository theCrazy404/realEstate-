from django.shortcuts import render
from .models import Realtor
# Create your views here.
def index(request):
    return render(request,'realtors/realtor.html')


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)
    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors,
    }
    return render(request,'pages/about.html',context)