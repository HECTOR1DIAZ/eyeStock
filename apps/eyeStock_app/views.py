from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def welcome(request):
        return redirect("/login")

def registration(request):
        errors = Company.objects.company_validator(request.POST)
        if len(errors) > 0:
                for key, value in errors.items():
                        messages.error(request,value)
                return redirect('/')
        else:
                hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
                Company.objects.create(name=request.POST["name"],address=request.POST['address'],email=request.POST['email'],password=hash1.decode())
                company= Company.objects.last()
                request.session['company_id']= company.id
                return redirect('/dashboard')

def dashboard(request):
        # if 'user_id' not in request.session:
        #         return redirect('/')
        # else: 
                products = Product.objects.all()
                vehicles = Vehicle.objects.all()
                context = {
                        'products': products,
                        'vehicles': vehicles
                }
                return render(request, "eyeStock_app/dashboard.html", context)

def login(request):
        return render(request, "eyeStock_app/login.html")

def process_login(request):
        errors = Company.objects.login_validator(request.POST)
        if len(errors) > 0:
                for key, value in errors.items():
                        messages.error(request, value)
                return redirect('/')
        else:
                company_list = Company.objects.filter(email=request.POST['email'])
                if bcrypt.checkpw(request.POST['password'].encode(),company_list[0].password.encode()):
                        request.session['company_id'] = company_list[0].id
                        return redirect('/dashboard')

def checkout(request):
        products = Product.objects.all()
        employees = Employee.objects.all()
        context = {

                'products' : products,
                'employees' : employees,
        }
        return render(request, 'eyeStock_app/product_checkout.html', context)

def products(request):
        if 'product_name' in request.GET:
                product_name = request.GET['product_name']
        else:
                product_name = ""
        if 'barcode' in request.GET:
                barcode = request.GET['barcode']
        else:
                barcode = ""
        if 'description' in request.GET:
                description = request.GET['description']
        else:
                description = ""

        context = {
                'product_name': product_name,
                'barcode': barcode,
                'description': description
        }
        return render(request, "eyeStock_app/products.html", context)

def add_product(request):
        if 'product_name' not in request.POST:
                return redirect('/dashboard')
        Product.objects.create(
                product_name = request.POST['product_name'], 
                barcode_number= request.POST['barcode_number'],
                description = request.POST ['description'],
                quantity = request.POST['quantity']
                )
        return redirect('/dashboard')

def edit_product(request, product_id):
        return render(request, "eyeStock_app/edit_product.html")

def process_edit_product(request, product_id):
        product= Product.objects.get(id=show_id)
        product.product_name = request.POST['product_name']
        product.description = request.POST['description']
        product.save()
        context = {
                'product':product,
                'product.product_name': product.product_name,
                'product.description': productct.description,
        }

        return render(f"/edit_product/{product.id}", context)

def add_vehicle(request):
        errors = Company.objects.vehicle_validator(request.POST)
        if len(errors) > 0:
                for key, value in errors.items():
                        messages.error(request, value)
                return redirect('/')
        else:
                Vehicle.objects.create(
                        year = request.POST['year'],
                        make = request.POST['make'],
                        model = request.POST['model'],
                        vin = request.POST['vin'],
                        stock_number = request.POST['stock_number']
                )
                vehicle = Vehicle.objects.last()
                context = {
                        'vehicle':vehicle,
                }
                return redirect('/dashboard', context)

def employee_form(request):
        return render(request, "eyeStock_app/employee_form.html")

def add_employee(request):
        Employee.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST ['last_name'],
                employee_address = request.POST['employee_address'],
                phone_number = request.POST['phone_number'],
                employee_email = request.POST ['employee_email']
        )
        employee = Employee.objects.last()
        request.session['employee_id'] = employee.id
        return redirect('/employee_list')

def employee_list(request,):
        employees = Employee.objects.all()
        context ={
                'employees':employees,
        }
        return render(request, "eyeStock_app/employee_list.html", context)

def employee_info(request, employee_id):
        employee = Employee.objects.get(id=employee_id)
        context ={
                'employee':employee,
        }      
        return render(request,'eyeStock_app/employee_info.html', context)

def delete_employee(request, employee_id):
    delete_employee =Employee.objects.get(id=employee_id)
    delete_employee.delete()
    context = {
        'delete_employee': delete_employee,
    }
    return redirect('/dashboard', context)

def delete_product(request, product_id):
    delete_product =Product.objects.get(id=product_id)
    delete_product.delete()
    context = {
        'delete_product': delete_product,
    }
    return redirect('/dashboard', context)

def delete_vehicle(request, vehicle_id):
    delete_vehicle =Vehicle.objects.get(id=vehicle_id)
    delete_vehicle.delete()
    context = {
        'delete_vehicle': delete_vehicle,
    }
    return redirect('/dashboard', context)

def logout(request):
        request.session.clear()
        return redirect('/')