from django.db import models

# Create your models here.
class MainMenu(models.Model):
    name = models.CharField(default="" , max_length=25)
    url = models.CharField(default="" , max_length=25)
    permissions = models.CharField(default="" , max_length=25)
    icon_class = models.CharField(default="" , max_length=25)
    has_submenu = models.IntegerField(default=None)

    def __str__(self):
        return '%s' % self.name

class SubMenu(models.Model):
    name = models.CharField(default="" , max_length=25)
    mainmenu = models.ForeignKey(MainMenu, on_delete=models.CASCADE , default=None)
    url = models.CharField(default="" , max_length=25)
    permissions = models.CharField(default="" , max_length=25)
    icon_class = models.CharField(default="" , max_length=25)
   