from django.db import models


class Boss(models.Model):
    boss_name = models.CharField(max_length = 30)
    boss_position = models.CharField(max_length = 30, null = True)
    def __str__(self):
        return self.boss_name

class Employee_data(models.Model):
    boss = models.ForeignKey(Boss, related_name = 'boss', on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)
    patronimyc = models.CharField(max_length = 60)
    position = models.CharField(max_length = 60)
    employee_date = models.DateField(auto_now = False, auto_now_add = False)
    salary = models.PositiveIntegerField(null = True, default = 0)
    employee_image = models.ImageField(blank=True, upload_to='images')
    def __str__(self):
        return self.name

# Create your models here.
