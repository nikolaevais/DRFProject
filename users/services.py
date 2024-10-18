import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """создает продукт в страйп"""
    product = instance.payment_course if instance.payment_course else instance.payment_lesson
    stripe_product = stripe.Product.create(name=product)
    return stripe_product.get('id')


def create_stripe_price(product_id, amount):
    """создает цену в страйпе"""
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product_id
    )


def create_stripe_session(price):
    """создает сессию на оплату в страйпе"""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
