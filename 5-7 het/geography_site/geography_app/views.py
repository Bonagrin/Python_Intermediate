from django.http import HttpResponse

def index(request):
    return HttpResponse('Index')

def add_country(request):
    return HttpResponse('add_country')

def add_country_record(request):
    return HttpResponse('add_country_record')

def update_country(request, id):
    return HttpResponse(f'Update_country: {id}')

def update_country_record(request, id):
    return HttpResponse(f'Update_country_record: {id}')

def delete_country(request, id):
    return HttpResponse(f'Delete_country: {id}')

def add_city(request):
    return HttpResponse('add_city')

def add_city_record(request):
    return HttpResponse('add_city_record')

def update_city(request, id):
    return HttpResponse(f'Update_city: {id}')

def update_city_record(request, id):
    return HttpResponse(f'Update_city_record: {id}')

def delete_city(request, id):
    return HttpResponse(f'Delete_city: {id}')
