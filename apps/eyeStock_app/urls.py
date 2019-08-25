from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^registration$',views.registration),
    url(r'^dashboard$',views.dashboard),
    url(r'^login$',views.login),
    url(r'^process_login$',views.process_login),
    url(r'^checkout$',views.checkout),
    url(r'^products$',views.products),
    url(r'^add_product$',views.add_product),
    url(r'^edit_product/(?P<product_id>\d+)$',views.edit_product),
    url(r'^add_vehicle$',views.add_vehicle),
    url(r'^employee_form$',views.employee_form),
    url(r'^add_employee$',views.add_employee),
    url(r'^employee_list$',views.employee_list),
    url(r'^employee_info/(?P<employee_id>\d+)$',views.employee_info),
    url(r'^logout$',views.logout),
    url(r'^delete_product/(?P<product_id>\d+)$',views.delete_product),
    url(r'^delete_vehicle/(?P<vehicle_id>\d+)$',views.delete_vehicle),
    url(r'^delete_employee/(?P<employee_id>\d+)$',views.delete_employee)

]