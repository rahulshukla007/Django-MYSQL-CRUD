from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employees
# Create your views here.

def home(request):
    if request.method == "POST":
        #the variable equal to the Employee database in models.py
        emp = Employees()

        #Getting Data from HTML Form
        emp.eid      = request.POST.get('eid')
        emp.ename    = request.POST.get('ename')
        emp.eemail   = request.POST.get('email')
        emp.econtact = request.POST.get('contact')

        #Saving data into database
        emp.save()

        #it will redirect to home urls
        return redirect("/")
    else:
        print('not a post request, it will redirect to form page')
    return render(request, 'djmysql/index.html')


#Getting data from database & showing in table
def show(request):
    employeedata = Employees.objects.all()
    return render(request, 'djmysql/show.html',{'employeedata':employeedata})

#Getting edit request with id
def edit(request,id):
    print(id)                  #model_id = get_id
    edit_emp = Employees.objects.get(id=id)
    return render(request, 'djmysql/edit.html',{"edit_emp": edit_emp})

def update(request,id):
    #Opening Existing Employees object with the help of id
    update_emp = Employees.objects.get(id=id)

    # Getting Updated Data from edit HTML & Updating Employee objects
    update_emp.eid      = request.POST.get('eid')
    update_emp.ename    = request.POST.get('ename')
    update_emp.eemail   = request.POST.get('email')
    update_emp.econtact = request.POST.get('contact')

    # Saving data into database
    update_emp.save()
    return redirect('/show')


#Getting delete request with id
def delete(request,id):
    #Opening Existing Employees object with the help of id
    delete_emp = Employees.objects.get(id=id)

    #Deleting data into database
    delete_emp.delete()
    return redirect('/show')