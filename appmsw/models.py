from django.db import models
from django.contrib.auth.models import User
#from django.utils.translation import ugettext_lazy as _  replace to gettext_lazy
#https://stackoverflow.com/questions/70656495/importerror-cannot-import-name-ugettext-lazy
from django.utils.translation import gettext_lazy as _

categorys = [
    ("systems", "Systems Parameters Integrations"),
    ("app", "Application Parameters"),
    ("sidemenu", "Side Menu"),
    ("topmenu", "Top Menu"),
    ("prj", "Project"),
]

class Param(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=categorys, default='app')
    desc = models.CharField(max_length=1000, default = '')
    option = models.CharField(max_length=1000, default='')
    json = models.TextField(max_length=75000, default='')
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True)
    public=models.BooleanField(default=True)
    enabled=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name},{self.category},{self.desc}, {self.json}"
 
    def __repr__(self):
        return f"{self.name}, {self.category},{self.desc}"

class Comment(models.Model):
   text = models.TextField(max_length=2000)
   creation_date = models.DateTimeField(auto_now=True)
   author = models.ForeignKey(to=User, on_delete=models.CASCADE)
   param = models.ForeignKey(to=Param, on_delete=models.CASCADE, related_name='comments')

   def __str__(self):
        return f"{self.text}, {self.author}"


