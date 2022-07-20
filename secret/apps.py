from django.apps import AppConfig


class SecretConfig(AppConfig):
    name = 'secret'



class SecretConfig(AppConfig):
    name = 'secret'

    def ready(self):
        import secret.signals
 
   