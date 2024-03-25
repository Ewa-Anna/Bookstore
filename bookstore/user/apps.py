from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
    verbose_name = "User"

    def ready(self):
        import user.signals  # pylint: disable=C0415,W0611
