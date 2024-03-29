from django.shortcuts import render, get_object_or_404
from firstapp.models import Pizza

from firstapp.forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    # Request to db for getting all objects
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    form = OrderForm(request.POST or None, initial={
        'pizza': pizza
    })

    # Checks if all fields are filled
    if request.method == "POST":
        if form.is_valid():
            form.save()
            # Redirect to the pizza which user orders
            return HttpResponseRedirect('{}?sent=True'.format(reverse('pizza_detail', kwargs={'pizza_id': pizza.id})))

    return render(request, 'pizza_detail.html', {
        'pizza': pizza,
        'form' : form,
        'sent': request.GET.get('sent', False)
    })
