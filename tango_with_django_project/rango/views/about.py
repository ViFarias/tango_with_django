from django.shortcuts import render


def about(request):
    context_dict = {'autor': 'Viviane Laís de Farias'}
    return render(request, 'rango/about.html', context=context_dict)
