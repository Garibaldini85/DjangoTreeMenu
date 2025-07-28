from django.shortcuts import render


def test_menu_view(request):
    return render(request, 'base.html')


def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)
