

def fidelity_promo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

def bulk_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

def large_promo(order):
    discount_item = {item.product for item in order.cart}
    if len(discount_item) >= 10:
        return order.total() * 0.07
    return 0