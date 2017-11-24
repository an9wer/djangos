from django.core.management.base import BaseCommand, CommandError

from model_layer.models import ProxyModel


class Command(BaseCommand):
    help = "initialize models from model_layer"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # ProxyModel
        ProxyModel.objects.create(field="proxy model")

        self.stdout.write(
            self.style.SUCCESS('Successfully initialize models'))
