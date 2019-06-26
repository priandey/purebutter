from django.core.management.base import BaseCommand, CommandError
from products.models import Product

import requests


class Command(BaseCommand):
    '''
    Custom management command, used to populate database with data from OpenFoodFacts.
    Call command by typing "manage.py populate" in cli.
    '''

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
                    'sodas'
                    ]

        for category in categories:
            self.stdout.write(f'=== RECEIVING DATA FROM OPENFOODFACTS FOR {category} ===')
            payload['tag_1'] = category
            raw_output = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
            dict_output = raw_output.json()
            appended_product = list()
            product_incomplete = 0
            for entry in dict_output['products']:
                if entry in appended_product:
                    continue
                else:
                    appended_product.append(entry)
                try:
                    if entry['stores'] == '':
                        continue
                    product = Product(name=entry['product_name'],
                                      nutrition_grade=entry['nutrition_grades'],
                                      url=entry['url'],
                                      store=entry['stores'],
                                      category=category,
                                      thumb_link=entry["image_front_url"],
                                      diet_link=entry['selected_images']['ingredients']['display']['fr'])
                    product.save()
                except KeyError:
                    product_incomplete += 1
                    continue
            self.stdout.write(f'=== DONE {product_incomplete} products incomplete ===')


# TODO: Rework populate command
# TODO: Add "Nutella" !!!!