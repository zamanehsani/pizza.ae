from django.shortcuts import render
from dashboard import models
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView


class Menu(ListView):
    model = models.Menu_category
    template_name = "website/menu.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Menu, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'PIZZA.AE'
        return data


class Cart(DetailView):
    model = models.Menu
    template_name = "website/cart.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Cart, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'your order'
        return data

class LandingPage(TemplateView):
    template_name = "website/LandingPage.html"

    def get_context_data(self, *args, **kwargs):
        data = super(LandingPage, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'PIZZA.AE'
        return data
