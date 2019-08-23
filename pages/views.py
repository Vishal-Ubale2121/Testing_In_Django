from django.views.generic import TemplateView
from django.views.generic import ListView
from reportlab.pdfgen import canvas
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class MyPdf(ListView):
    def getpdf(request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="vishal.pdf"'
        p = canvas.Canvas(response)
        p.setFont("Times-Roman", 55)
        p.drawString(100, 700, " This file is created by Vishal.")
        p.showPage()
        p.save()
        return response