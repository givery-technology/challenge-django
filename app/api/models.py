from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)
    company = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.username, self.email, self.birthday, self.company, self.location)

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

class Followers(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='followers_user_followed')        # User who is followed
    followed_by_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='followers_follower')    # User one who following 
    followed_at = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user_id', 'followed_by_id')

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.user_id.id, self.followed_by_id.id, self.followed_at)    

# user = Users.objects.get(id=1)
# follower = Users.objects.get(id=2)
# f = Followers(user_id=user, followed_by_id=follower)
# f.save()
# user = Users.objects.get(id=1)
# follower = Users.objects.get(id=3)
# f = Followers(user_id=user, followed_by_id=follower)
# f.save()
# user = Users.objects.get(id=1)
# follower = Users.objects.get(id=4)
# f = Followers(user_id=user, followed_by_id=follower)
# f.save()
# user = Users.objects.get(id=1)
# follower = Users.objects.get(id=5)
# f = Followers(user_id=user, followed_by_id=follower)
# f.save()
# user = Users.objects.get(id=1)
# follower = Users.objects.get(id=6)
# f = Followers(user_id=user, followed_by_id=follower)
# f.save()
# user = Users.objects.get(id=2)
# follower = Users.objects.get(id=1)
# f = Followers(user_id=user, followed_by_id=follower)
# f.save()
# user = Users.objects.get(id=2)
# follower = Users.objects.get(id=3)
# f = Followers(user_id=user, followed_by_id=follower)
# f.save()





