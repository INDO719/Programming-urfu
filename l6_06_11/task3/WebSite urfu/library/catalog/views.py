"""Представления приложения catalog."""

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def get_info(request):
    """Отображает информацию о книге.

    Формирует словарь с данными книги и передаёт его в шаблон
    ``catalog/book_detail.html`` в контексте ``info``.

    Параметры:
        request (HttpRequest): Объект HTTP-запроса.

    Возвращает:
        HttpResponse: Отрендеренная страница с информацией о книге.
    """

    info = {
        'title': 'Абра кадабра',
        'author': 'Лев Толстый',
        'year': 1984,
        'rating': 5
    }

    return render(request, 'catalog/book_detail.html', {'info': info})