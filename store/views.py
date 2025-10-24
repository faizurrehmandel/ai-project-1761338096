from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, paid=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    order = Order.objects.filter(user=request.user, paid=False).first()
    return render(request, 'store/cart_detail.html', {'order': order})

@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, paid=False).first()
    if request.method == 'POST':
        try:
            charge = stripe.Charge.create(
                amount=int(order.get_total_cost() * 100),
                currency='usd',
                description=f'Order {order.id}',
                source=request.POST['stripeToken']
            )
            order.paid = True
            order.save()
            return redirect('order_success')
        except stripe.error.CardError as e:
            return render(request, 'store/checkout.html', {'error': str(e)})
    return render(request, 'store/checkout.html', {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })