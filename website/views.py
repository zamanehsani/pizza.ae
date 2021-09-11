from dashboard.forms import OrderForm
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from dashboard import models
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView


class Menu(ListView):
    model = models.Menu_category
    template_name = "website/menu.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Menu, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'menu'
        return data

class LandingPage(TemplateView):
    template_name = "website/LandingPage.html"

    def get_context_data(self, *args, **kwargs):
        data = super(LandingPage, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'PIZZA.AE'
        return data


# login page
class LoginCustomerView(TemplateView):
    template_name = "website/login_customer.html"

    def get_context_data(self, *args, **kwargs):
        data = super(LoginCustomerView, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Login'
        return data


# sign up page
class Sign_up_CustomerView(TemplateView):
    template_name = "website/sign_up_customer.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Sign_up_CustomerView, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Sign up'
        return data


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class CartView(TemplateView):
    template_name = "website/cart_view.html"

    def get_context_data(self, *args, **kwargs):
        data = super(CartView, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Cart'
        return data

    def post(self, request, *args, **kwargs):
        name_order = request.POST.get('name')
        number_order = request.POST.get('number')
        location_order = request.POST.get('location')
        address_order = request.POST.get('address') +" - " +request.POST.get('address2')
        payment_order = request.POST.get('payment')
        note_order = request.POST.get('note')

        if request.POST.get('area') == 'false':
            print("area is false, make the first area by default")
            area_order = models.Areas.objects.first()
        else:
            print("area is not false, geting the area of tha area number")
            area_order = get_object_or_404(models.Areas, pk = int(request.POST.get('area')))


        order_obj = models.Order(
                name = name_order, 
                number = int(number_order), 
                location = location_order, 
                status = 'ordered',
                address = address_order,
                area = area_order,
                payment_method = payment_order,
                description = note_order)

        order_obj.save()

        print("daved")
        
        import json
        order = request.POST.get('order').split(';')
        for i in order:
            item = json.loads(i)
            menu_item_obj = get_object_or_404(models.Menu ,pk = int(item['id']))
            order_item = models.Order_items(order = order_obj, menu_item = menu_item_obj, quantity = int(item['quantity']))
            order_item.save()
            print(order_item, order_item.quantity)

        return JsonResponse(order_obj.pk, safe=False)