from django.contrib import messages
from django.shortcuts import redirect, render
from menu.models import Pizza
from .forms import ReservationForm


def index(request):
    # pylint: disable=no-member
    pizzas = Pizza.objects.filter(disponible=True).order_by('-signature', 'prix', 'nom')
    featured_pizzas = list(pizzas[:3])
    signature_pizzas = list(pizzas.filter(signature=True)[:3]) or featured_pizzas

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Votre demande de réservation a bien été prise en compte. Nous vous recontacterons si nécessaire."
            )
            return redirect('main:index')
    else:
        form = ReservationForm()

    context = {
        'featured_pizzas': featured_pizzas,
        'signature_pizzas': signature_pizzas,
        'pizza_count': pizzas.count(),
        'vegetarian_count': pizzas.filter(vegetarienne=True).count(),
        'starting_price': pizzas.order_by('prix').first().prix if pizzas.exists() else None,
        'reservation_form': form,
    }
    return render(request, 'main/index.html', context)
