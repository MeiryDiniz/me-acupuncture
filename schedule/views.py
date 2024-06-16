from django.shortcuts import render
from django.views import generic
from .models import Review
# from django.http import HttpResponse

# Create your views here.

class ReviewList(generic.ListView):
    # model = Review
    queryset = Review.objects.all()
    template_name = "review_list.html"


# def index(request):
#     if request.method == "GET":
#         return HttpResponse("Hello Patient!")
#     elif request.method == "POST":
#         return HttpResponse("Thank you!")    
