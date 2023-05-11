from django.shortcuts import render

# Create your views here.
# создание функций/представлений/контроллеров для отображения наших шаблонов
def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')