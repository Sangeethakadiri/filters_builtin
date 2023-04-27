from django.shortcuts import render

# Create your views here.

def build_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'Hai THiS sAnGeeTa','dt':dt,'c':1}
    return render(request,'build_in_filters.html',d)
