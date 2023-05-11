from django.shortcuts import render

# Create your views here.
# создание функций/представлений/контроллеров для отображения наших шаблонов
def index(request):
    context = {
        'title': 'Store', 
        'username': 'Sandzhi',
        'is_promotion': False,
    }
    return render(request, 'products/index.html', context)

def products(request):
    return render(request, 'products/products.html')
