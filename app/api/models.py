from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)
    company = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.name, self.email, self.birthday, self.company, self.location)

# from passlib.hash import pbkdf2_sha256
# hash = pbkdf2_sha256.encrypt("password", rounds=8000, salt_size=10)
# hash = $pbkdf2-sha256$8000$HaPUeu99L4VQKg$TmNh1N7/aQkkfVE1902sHc0uBHzwuVEUrMW3q5oiZwg
# u = Users(username="user1", password=hash,email="user1@test.com",birthday="1991-04-17",company="company1",location="location1")
# u.save()
# u = Users(username="user2", password=hash,email="user2@test.com",birthday="1989-04-17",company="company2",location="location2")
# u.save()
# u = Users(username="user3", password=hash,email="user3@test.com",birthday="1995-04-17",company="company3",location="location1")
# u.save()
# u = Users(username="user4", password=hash,email="user4@test.com",birthday="1987-04-17",company="company2",location="location1")
# u.save()
# u = Users(username="user5", password=hash,email="user5@test.com",birthday="1999-04-17",company="company2",location="location2")
# u.save()
# u = Users(username="user6", password=hash,email="user6@test.com",birthday="1994-04-17",company="company1",location="location2")
# u.save()