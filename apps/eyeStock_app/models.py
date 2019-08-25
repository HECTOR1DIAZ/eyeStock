from __future__ import unicode_literals
from django.db import models


# Create your models here.
class UserManager(models.Manager):
    def company_validator(self,postData):
        errors = {}
        if len(postData["name"]) == 0:
            errors["name_comp"] = "Enter company's name"
        if len(postData["address"]) == 0:
            errors["address"] = "Address is requiered!"
        if len(postData["email"]) == 0:
            errors["email"] = "Email is requiered!"
        elif len(Company.objects.filter(email = postData['email'])) > 0:
            errors['reg_email'] = "Email already exist, please Log In"
        if len(postData["password"]) == 0:
            errors["password"] = "Password is requiered!"
        elif len(postData["password"]) < 8:
            errors["short_pw"] = "Password has to be greater than 8 characters!"
        elif postData["password"] != postData["confirm_pw"]:
            errors["confirm_pw"] = "Password does not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(postData["email"]) == 0:
            errors["email_log"] = "Please enter email"
        if len(Company.objects.filter(email = postData['email'])) == 0:
            errors['invalid_e'] = "Email doesnt exist." 
        return errors
    
    def vehicle_validator(self,postData):
        errors = {}
        if len(postData['vin']) == 0:
            errors['vin'] = "Vehicle Identification number is needed."
        if len(postData['stock_number']) == 0:
            errors['stock_number'] = "Stock Number is needed."
        elif len(Vehicle.objects.filter(vin = postData['vin'])) > 0:
            errors['dup_vin'] = "The Vehicle Identification Number is already in system."
        elif len(Vehicle.objects.filter(stock_number = postData['stock_number'])) > 0:
            errors['dup_stock_number'] = "The stock number is already in the system."

    

class Company(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    
class Employee(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    employee_address = models.EmailField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    employee_email = models.EmailField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    product_name = models.CharField(max_length = 255)
    barcode_number = models.CharField(max_length = 255)
    employees_p = models.ForeignKey(Employee, related_name ="products",on_delete=models.CASCADE, null = True)
    description = models.TextField()
    quantity = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Vehicle (models.Model):
    year = models.IntegerField(max_length = 4)
    make = models.CharField(max_length = 255)
    model = models.CharField(max_length = 255)
    vin = models.CharField(max_length = 17)
    employees_v = models.ForeignKey(Employee, related_name="vehicles",on_delete=models.CASCADE, null = True)
    stock_number = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
