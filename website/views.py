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
        data['page_title'] = ' '
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
        address_order = request.POST.get('address') +" , " +request.POST.get('address2')
        payment_order = request.POST.get('payment')
        note_order = request.POST.get('description')

        order_obj = models.Order(
                name = name_order, 
                number = int(number_order), 
                location = location_order, 
                status = 'ordered',
                address = address_order,
                payment_method = payment_order,
                description = note_order,
                order_source = 'online')

        order_obj.save()

        # send sms here
        from dashboard.requests import sendsms
        # send a notification to the owner
        text = f'your order with ID of {order_obj.pk} had been placed.'
        sendsms(text, order_obj.number)

        # update the order it no area
        if request.POST.get('area') != 'false':
            print("area has been selected", request.POST.get('area'))
            order_obj.area = get_object_or_404(models.Areas, pk = int(request.POST.get('area')))
            order_obj.save()
        
        import json
        order = request.POST.get('order').split(';')
        for i in order:
            item = json.loads(i)
            menu_item_obj = get_object_or_404(models.Menu ,pk = int(item['id']))
            order_item = models.Order_items(order = order_obj, menu_item = menu_item_obj, quantity = int(item['quantity']))
            order_item.save()

        return JsonResponse(order_obj.pk, safe=False)

# order tracking
class TrackOrder(DeleteView):
    model = models.Order
    template_name = "website/track_order.html"

    def get_context_data(self, *args, **kwargs):
        data = super(TrackOrder, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Track Order'
        return data

class Dine_Menu(ListView):
    model = models.Menu_category
    template_name = "website/menu_dine.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Dine_Menu, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'DINE IN'
        return data


@method_decorator(csrf_exempt, name='dispatch')
class Dine_CartView(TemplateView):
    template_name = "website/dine_in_cart_view.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Dine_CartView, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'DINE IN'
        return data

    def post(self, request, *args, **kwargs):
        print(request.POST)

        # get the db to cloud, 
        #
        order_obj = models.Order(name="dine-in", status = 'ordered', order_source = 'dine-in')

        order_obj.save()
        import json
        order = request.POST.get('order').split(';')
        for i in order:
            item = json.loads(i)
            menu_item_obj = get_object_or_404(models.Menu ,pk = int(item['id']))
            order_item = models.Order_items(order = order_obj, menu_item = menu_item_obj, quantity = int(item['quantity']))
            order_item.save()

        return JsonResponse(1, safe=False)

