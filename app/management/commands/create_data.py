from app.models import Interest, Skill
from main.models import Post, Profile
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'This command creates some data'

    def handle(self, *args, **options):

        if not Interest.objects.filter(name="Information Technology").exists():

            Interest.objects.create(
                name="Information Technology",
                description="Information Technology")

        if not Interest.objects.filter(name="Programming").exists():

            Interest.objects.create(
                name="Programming",
                description="Programming")

        if not Skill.objects.filter(name="Java").exists():

            Skill.objects.create(
                name="Java",
                description="Java",)

        if not Skill.objects.filter(name="Python").exists():

            Skill.objects.create(
                name="Python",
                description="Python")

        if not Skill.objects.filter(name="Django").exists():

            Skill.objects.create(name="Django",
                                 description="Django",)

        if not Profile.objects.filter(user="nicko_b").exists():

            Profile.objects.create(
                user="nicko_b",
                fullname="Maksat Hemdemow",
                email="thehighestintheroom00@gmail.com",
                bio="Big Boy")

        if not Post.objects.filter(title="Python").exists():

            Post.objects.create(
                title="Python",
                description="Python",
                source_link="https://www.python.org/",
                body="Python is the best programming language",
                author=Profile.objects.get(user="nicko_b"),)
