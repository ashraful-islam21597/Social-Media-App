from django.db.models.signals import post_save
from django.dispatch import receiver

import notifications


# @receiver(post_save, sender=notifications)
# def post_save_create_notifications(sender, instance, created, **kwargs):
#     if created:
#         if instance.notification_TYPE==1:
#             text=f''