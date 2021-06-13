from django.db import models

# Create your models here.
class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)  # set to true after datatable population

    def __str__(self):
        return 'File id: ' + str(self.id)