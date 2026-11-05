from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Pizza


def index(request):
    vegetarian_only = request.GET.get('vegetarian') == '1'
    sort = request.GET.get('sort', 'price')
    category = request.GET.get('category', '')
    query = request.GET.get('q', '').strip()

    pizzas = Pizza.objects.filter(disponible=True)

    if vegetarian_only:
        pizzas = pizzas.filter(vegetarienne=True)

    if category:
        pizzas = pizzas.filter(categorie=category)

    if query:
        pizzas = pizzas.filter(
            Q(nom__icontains=query)
            | Q(ingredients__icontains=query)
            | Q(description__icontains=query)
        )

    if sort == 'name':
        pizzas = pizzas.order_by('nom')
    elif sort == 'price_desc':
        pizzas = pizzas.order_by('-prix', 'nom')
    else:
        sort = 'price'
        pizzas = pizzas.order_by('prix', 'nom')

    context = {
        'pizzas': pizzas,
        'vegetarian_only': vegetarian_only,
        'sort': sort,
        'category': category,
        'query': query,
        'pizza_count': pizzas.count(),
        'categories': Pizza.CATEGORIES,
    }
    return render(request, 'menu/index.html', context)



def detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id, disponible=True)
    suggested_pizzas = Pizza.objects.filter(disponible=True).exclude(pk=pizza.pk).order_by('-signature', 'prix', 'nom')[:3]
    return render(request, 'menu/detail.html', {
        'pizza': pizza,
        'suggested_pizzas': suggested_pizzas,
    })
