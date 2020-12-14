from django.db import models

# Create your models here.
# creating model class = table in data base
# creating model fields = columns in data base
class job(models.Model): # table

    # adding title field
    title = models.CharField(max_length=100) # coulmn 

    # job type choices 
    JobType = (
        ('full time','full time'),
        ('part time','part time'),
    )
    # adding job type field
    job_type = models.CharField(choices =JobType , max_length=15)
    
    #adding description field 
    description = models.TextField(max_length=1000)

    #adding published at field 
    published_at = models.DateTimeField(auto_now=True)
    
    #adding vacancy field 
    vacancy = models.IntegerField(default=1)

    #adding salary field 
    salary = models.IntegerField(default=0)

    #adding experince field
    experince = models.IntegerField(default=1) 

    
    def __str__(self):
        return self.title
        