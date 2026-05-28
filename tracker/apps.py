from django.apps import AppConfig


class TrackerConfig(AppConfig):
    name = 'tracker'
    verbose_name = 'Financial Tracker'

    def ready(self) -> None:
        from . import signals
