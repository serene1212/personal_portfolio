from django.db import models

from utils.base_model import BaseModel


class Sender(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta(BaseModel.Meta):
        abstract = True


class Message(Sender):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"{self.email} {self.title}"
