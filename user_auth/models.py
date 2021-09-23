from django.contrib.auth.models import User
from django.db import models


class UserInput(models.Model):
    input = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def user_id(self):
        return self.user.id

