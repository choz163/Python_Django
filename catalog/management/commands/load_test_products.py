import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.utils import timezone


class Command(BaseCommand):
    help = 'Load test products'

    def handle(self, *args, **kwargs):
        with open('catalog.json') as f:
            data = json.load(f)

        for entry in data:
            model = entry['model']
            fields = entry['fields']

            if model == 'catalog.category':
                category = Category(**fields)
                category.save()
                self.stdout.write(self.style.SUCCESS(f'Loaded category: {fields["name"]}'))
            elif model == 'catalog.product':
                category_id = fields.pop('category')
                category = Category.objects.get(pk=category_id)

                fields['created_at'] = timezone.now()
                product = Product(**fields)
                product.category = category
                product.save()
                self.stdout.write(self.style.SUCCESS(f'Loaded product: {fields["name"]}'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded test products'))
