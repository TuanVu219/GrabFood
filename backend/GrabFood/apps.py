from django.apps import AppConfig


class GrabfoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GrabFood'

    def ready(self):
        import GrabFood.signals