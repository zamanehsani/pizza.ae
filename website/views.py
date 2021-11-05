import decimal
import random
from django.db.models.query import QuerySet

from requests.api import get, request
from dashboard.forms import OrderForm
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from dashboard import models
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView


class Menu(ListView):
    model = models.Menu_category
    template_name = "website/menu.html"
    ordering = ['sort']
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
        address_order = request.POST.get('address')
        payment_order = request.POST.get('payment')

        order_obj = models.Order(
                name = name_order, number = int(number_order), 
                location = location_order, status = 'ordered',
                address = address_order, payment_method = payment_order,
                order_source = 'online')
        order_obj.save()

        # send sms here
        if request.POST.get('sms'):
            from dashboard.requests import sendsms
            # send a notification to the owner
            text = "THANK YOU FOR ORDERING WITH US. your order had been placed. we will call you once the order arrive."
            sendsms(text, order_obj.number)

        # update the order it no area
        if request.POST.get('area'):
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


class Order_cart(TemplateView):
    template_name = "website/order_cart.html"
    def post(self, request,*args, **kwargs):
        # if the post request has otp_validation in it, it means that otp post form is being submitted
        if "otp_validation" in request.POST:
            otp = get_object_or_404(models.OTP, pk = request.POST.get('otp'))
            # OTP_complate =  request.POST.get('first')
            # OTP_complate += request.POST.get('second')
            # OTP_complate += request.POST.get('third')
            # OTP_complate += request.POST.get('fourth')

            OTP_complate =  request.POST.get('opt_code')
            if OTP_complate == otp.otp:    
                data = {"otp_com" : OTP_complate, "otp":otp , 'number':otp.number}
                return render(request, 'website/order_cart_Add.html', data)
            else:
                data = {"otp" : otp, "number":otp.number, 'error':"failed" }
                return render(request, 'website/order_cart_OTP.html', data)

        if "otp_send" in request.POST:
            otp = otp_gen()
            number = request.POST.get('number')
            if(number[0] == "0"):
                number = number[1:]
            # send otp to number
            from dashboard.requests import sendsms
            text = f'your OTP is {otp}'
            sendsms(text, number)
            # save otp generated for number
            OTP_obj = models.OTP.objects.create(number = number, otp = otp)
            OTP_obj.save()
            
            data = {"otp" : OTP_obj, "number":number }
            return render(request, 'website/order_cart_OTP.html', data)

def otp_gen():
    import random
    otp_1 = random.randint(0,9)
    otp_2 = random.randint(0,9)
    otp_3 = random.randint(0,9)
    otp_4 = random.randint(0,9)
    otp   = str(otp_1) + str(otp_2) + str(otp_3) + str(otp_4)
    return otp
# this class is not needed
class Order_cart_OTP(TemplateView):
    template_name = "website/order_cart_OTP.html"

    def post(self, request,*args, **kwargs):
        data = 0
        return render(request, 'website/order_cart_Add.html', data)

    def get_context_data(self, *args, **kwargs):
        data = super(Order_cart_OTP, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Order'
        return data

class Order_Location(TemplateView):
    template_name = "website/order_cart_Add.html"

def resend_otp(request):
    if request.method =="GET":
        number = request.GET.get('number')
        if number[0] == "0":
            number = number[1:]

        # generate otp and save it to db
        otp = otp_gen()
        obj_otp = models.OTP.objects.create(number = number, otp = otp)
        obj_otp.save()

        # send otp to number
        from dashboard.requests import sendsms
        sendsms(f"your OTP is: {otp}", number)
        return JsonResponse(obj_otp.pk, safe=False)
    else:
        return JsonResponse(False, safe=False) 

class Order_summary(TemplateView):
    template_name = 'website/order_cart_summary.html'

class Order_payment(TemplateView):
    template_name = 'website/order_cart_payment.html'

# order tracking
class TrackOrder(DeleteView):
    model = models.Order
    template_name = "website/confirmed_order.html"

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



# load the payment network international
def Access_token(request):
    id = int(request.GET.get('id'))
    obj = get_object_or_404(models.Order, pk = id)

    # calculate the prices and all
    payment_amount = 0
    tot = models.Order_items.objects.filter(order = obj.pk)
    for i in tot:
        payment_amount += i.quantity * i.menu_item.price
    delivery = obj.area.charge
    vat = (payment_amount * 5) / 100
    payment_amount += delivery
    payment_amount += vat

    # changing it to decimal
    # from decimal import Decimal
    # dec = Decimal(payment_amount)

    # doing it this way now
    payment_amount = "{:.2f}".format(payment_amount) 
    arr = str(payment_amount).split('.')

    import requests
    url = "https://api-gateway.sandbox.ngenius-payments.com/identity/auth/access-token"
    headers = {
        "Accept": "application/vnd.ni-identity.v1+json",
        "Authorization": "Basic MmI3MDRiZTktZTVkMy00NmU3LWI5MzUtYmVmNWJjYTY0YTg3OjMyY2IzNDA2LWY0M2ItNDdiZS1iMDdlLWFjNzg2ZWExYzMxNw==",
        "Content-Type" : "application/vnd.ni-identity.v1+json"
    }
    response = requests.request("POST", url, headers=headers)
    import json 
    y = json.loads(response.text)
    # print(y['access_token'])
    # print(y['refresh_token'])

    order_url = "https://api-gateway.sandbox.ngenius-payments.com/transactions/outlets/71a92b33-a43c-42f0-8996-df7933c7c9c7/orders"

    payload = {
        "merchantAttributes":{
            "redirectUrl":"https://www.pizza.ae/order-payment-status?id="+str(obj.pk),
            "skipConfirmationPage":True
            },
            "amount":{
                "currencyCode":"AED",
                "value":int(arr[0]+arr[1])
            },
            "action":"PURCHASE"
        }

    # print(payload)
    data_obj = json.dumps(payload)
    order_headers = {
        "Accept": "application/vnd.ni-payment.v2+json",
        "Content-Type": "application/vnd.ni-payment.v2+json",
        "Authorization": "Bearer "+y['access_token'],
    }

    res = requests.request("POST", order_url, data=data_obj, headers=order_headers)
    # print(res)
    res_res = json.loads(res.text)
    pay_id = res_res['_id']
    link = res_res["_links"]["payment"]["href"]
    obj.order_pay_ref = pay_id[10:]
    obj.is_complete = False
    obj.save()

    return JsonResponse(link+ "&slim=true", safe=False)


# this is the function that runs after the payment is done
def online_pay_complete(request):
    id = request.GET.get('id')
    ref = request.GET.get('ref')
    print("print all ")
    print(id)
    print(ref)
    # get access token

    import requests
    url = "https://api-gateway.sandbox.ngenius-payments.com/identity/auth/access-token"
    headers = {
        "Accept": "application/vnd.ni-identity.v1+json",
        "Authorization": "Basic MmI3MDRiZTktZTVkMy00NmU3LWI5MzUtYmVmNWJjYTY0YTg3OjMyY2IzNDA2LWY0M2ItNDdiZS1iMDdlLWFjNzg2ZWExYzMxNw==",
        "Content-Type" : "application/vnd.ni-identity.v1+json"
    }
    response = requests.request("POST", url, headers=headers)
    import json 
    token = json.loads(response.text)
    # print(token['access_token'])

    # requesting for status
    status_url = "https://api-gateway.sandbox.ngenius-payments.com/transactions/outlets/71a92b33-a43c-42f0-8996-df7933c7c9c7/orders/"+ref
    
    res = requests.request("GET", status_url, headers= {"Authorization": "Bearer "+token['access_token']})
    # print("this is the status of pay order:")
    # print(res)
    # print(res.text)
    res_res = json.loads(res.text)
    # print(res_res)

    pay_id = res_res['_id']
    pay_id = pay_id[10:]
    obj = get_object_or_404(models.Order, pk = id)

    if obj.order_pay_ref == ref:
        # print("both are the same")
        val = res_res['amount']['value']
        # print("this mapymnet was : ", val)
        obj.payment = float(val)
        obj.is_complete = True
        obj.save()
        from dashboard.requests import sendsms
        text = "THANK YOU FOR ORDERING WITH US. your order had been placed. we will call you once the order arrive."
        sendsms(text, obj.number)
        # print("redirecting")
        return redirect('website:confirmed', pk=obj.pk)
    else:
        return JsonResponse(res.text, safe=False)


class Delete(ListView):
    # model = models.Order
    template_name = "website/history.html"
    paginate_by = 10
    queryset = models.Order.objects.filter(number = '566652534').order_by('-date')

    def get_context_data(self, *args, **kwargs):
        data = super(Delete, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Order History'
        return data


def history(request):
    if request.method == "POST":
        number = request.POST.get('idontknow')
        print(number)
        objects = models.Order.objects.filter(number = number)
        return render(request, 'website/history.html', {'object_list': objects})
    else:
        return redirect('website:auth_otp')

def auth_otp(request):
    if request.method == 'POST':
        # validate the OTP
        if 'otp_validation' in request.POST:
            obj = get_object_or_404(models.OTP, pk = request.POST.get('otp'))
            OTP_complate =  request.POST.get('opt_code')
            if OTP_complate == obj.otp:    
                return render(request, "website/redirects.html", {'number' :obj.number}) 
            else:
                data = {"otp" : obj, "number":obj.number, 'error':"failed" }
                return render(request, 'website/history_OTP.html', data)

        number = request.POST.get('number')
        number = number[1:]

        # generate otp and save it to db
        otp = otp_gen()
        obj_otp = models.OTP.objects.create(number = number, otp = otp)
        obj_otp.save()

        from dashboard.requests import sendsms
        # send otp to number
        sendsms(f"your OTP is: {otp}", number)
        data = {"otp" : obj_otp, "number":number }
        return render(request, 'website/history_OTP.html', data)

    return render(request, 'website/auth_otp.html')



def re_order(request):
    print(request.GET)
    # get id and 
    # find the order and change add a reorder by changeing its status and date
    obj = get_object_or_404(models.Order, pk = request.GET.get('pk'))
    print(obj)
    obj.status = 'ordered'
    obj.is_complete = True
    obj.save()

    return JsonResponse(obj.is_complete, safe=False)