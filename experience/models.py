from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    
    class Meta:
        ordering = ['-start_date']
        
    def __str__(self):
        return f"{self.role} at {self.company}"
