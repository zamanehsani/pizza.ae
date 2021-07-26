
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from dashboard import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from dashboard import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect, render


class Dashboard(LoginRequiredMixin, TemplateView):
    # login_url = "./dashboard/login"
    template_name = "dashboard/index.html"

    def get_queryset(self):
        category = self.kwargs.get("category")
        # s/alary 
        # if category:
        #     queryset = Product.objects.filter(category__iexact=category)
        # else:
        #     queryset = Product.objects.all()
        # return queryset

    def get_context_data(self, *args, **kwargs):
        data = super(Dashboard, self).get_context_data(*args, **kwargs)
        
        from datetime import datetime
        month = datetime.now().strftime('%B')
        data['page_title'] = 'Dashboard'
        data['salaries'] = models.Staff_Salary.objects.filter(month = month).count()
        data['users'] = User.objects.all().count()
        data['stocks'] = models.Stock.objects.all().count()
        data['menus'] = models.Menu.objects.all().count()
        data['orders'] = models.Order.objects.all().count()

        return data

class Profile(LoginRequiredMixin,SuccessMessageMixin, DetailView):
    model = User
    template_name = 'dashboard/profile.html'

    def post(self, request, pk):
        user = User.objects.get(pk = request.user.id)
        u_form = forms.UserUpdateform(request.POST, instance=user)
        p_form = forms.UserProfileform(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'your Profile has been updated.', fail_silently=True)
            return redirect('dashboard:profile', pk=user.id)
        return redirect('dashboard:profile', pk=user.id)

class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = "dashboard/users.html"

    def get_context_data(self, *args, **kwargs):
        data = super(UserList, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Users'
        return data

class Add_User(LoginRequiredMixin,CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'dashboard/User_form.html'
    success_url = '/dashboard/users'

    def get_context_data(self, *args, **kwargs):
        data = super(Add_User, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Users'
        return data

class Update_User(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard/User_form.html'
    fields = [ 'first_name', 'last_name', 'username', "is_active", "user_permissions"]
    success_url = '/dashboard/users'

    def get_context_data(self, *args, **kwargs):
        data = super(Update_User, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Users'
        return data

@login_required(login_url="/login")
def Passchange(request, pk):
    user = User.objects.get(pk = pk)
    form = PasswordChangeForm(user=user)
    if request.method =="POST":
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{user} password has been changed.', fail_silently=True)
            return redirect("dashboard:users")
        else:
            return render(request, 'dashboard/User_form.html',{'form':form})
    return render(request, 'dashboard/User_form.html',{'form':form})
    
class Delete_User(LoginRequiredMixin, DeleteView):
    model = User
    # login_url ="/login"
    template_name = "dashboard/delete_user.html"
    success_url = '/dashboard/users'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_User, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Users'
        return data
    
class MenuList(LoginRequiredMixin, ListView):
    # login_url = '/login'
    model = models.Menu_category
    template_name = "dashboard/MenuList.html"

    def get_context_data(self, *args, **kwargs):
        data = super(MenuList, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Menu'
        return data

class Add_Menu(LoginRequiredMixin,CreateView):
    model = models.Menu
    template_name = 'dashboard/Menu_form.html'
    fields = "__all__"
    def get_context_data(self, *args, **kwargs):
        data = super(Add_Menu, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Menu'
        return data

class Update_Menu(LoginRequiredMixin, UpdateView):
    model = models.Menu
    template_name = 'dashboard/Menu_form.html'
    fields = "__all__"
    def get_context_data(self, *args, **kwargs):
        data = super(Update_Menu, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Menu'
        return data


class Delete_Menu(LoginRequiredMixin, DeleteView):
    model = models.Menu
    template_name = "dashboard/delete_menu.html"
    success_url = '/dashboard/menu'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_Menu, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Menu'
        return data

class Add_Menu_category(LoginRequiredMixin,CreateView):
    model = models.Menu_category
    template_name = 'dashboard/Menu_category_form.html'
    fields = "__all__"
    def get_context_data(self, *args, **kwargs):
        data = super(Add_Menu_category, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Menu'
        return data

class Update_Menu_category(LoginRequiredMixin, UpdateView):
    model = models.Menu_category
    template_name = 'dashboard/Menu_category_form.html'
    fields = "__all__"
    def get_context_data(self, *args, **kwargs):
        data = super(Update_Menu_category, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Menu'
        return data


class Delete_Menu_category(LoginRequiredMixin, DeleteView):
    model = models.Menu_category
    template_name = "dashboard/delete_menu_category.html"
    success_url = '/dashboard/menu'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_Menu_category, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Menu'
        return data



# the expenses, 
class Stock(LoginRequiredMixin, ListView):
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

    def get_context_data(self, *args, **kwargs):
        data = super(Add_Stock, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Stock'
        return data

class Update_Stock(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # login_url = '/login'
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
    # login_url ="/login"
    template_name = "dashboard/delete_stock.html"
    success_url = '/dashboard/stock'
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
    # login_url = '/login'

    def get_context_data(self, *args, **kwargs):
        data = super(Salary, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Employee Salary'
        return data

class Pay_salary(LoginRequiredMixin, CreateView):
    # login_url = '/login'
    model = models.Staff_Salary
    template_name = 'dashboard/staff_salary_form.html'
    fields = ['name', 'salary', 'month', 'Pay']
    
    def form_valid(self, form):
        form.instance.pay_by = self.request.user
        return super().form_valid(form)

class Update_salary(LoginRequiredMixin, UpdateView):
    # login_url = '/login'
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
    # success_url = '/dash/salary'
    def get_context_data(self, *args, **kwargs):
        data = super(Delete_Salary, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Employee Salary'
        return data
    
    # def test_func(self):
    #     salary = self.get_object()
    #     if self.request.pay_by == salary.pay_by:
    #         return True
    #     return False