# api-challenge-python

Implement RESTful API's in Django framework to pass the tests.
Specifications are defined in [tests files](/app/api/tests.py)

Database details 
- [Users Model](/app/api/models.py)

Settings can be modified [here](/app/settings.py)

The goal of this challenge is to implement following API's
1. Create a basic login API with session
    - Signup
    - Login
    - Logout
2. Profile API
    - Allow signedUp/registered user to edit details i.e update profile (username, password, birthday, company, location)
    Note: email id is unique and cannot be changed.
3. Follow/Unfollow API
    - A user can follow another user and vice versa

You can use [Comments.md](comments.md) for any kind of notes, for example
- Personal notes or problems
- Information on how your code works
- Any suggestions on what should be changed in the specifications.