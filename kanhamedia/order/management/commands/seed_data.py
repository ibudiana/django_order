from django.core.management.base import BaseCommand
from faker import Faker
from order.models import User, Template, Hosting, Order

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Seed Users
        for _ in range(10):
            User.objects.create(
                no_ktp=fake.unique.ssn(),
                name=fake.name(),
                email=fake.email(),
                password=fake.password(),
                no_phone=fake.phone_number(),
                files_link=fake.url(),
            )

        # Seed Templates
        for _ in range(10):
            Template.objects.create(
                template_name=fake.company(),
                image_link=fake.image_url(),
                demo_link=fake.url(),
            )

        # Seed Hosting
        for _ in range(5):
            Hosting.objects.create(
                type_hosting=fake.domain_word(),
                price=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
            )

        users = list(User.objects.all())
        templates = list(Template.objects.all())
        hostings = list(Hosting.objects.all())

        # Seed Orders
        for _ in range(20):
            Order.objects.create(
                domain_name=fake.domain_name(),
                payment_status=fake.random_element(elements=('Pending', 'Completed', 'Failed')),
                id_user=fake.random_element(elements=users),
                id_template=fake.random_element(elements=templates),
                id_hosting=fake.random_element(elements=hostings),
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
