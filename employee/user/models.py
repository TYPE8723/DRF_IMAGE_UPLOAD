from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class Employee(models.Model):
    def validate_image(img_data):#validating image size
        datasize = img_data.file.size
        megabyte_limit = 5.0
        if datasize > megabyte_limit*1024*1024:
            raise ValidationError(f"File size exceded.max size is {megabyte_limit}mb")
    name = models.CharField(max_length=50,null=False,help_text="name of the User")
    email = models.CharField(max_length=100,null=False,unique=True,validators=[EmailValidator()],help_text="Email of the user")
    photo = models.ImageField(upload_to ='static/user/',blank=True,null=True,validators=[validate_image])
    
    def __str__(self) -> str:
        return f"{self.email}"