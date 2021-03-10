from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.models import UserProfile
from bargain.models import Purchase


@login_required
def create_purchase(req, user_pk, watch_pk):
    purchase = Purchase(user_id=user_pk, watch_id=watch_pk)
    purchase.save()
    return redirect('purchases', user_pk)


@login_required
def show_purchases(req, pk):
    profile = UserProfile.objects.get(pk=pk)
    context = {
        'profile': profile,
        'purchases': profile.purchase_set.all(),
        'prices': ' + '.join(map(str, (purchase.watch.price for purchase in profile.purchase_set.all()))),
        'end_price': sum(purchase.watch.price for purchase in profile.purchase_set.all()),
    }

    return render(req, 'bargain/purchases.html', context=context)


def remove_purchase(req, user_pk, product_pk):
    purchase = Purchase.objects.get(pk=product_pk)
    purchase.delete()
    return redirect('purchases', user_pk)