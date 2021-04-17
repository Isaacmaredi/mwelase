from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    
    
    NOT_STARTED='NS'
    IN_PROGRESS_DELAYED='IPD'
    IN_PROGRESS_ON_TRACK ='IPO'
    TERMINATED='TM'
    COMPLETED='CM'
    
    project_status = [ 
    ('NOT_STARTED','Not Started'),
    ('IN_PROGRESS_DELAYED','Delayed'),
    ('IN_PROGRESS_ON_TRACK','On Track'),
    ('TERMINATED','Terminated'),
    ('COMPLETED','Completed')
    ]

    construction_type =[
    ('CC', 'Civil Construction'),
    ('BC','Building Construction'),
    ('RW','Renovations'),
    ]
    
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    category=models.CharField(max_length=30, choices=construction_type,default='Civil Construction')
    description = models.TextField()
    client = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=30, choices=project_status, default='NS')
    progress_indicator=models.IntegerField()
    status_date=models.DateField(auto_now_add=False, default=None, blank=True,null=True)
    image = models.ImageField(default='images/ewc.jpg', upload_to='project_photos/%Y/%m/', blank=True)
    value = models.FloatField()
    
    def __str__(self):
        return f'{self.description} for {self.client}'
    
class Gallery(models.Model):
    picture = models.ImageField(default='images/build5.jpg', upload_to='gallery_photos/%Y/%m/', blank=False, null=False)
    description=models.CharField(max_length=300)
    place=models.CharField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.description} at {self.place}'
    
    
    
    
    
    
    
    
    