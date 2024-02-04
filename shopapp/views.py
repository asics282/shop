from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
    site_data = {
        'site_name': 'Магазин',
        'site_description': 'Добро пожаловать в наш магазин!',
    }

    html_content = """
        <h1>{site_name}</h1>
        <p>{site_description}</p>
    """.format(**site_data)

    return HttpResponse(html_content)

def about(request):
    about_me_data = {
        'my_name': 'Онлайн-магазин велосиаедных цепей',
        'my_bio': 'Приветствуем Вас в нашем магазине качественных велосипедных цепей',
    }

    html_content = """
        <h2>О нас: {my_name}</h2>
        <p>{my_bio}</p>
    """.format(**about_me_data)

    return HttpResponse(html_content)
