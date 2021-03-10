def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], 'Invalid discount'
    return price


shoes = {
    'name': 'Hyper Beast',
    'price': 14900,
}

print(apply_discount(shoes, 0.1))
print(apply_discount(shoes, 10))
