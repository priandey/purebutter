from django.core.management.base import BaseCommand
from products.models import Product

import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        payload = {'action': 'process',
                   'tagtype_0': 'languages',
                   'tag_contains_0': 'contains',
                   'tag_0': 'fr',
                   'tagtype_1': 'categories',
                   'tag_contains_1': 'contains',
                   'tag_1': '',
                   'sort_by': 'unique_scans_n',
                   'json': '1',
                   'page_size': '500',
                   'page': '1'}

        categories = ['biscuits-et-gateaux',
                    'charcuteries',
                    'cereales-pour-petit-dejeuner',
                    'plats-prepares',
                    'fromages',
                    'sodas',
                    'snacks-sales'
                    ]

        for category in categories:
            openfoodfacts_response = self.get_category(category, payload)
            appended_product = list()
            product_incomplete = 0
            for entry in openfoodfacts_response['products']:
                if entry in appended_product:
                    continue
                else:
                    appended_product.append(entry)
                try:
                    if entry['stores'] == '':
                        product_incomplete += 1
                        continue
                    self.append_product(category, entry)
                except KeyError:
                    product_incomplete += 1
                    continue
            self.stdout.write(f'=== DONE {product_incomplete} products incomplete ===')

    @staticmethod
    def append_product(self, category, entry):
        product = Product(name=entry['product_name'],
                          nutrition_grade=entry['nutrition_grades'],
                          url=entry['url'],
                          store=entry['stores'],
                          category=category,
                          thumb_link=entry["image_front_url"],
                          diet_link=entry['selected_images']['ingredients']['display']['fr'])
        product.save()

    def get_category(self, category, payload):
        self.stdout.write(f'=== RECEIVING DATA FROM OPENFOODFACTS FOR {category} ===')
        payload['tag_1'] = category
        raw_output = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
        dict_output = raw_output.json()
        return dict_output