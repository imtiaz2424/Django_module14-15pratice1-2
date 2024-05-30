from django.db import models

# Create your models here.
class FirstApp(models.Model):
    auto_field = models.AutoField(primary_key=True, default='1')
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # char_field = models.CharField(max_length=255)
    # date_field = models.DateField()
    # date_time_field = models.DateTimeField()
    # decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    
    
    


    def __str__(self):
        return f"auto_field : {self.auto_field} - {self.name}"