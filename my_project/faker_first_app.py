import os

from my_project.first_app import models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
import django

django.setup()

import random
import first_app.models as md
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = md.Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for i in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        wbpage = md.WebPage.objects.get_or_create(topic=top, name=fake_name, urls=fake_url)[0]

        accrec = md.AccessRecord.objects.get_or_create(name=wbpage, date=fake_date)[0]



if __name__ == '__main__':
    print('poulating')
    populate(20)
    print('population complete')

