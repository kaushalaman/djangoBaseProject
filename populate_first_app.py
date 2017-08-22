import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstProject.settings')

import django
django.setup()

## FAKE POPULATE SCRIPT
import random
from firstApp.models import AccessRecord,Topic,WebPage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for i in range(N):

        #create a topics

        topic = add_topic()

        #create fake entries

        fake_name = fakegen.company()
        fake_url  = fakegen.url()
        fake_date = fakegen.date()

        #create an entry for WebPage

        webpg = WebPage.objects.get_or_create(top_name = topic, name = fake_name, url = fake_url)[0]

        #create an entry for AccessRecord

        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]


if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating completed")
