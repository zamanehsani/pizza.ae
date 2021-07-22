
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    login_url = "/login"
    template_name = "dashboard/index.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Dashboard, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Dashboard'
        return data


class MenuList(ListView):
    # login_url = '/login'
    model = models.Menu
    template_name = "dashboard/MenuList.html"

    def get_context_data(self, *args, **kwargs):
        data = super(MenuList, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Menu'
        return data
    
# the expenses, 
class Stock(ListView):
    model = models.Stock
    template_name = "dashboard/Stock.html"

    def get_context_data(self, *args, **kwargs):
        data = super(Stock, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Stock'
        return data

class Add_Stock(LoginRequiredMixin,CreateView):
    # login_url = '/login'
    model = models.Stock
    template_name = 'dashboard/Stock_form.html'
    fields = ['name', 'quantity', 'unit_type', 'Unit_price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.totol_price = form.instance.quantity * form.instance.Unit_price
        return super().form_valid(form)

class Update_Stock(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login'
    model = models.Stock
    template_name = 'dashboard/Stock_form.html'
    fields = ['name', 'quantity', 'unit_type', 'Unit_price']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.totol_price = form.instance.quantity * form.instance.Unit_price
        return super().form_valid(form)

    # def form_valid(self, form):
    #     form.instance.pay_by = self.request.user
    #     return super().form_valid(form)
    
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False

class Delete_Stock(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = models.Stock
    login_url ="/login"
    template_name = "dashboard/delete_stock.html"
    success_url = '/dash/stock'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_Stock, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Stock'
        return data
    
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.user:
            return True
        return False



# the salary module includes the listing, making the payment, removal and editing
class Salary(LoginRequiredMixin, ListView):
    model = models.Staff_Salary
    template_name = "dashboard/salary.html"
    login_url = '/login'

    def get_context_data(self, *args, **kwargs):
        data = super(Salary, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Employee Salary'
        return data

class Pay_salary(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = models.Staff_Salary
    template_name = 'dashboard/staff_salary_form.html'
    fields = ['name', 'salary', 'month', 'Pay']
    
    def form_valid(self, form):
        form.instance.pay_by = self.request.user
        return super().form_valid(form)


class Update_salary(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = models.Staff_Salary
    template_name = 'dashboard/staff_salary_form.html'
    fields = ['name', 'salary', 'month', 'Pay']
    
    def form_valid(self, form):
        form.instance.pay_by = self.request.user
        return super().form_valid(form)
    
    # def test_func(self):
    #     salary = self.get_object()
    #     if self.request.pay_by == salary.pay_by:
    #         return True
    #     return False

class Delete_Salary(LoginRequiredMixin, DeleteView):
    model = models.Staff_Salary
    template_name = "dashboard/delete_salary.html"
    success_url = '/dash/salary'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_Salary, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Employee Salary'
        return data
    
    # def test_func(self):
    #     salary = self.get_object()
    #     if self.request.pay_by == salary.pay_by:
    #         return True
    #     return False