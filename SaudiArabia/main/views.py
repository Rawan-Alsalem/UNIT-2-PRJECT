from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse # Import JsonResponse
from django.shortcuts import resolve_url
from django.shortcuts import redirect


# Create your views here.

def index_view(request: HttpRequest):
    # Read the font_size cookie state and pass it to the template context
    font_size = request.COOKIES.get('font_size', 'normal')
    return render(request, "main/index.html", {'font_size': font_size})


def heritage_view(request: HttpRequest):
    return render(request, "main/heritage.html")


def art_view(request: HttpRequest):
    return render(request, "main/art.html")


def architecture_view(request: HttpRequest):
    return render(request, "main/architecture.html")


def festivals_view(request: HttpRequest):
    return render(request, "main/festivals.html")


def fashion_view(request: HttpRequest):
    return render(request, "main/fashion.html")


def music_view(request: HttpRequest):
    return render(request, "main/music.html")


# cookies view for font
def toggle_font(request):
    # This view is now called via AJAX/Fetch, so we return a JsonResponse
    # instead of a redirect to prevent page reload.
    current_size = request.COOKIES.get('font_size', 'normal')

    if current_size == 'normal':
        new_size = 'large'
    else:
        new_size = 'normal'
    
    # We must respond with an HttpResponse or a subclass (like JsonResponse)
    # to set the cookie.
    response = JsonResponse({'status': 'success', 'font_size': new_size})
    response.set_cookie('font_size', new_size)

    return response