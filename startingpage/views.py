from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
  template = loader.get_template('cellLayout.html')
  return HttpResponse(template.render())

def lysosomes(request):
  template = loader.get_template('lysosomes.html')
  return HttpResponse(template.render())

def ribosomes(request):
  template = loader.get_template('ribosomes.html')
  return HttpResponse(template.render())

def nucleus(request):
  template = loader.get_template('nucleus.html')
  return HttpResponse(template.render())

def ER(request):
  template = loader.get_template('ER.html')
  return HttpResponse(template.render())

def golgiapparatus(request):
  template = loader.get_template('golgiapparatus.html')
  return HttpResponse(template.render())

def mitochondria(request):
  template = loader.get_template('mitochondria.html')
  return HttpResponse(template.render())

def vacuoles(request):
  template = loader.get_template('vacuoles.html')
  return HttpResponse(template.render())