from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('patients/', views.patients_page, name='patients_page'),
    # path('write-review/', views.create_review, name='write_review'),
]