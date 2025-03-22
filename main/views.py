from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context: dict[str, str] = {
        'title': "Home - Главная",
        'content': "Магазин мебели HOME",
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': "Home - О нас",
        'content': "О нас",
        'text_on_page': "Не следует, однако забывать, что новая модель организационной деятельности играет важную роль в формировании существенных финансовых и административных условий. Повседневная практика показывает, что консультация с широким активом позволяет выполнять важные задания по разработке существенных финансовых и административных условий. Повседневная практика показывает, что консультация с широким активом играет важную роль в формировании новых предложений. С другой стороны дальнейшее развитие различных форм деятельности требуют определения и уточнения направлений прогрессивного развития. "
    }

    return render(request, 'main/about.html', context)