from django.shortcuts import render
from django.views import generic
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
# from django.http import HttpResponse

# Create your views here.

class ReviewList(generic.ListView):
    # model = Review
    queryset = Review.objects.all().order_by("-created_on")[:3]
    template_name = "schedule/index.html"

@login_required
def patients_page(request):
    # reviews = Review.objects.all().order_by("-created_on")
    reviews = Review.objects.filter(author=request.user).order_by("-created_on")
    review_count = reviews.filter(approved=True).count()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review has being successfuly submitted and is awaiting approval!'
            )
            return redirect('patients_page')
    else:
        form = ReviewForm() 
    
    return render(
        request,
        "schedule/patients.html",
        {
            "reviews": reviews,
            "review_count": review_count,
            "form": form,
        },
    )
# def patients_page(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.author = request.user
#             review.save()
#             return redirect('patients_page')
#     else:
#         form = ReviewForm()
#     return render(request, 'patients.html', {'form': form})
    




# def index(request):
#     if request.method == "GET":
#         return HttpResponse("Hello Patient!")
#     elif request.method == "POST":
#         return HttpResponse("Thank you!")    
