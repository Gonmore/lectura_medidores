from django.apps import AppConfig


class SntmeterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sntmeter'
    
    def ready(self):
        from sntmeter.jobs import updater
        updater.start()
