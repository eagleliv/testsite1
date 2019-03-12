from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Boss_Form, Employee_Data_Form, PassForm, PassValForm
from .models import Boss, Employee_data
from django_seed import Seed
import datetime
from django.contrib.auth import login, get_user, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate

if Employee_data.objects.all().count() != 500:
    seeder = Seed.seeder()
    seeder.add_entity(Boss, 10)
    seeder.add_entity(Employee_data, 500)
    seeder.execute()

class Employee(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request):
        person_data = {}
        boss = Boss.objects.all()
        for i in boss:
            employee = i.boss.all()
            person_data[i] = employee
        return render(request, 'mainpage/mainpage1.html', context = {'person_data': person_data})

    def post(self, request):
        person_data = {}
        select = request.POST['select']
        if select == 'Boss name':
            boss = Boss.objects.all().order_by('boss_name')
        else:
            boss = Boss.objects.all()
        for i in boss:
            if select == 'Date':
                employee = i.boss.all().order_by('employee_date')
            elif select == 'Boss name':
                employee = i.boss.all()
            else:
                employee = i.boss.all().order_by(select.lower())
            person_data[i] = employee
        return render(request, 'mainpage/mainpage1.html', context = {'person_data': person_data})

class Person(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request, pk):
        person = Employee_data.objects.filter(pk = pk)
        return render(request, 'mainpage/person.html', context = {'person': person})

    def post(self, request, pk):
        person = Employee_data.objects.get(pk=pk)
        person.delete()
        return redirect ('/main/')

class Search(LoginRequiredMixin, View):
    raise_exception = True
    def post(self, request):
        boss = ''
        filter_by = {}
        search_by = {'surname__icontains': request.POST['bysurname'].strip(), 'position__icontains': request.POST['byposition'].strip(), 'salary': request.POST['bysalary'].strip(), 'employee_date': request.POST['bydateofemployement']}
        if request.POST['bybossname'].strip():
            search_data = Employee_data.objects.filter(boss__boss_name__icontains=request.POST['bybossname'])
        else:
            for key, value in search_by.items():
                if value:
                    print(key, value)
                    filter_by[key] = search_by[key]
                    search_data = Employee_data.objects.filter(**filter_by)
        return render(request, 'mainpage/person.html', context = {'person': search_data})

def passlogout(request):
    logout(request)
    return redirect('/')

class Loginpage(FormView):
    def get(self, request):
        if get_user(request).is_authenticated:
            return redirect('/main/')
        else:
            form = PassValForm() #AuthenticationForm()
            return render(request, 'mainpage/login.html', context={'form': form})
    def post(self, request):
        form = PassValForm(None, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/main/')
        return render(request, 'mainpage/login.html', context={'form': form})

class Registerpage(FormView):
    def get(self, request):
        form = PassForm()
        return render(request, 'mainpage/register.html', context={'form': form})
    def post(self, request):
        form = PassForm(request.POST)
        if form.is_valid():
            form.save()
            user_n = form.cleaned_data.get('username')
            user_p = form.cleaned_data.get('password1')
            user = authenticate(username = user_n, password = user_p)
            login(request, user)
            return redirect('/main/')
        return render(request, 'mainpage/register.html', context={'form': form})

class Editperson(LoginRequiredMixin, FormView):
    raise_exception = True
    def get(self, request, pk):
        person = Employee_data.objects.get(pk = pk)
        boss = Boss.objects.all()
        form_person = Employee_Data_Form(instance = person)
        return render(request, 'mainpage/editperson.html', context = {'form': form_person, 'person': person, 'boss': boss})
    def post(self, request, pk):
        person = Employee_data.objects.get(pk = pk)
        form_person = Employee_Data_Form(request.POST, request.FILES, instance = person)
        if form_person.is_valid():
            form_person.save()
            return redirect('person', pk = person.id)
        return render(request, 'mainpage/editperson.html', context = {'form': form_person, 'person': person})

class Createperson(LoginRequiredMixin, FormView):
    raise_exception = True
    def get(self, request):
        form_create_person = Employee_Data_Form()
        form_create_boss = Boss_Form()
        return render(request, 'mainpage/createperson.html', context = {'form_create_person': form_create_person, 'form_create_boss': form_create_boss})
    def post(self, request):
        form_create_person = Employee_Data_Form(request.POST, request.FILES)
        form_create_boss = Boss_Form(request.POST)
        if form_create_person.is_valid() and form_create_boss.is_valid():
            new_boss, _ = Boss.objects.get_or_create(boss_name = form_create_boss.cleaned_data['boss_name'], boss_position = form_create_boss.cleaned_data['boss_position'])
            new_person = Employee_data.objects.create(boss = new_boss,
            name = form_create_person.cleaned_data['name'],
            surname = form_create_person.cleaned_data['surname'],
            patronimyc = form_create_person.cleaned_data['patronimyc'],
            position = form_create_person.cleaned_data['position'],
            employee_date = form_create_person.cleaned_data['employee_date'],
            salary = form_create_person.cleaned_data['salary'],
            employee_image = request.FILES['employee_image'])
            print(request.FILES)
            return redirect('person', pk = new_person.id)

        return render(request, 'mainpage/createperson.html', context = {'form_create_person': form_create_person, 'form_create_boss': form_create_boss})
