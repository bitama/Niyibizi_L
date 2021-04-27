from django.db import models
from login_app.models import User
from datetime import datetime

class TripManager(models.Manager):
    def validator(self,post_data):
        errors={}
        
        if len(post_data["destination"]) < 3:
            errors["destination"] = "Destination must be at least 3 characters."
            
        if len(post_data["plan"]) < 3:
            errors["plan"] = "Plan must be at least 3 characters."
            
        if post_data["start_date"]== "":
            errors["date_errors"] = "Please provide a start_date"
        else:
            today = datetime.now()
            start_date = datetime.strptime(post_data["start_date"], "%Y-%m-%d")
            if start_date < today:
                errors["start_date"] ="show_date must be in the future"
        
        if post_data["end_date"] == "":
            errors["end_date_errors"] = "Please provide an end_date"
        else:
            today = datetime.now()
            end_date = datetime.strptime(post_data["end_date"], "%Y-%m-%d")
            if end_date < today:
                errors["end_date"] ="End_date must be in the future"
                
        return errors

class Trip(models.Model):
    destination= models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    plan= models.TextField(max_length=500)
    user= models.ForeignKey(User,related_name="trips",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=TripManager()
    
