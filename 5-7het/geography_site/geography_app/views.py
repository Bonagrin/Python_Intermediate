from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from geography_app.models import Country, City


def index(request):
    cities = City.objects.all()
    return HttpResponse(loader.get_template('index.html').render({
        'countries': Country.objects.all(),
        'cities': cities,
        'eu_capitals': [city.name for city in cities if city.is_capital and city.country.eu_member],
    }, request))


def add_country(request):
    return HttpResponse(loader.get_template('country.html').render({}, request))


def add_country_record(request):
    Country(
        name=request.POST.get('name'),
        eu_member=request.POST.get('eu_member') == 'on'
    ).save()
    return HttpResponseRedirect(reverse('index'))


def update_country(request, id):
    return HttpResponse(loader.get_template('country.html').render({
        'country': Country.objects.get(id=id)
    }, request))


def update_country_record(request, id):
    country = Country.objects.get(id=id)
    country.name = request.POST.get('name')
    country.eu_member = request.POST.get('eu_member') == 'on'
    country.save()
    return HttpResponseRedirect(reverse('index'))


def delete_country(request, id):
    Country.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('index'))


def add_city(request):
    return HttpResponse(loader.get_template('city.html').render({
        'countries': Country.objects.all(),
    }, request))


def add_city_record(request):
    City(
        name=request.POST.get('name'),
        is_capital=request.POST.get('is_capital') == 'on',
        country=Country.objects.get(id=request.POST.get('country_id'))
    ).save()
    return HttpResponseRedirect(reverse('index'))


def update_city(request, id):
    return HttpResponse(loader.get_template('city.html').render({
        'city': City.objects.get(id=id),
        'countries': Country.objects.all(),
    }, request))


def update_city_record(request, id):
    city = City.objects.get(id=id)
    city.name = request.POST.get('name')
    city.is_capital = request.POST.get('is_capital') == 'on'
    city.country = Country.objects.get(id=request.POST.get('country_id'))
    city.save()
    return HttpResponseRedirect(reverse('index'))


def delete_city(request, id):
    City.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('index'))