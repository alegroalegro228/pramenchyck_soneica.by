from django.shortcuts import render


def about(request):
    return render(request, template_name='about/about.html')


def contacts(request):
    return render(request, template_name='about/contacts.html')