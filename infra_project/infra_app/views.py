from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось не с первого раза!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
