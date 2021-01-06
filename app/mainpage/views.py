from django.shortcuts import render


def index(request):
    """
    Main Page
    """
    return render(request, 'mainpage/index.html')
