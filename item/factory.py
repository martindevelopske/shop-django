# Import necessary modules and your UserFactory
from datetime import datetime
import factory
from django.contrib.auth.models import User

# Define your UserFactory class
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.username).lower())
    password = factory.Faker('password')
    date_joined = factory.LazyFunction(datetime.now)

# Run the factory to create instances
if __name__ == '__main__':
    # Use the create() method to create a single instance
    user_instance = UserFactory.create()

    # Alternatively, use the create_batch() method to create multiple instances
    user_instances = UserFactory.create_batch(5)

    # Print information about the created instances
    print("Single instance created:", user_instance)
    print("Multiple instances created:", user_instances)
