from django.shortcuts import render

def diagnose(request):
    return render(request, "diagnosis/diagnose.html")

# Create your views here.
