from django.conf import settings
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from myapp import models
from myapp.models import Industrial_Product


class Homepage(TemplateView):
    template_name = 'Homepage.html'


class Contactpage(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        my_feedback = (name, email, message)
        final = '\n'.join(my_feedback)

        send_mail('contact form', final, settings.EMAIL_HOST_USER, ['tattvam2@gmail.com'], fail_silently=False)
        return render(request, 'homepage.html')


class Hydraulic(ListView):
    template_name = 'hydraulics.HTML'
    context_object_name = 'hydraulic'
    queryset = models.HydraulicProduct.objects.select_related('company').order_by('company')


class igo(ListView):
    template_name = 'industialgear.html'
    context_object_name = 'igo'
    queryset = models.Industrial_Product.objects.select_related('company').order_by('company')

class mwo(ListView):
    template_name = 'mwo.html'
    context_object_name = 'mwo'
    queryset = models.MCW_Product.objects.select_related('company').order_by('company')

class rco(ListView):
    template_name = 'rco.html'
    context_object_name = 'rco'
    queryset = models.RCO_Product.objects.select_related('company').order_by('company')

class spo(ListView):
    template_name = 'spo.html'
    context_object_name = 'spo'
    queryset = models.SPL_Product.objects.select_related('company').order_by('company')

class TFO(ListView):
    template_name = 'tranformer.html'
    context_object_name = 'tfO'
    queryset = models.TRSProduct.objects.select_related('company').order_by('company')

class tur(ListView):
    template_name = 'turbine.html'
    context_object_name = 'tur'
    queryset = models.TUR_Product.objects.select_related('company').order_by('company')

class wro(ListView):
    template_name = 'wireope.html'
    context_object_name = 'wro'
    queryset = models.WIRProduct.objects.select_related('company').order_by('company')

class ING(ListView):
    template_name = 'ing.html'
    context_object_name = 'ing'
    queryset = models.IN_GreaseProduct.objects.select_related('company').order_by('company')

class ao(ListView):
    template_name = 'ao.html'
    context_object_name = 'ao'
    queryset = models.AO_Product.objects.select_related('company').order_by('company')

class AGO(ListView):
    template_name = 'ato.html'
    context_object_name = 'ago'
    queryset = models.AGO_Product.objects.select_related('company').order_by('company')

class rdc(ListView):
    template_name = 'rdc.html'
    context_object_name = 'rdc'
    queryset = models.RDC_Product.objects.select_related('company').order_by('company')

