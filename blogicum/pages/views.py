from django.shortcuts import render


def about(request):
    """Отображает страницу 'О нас'."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Отображает страницу с правилами."""
    template = 'pages/rules.html'
    return render(request, template)
