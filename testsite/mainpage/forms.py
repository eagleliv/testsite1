from django import forms
from .models import Boss, Employee_data
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class Boss_Form(forms.ModelForm):
    class Meta:
        model = Boss
        fields = ['boss_name', 'boss_position']
        help_texts = {
            'boss_name': 'Boss name',
            'boss_position': 'Boss position',
        }
    def __init__(self, *args, **kwargs):
        super(Boss_Form, self).__init__(*args, **kwargs)

        self.fields['boss_name'].widget.attrs['class'] = 'form-control mr-sm-2'
        self.fields['boss_position'].widget.attrs['class'] = 'form-control mr-sm-2'

        self.fields['boss_name'].widget.attrs['placeholder'] = 'enter Boss name'
        self.fields['boss_position'].widget.attrs['placeholder'] = 'enter Boss position'

class Employee_Data_Form(forms.ModelForm):
    class Meta:
        model = Employee_data
        fields = ['surname', 'name', 'patronimyc', 'position', 'employee_date', 'salary', 'employee_image']
        help_texts = {
            'surname': 'Employee surname',
            'name': 'Employee name',
            'patronimyc': 'Employee patronimyc',
            'position': 'Employee position',
            'employee_date': 'Date of employee',
            'salary': 'Employee salary'
        }
    def __init__(self, *args, **kwargs):
        super(Employee_Data_Form, self).__init__(*args, **kwargs)

        self.fields['surname'].widget.attrs['class'] = 'form-control mr-sm-2'
        self.fields['position'].widget.attrs['class'] = 'form-control mr-sm-2'
        self.fields['employee_date'].widget.attrs['class'] = 'form-control mr-sm-2'
        self.fields['salary'].widget.attrs['class'] = 'form-control mr-sm-2'
        self.fields['name'].widget.attrs['class'] = 'form-control mr-sm-2'
        self.fields['patronimyc'].widget.attrs['class'] = 'form-control mr-sm-2'
        self.fields['employee_image'].widget.attrs['class'] = 'form-control mr-sm-2'

        self.fields['surname'].widget.attrs['placeholder'] = 'enter Surname'
        self.fields['name'].widget.attrs['placeholder'] = 'enter Name'
        self.fields['patronimyc'].widget.attrs['placeholder'] = 'enter Patronimyc'
        self.fields['position'].widget.attrs['placeholder'] = 'enter Position'
        self.fields['employee_date'].widget.attrs['placeholder'] = 'enter Date of employement'
        self.fields['salary'].widget.attrs['placeholder'] = 'enter Salary'

        self.fields['employee_date'].widget.attrs['type'] = 'date'

class PassForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(PassForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat password'

class PassValForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(PassValForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
