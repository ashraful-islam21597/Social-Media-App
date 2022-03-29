from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from posts.models import Post, Post_reaction, Reaction


@receiver(post_save, sender=Post)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Post_reaction.objects.create(post=instance, )


@receiver(pre_save, sender=Reaction)
def pre_save_like(sender, instance, **kwargs):
    if instance.react == False:
        print(instance.react)
        instance.post_reaction.total_react = instance.post_reaction.total_react + (1)
        instance.react = True
        instance.post_reaction.save()

    # elif instance.react == True:
    #     print(instance.react)
    #     instance.post_reaction.total_react = instance.post_reaction.total_react - (1)
    #     instance.post_reaction.save()
    #     instance.delete()

