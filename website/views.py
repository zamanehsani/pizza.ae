from django.shortcuts import render
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

class CartView(TemplateView):
    template_name = "website/cart_view.html"

    def get_context_data(self, *args, **kwargs):
        data = super(CartView, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Cart'
        return data