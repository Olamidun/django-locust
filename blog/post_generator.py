from faker import Faker
from faker.providers import DynamicProvider
from django.contrib.auth.models import User

from .models import Post, Comment

fake = Faker()

user = User.objects.get(pk=1)

def generate_post():
    body = [Post(title=f"title {_ + 2150}", body=fake.text(), user=user) for _ in range(10000)]

    Post.objects.bulk_create(body)
    print("Done")


def generate_comment():

    body = [Comment(post=Post.objects.get(pk= _ + 400), body=fake.text(), user=user) for _ in range(500)]

    Comment.objects.bulk_create(body)
    print("Done")



# now you can use:

# 'dr.'