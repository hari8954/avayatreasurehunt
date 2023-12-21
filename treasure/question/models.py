from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self) -> str:
        return f"{self.question}"

class Clue(models.Model):
    teamName=models.CharField(blank=True,null=True,max_length=100)
    clue=models.CharField(max_length=100)
    assigned=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.teamName} : {self.clue}"