from django.core.management.base import BaseCommand
from faker import Faker
from website.models import Record

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **options):
        fake = Faker()
        for i in range(10):
            record = Record(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                zipcode=fake.zipcode(),
            )
            record.save()
