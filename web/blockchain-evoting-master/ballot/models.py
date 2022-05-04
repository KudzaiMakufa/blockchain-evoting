from django.db import models
from django.core.validators import FileExtensionValidator


class Candidate(models.Model):


    name = models.CharField(default="" , max_length=25)
    surname = models.CharField(default="" , max_length=25)
    national_id = models.CharField(default="" , max_length=25)
    address = models.CharField(default="" , max_length=25)
    photo = models.FileField(upload_to="uploads/" ,validators=[FileExtensionValidator(allowed_extensions=['jpg','png' ,'jpeg'])])
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
  

   