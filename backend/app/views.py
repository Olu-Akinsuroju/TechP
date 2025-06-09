from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'app/index.html')

@require_http_methods(["POST"])
def submit(request: HttpRequest) -> HttpResponse:
    interest = request.POST.get('interest', '')
    tools = request.POST.getlist('tools')
    activity = request.POST.get('activity', '')

    path = "General Tech"
    explanation = "Your interests and skills point towards a general exploration of technology."

    if 'Unity' in tools:
        path = "Game Development"
        explanation = "Your interest in Unity suggests a path in Game Development, creating interactive experiences."
    elif 'Terminal' in tools and activity == 'building websites':
        path = "Web Development"
        explanation = "Knowing how to use a Terminal and an interest in building websites are key for Web Development."
    elif activity == 'analyzing data':
        path = "Data Science"
        explanation = "Your excitement for analyzing data is a strong indicator for a future in Data Science."
    elif 'Python' in tools and activity == 'building websites':
        path = "Web Development (Python/Django)"
        explanation = "With Python skills and an interest in web building, consider focusing on Python-based web frameworks like Django."
    elif 'JavaScript' in tools and activity == 'building websites':
        path = "Web Development (JavaScript)"
        explanation = "JavaScript is fundamental for frontend web development and increasingly for backend too."


    context = {
        'path': path,
        'explanation': explanation,
        'interest': interest, # Included for potential future use or richer result page
        'tools': tools,
        'activity': activity
    }
    return render(request, 'app/result.html', context)
