from django.shortcuts import render

def home(request):
    # This line tells Django to find and display the template
    return render(request, 'music/index.html')