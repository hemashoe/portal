from app.models import Interest, Skill
from authentication.models import User
from main.models import Comment, Post, Profile, News

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'This command creates some data'

    def handle(self, *args, **options):
        
        if not Interest.objects.filter(
            name="Information Technology").exists():
        
            Interest.objects.create(
                name="Information Technology",
                description="Information Technology"
                )
        
        if not Interest.objects.filter(
            name="Programming").exists():

            Interest.objects.create(
                name="Programming",
                description="Programming"
                )        

        if not Skill.objects.filter(
            name="Java").exists():

            Skill.objects.create(
                name="Java",
                description="Java",)
        
        if not Skill.objects.filter(
            name="Python").exists():

            Skill.objects.create(
                name="Python",
                description="Python")

        if not Skill.objects.filter(
            name="Django").exists():

            Skill.objects.create(name="Django",
            description="Django",)

        if not Profile.objects.filter(
            user="andrey_petrovich").exists():

            Profile.objects.create(
                user="andrey_petrovich",
                fullname="Andrey Petrowich",
                email="andrey.petrowich@gmail.com",
                bio="I am a programmer")
        
        if not Profile.objects.filter(
            user="aman_aman").exists():
        
            Profile.objects.create(
                user="aman_aman",
                fullname="Aman Man",
                email="aman.aman@gmail.com",
                bio="I am a programmer")
        
        
        if not Post.objects.filter(
            title="Python").exists():

            Post.objects.create(
                title="Python",
                description="Python",
                source_link="https://www.python.org/",
                body="Python is the best programming language",
                author=Profile.objects.get(user="andrey_petrovich"),)
        
        if not News.objects.filter(
            title="Python").exists():

            News.objects.create(
                title="Python",
                description="Python",
                source_link="https://www.python.org/",
                body="Python is the best programming language",
                author=Profile.objects.get(user="aman_aman"),)