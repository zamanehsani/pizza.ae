
from django.views.generic.list import ListView
from . import models

class MenuList(ListView):
    # login_url = '/login'
    model = models.Menu
    template_name = "dashboard/MenuList.html"

    def get_context_data(self, *args, **kwargs):
        data = super(MenuList, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Menu'
        return data
    
