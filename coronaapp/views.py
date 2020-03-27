from django.shortcuts import get_object_or_404, render
from django.http import Http404, JsonResponse
from .utilfinal import result  

def index(request):
   return render(request, 'index.html')

def calc(request):
   population = float(request.GET.get('population', ''))
   count = float(request.GET.get('count', ''))
   lockdown = float(request.GET.get('lockdown','0'))
   gamma = float(request.GET.get('gamma','0.04'))
   beta = float(request.GET.get('beta','0.16'))
   u = float(request.GET.get('u','0.02'))
   
   res=result(population,0,0,count,population-count,0,gamma,beta/population,3,u)
   return JsonResponse(res, safe=False)