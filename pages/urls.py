from django.urls import path
from .views import HomePageView, AboutPageView
from .views import MyPdf

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('pdf',MyPdf.getpdf)

]