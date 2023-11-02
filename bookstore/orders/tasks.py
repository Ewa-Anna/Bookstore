from celery import shared_task

from django.core.mail import send_mail

from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order no {order.id} from Bookstore'
    message = f'Welcome {order.first_name},\n\n' \
                f'Thank you for odering at Bookstore.\n' \
                f'Your order no is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@bookstore.com',
                          [order.email])
    return mail_sent