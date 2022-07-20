# from sys import modules
# from django.dispatch import receiver
# from django.db.models.signals import pre_save
# from django.contrib.auth.models import User


# @receiver(pre_save, sender=User)
# def user_updated(sender,instance, **kwargs):
#         print("TRUEEEE")
#         print("***----USER-----***")
#         user = kwargs.get('instance', None)
#         print(user,"***-----USER-----***")
     
#         # module.signal.send(msg='this is a message to append on the response body')

       
#         # if user:
#         #     new_password = user.password
#         #     print(new_password,"------NEW PASSWORD ------")
#         #     try:
#         #         old_password = User.objects.get(pk=user.pk).password
#         #         print(old_password,"old-password")
#         #     except User.DoesNotExist:
#         #         old_password = None
#         #     if new_password != old_password:
#         #         pass