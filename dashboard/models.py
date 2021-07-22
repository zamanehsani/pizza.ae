from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class About_company(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone   = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    webesite = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard')

    class Meta:
        verbose_name_plural = "About Company"


# as menu has many categories of drink, appitid  ..
# this is the category for menu items
class Menu_category(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard')

    class Meta:
        verbose_name_plural = "Menu Category"
        

# this is the menu item and can be added to a category of menu
class Menu(models.Model):
    name            = models.CharField(max_length=150, null=True, blank=True)
    price           = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    photo           = models.ImageField(default='default.png', upload_to = "menu", null=True, blank=True)
    date            = models.DateField(auto_now_add=True, auto_now=False)
    category        = models.ForeignKey(Menu_category, on_delete=models.CASCADE)
    new             = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard')

    class Meta:
        verbose_name_plural = "Menu"

class Order(models.Model):
    st          = (("ordered", "ordered"),("confirmed","confirmed"), ("delivering", "delivering"), ("delivered", "delivered"))
    name        = models.CharField(max_length=200, null=True, blank=True)
    date        = models.DateTimeField(auto_now=False, auto_now_add=True)
    location    = models.TextField(null=True, blank=True)
    number      = models.IntegerField(null=True, blank=True)
    menu_items  = models.ManyToManyField(Menu)
    status      = models.CharField(max_length=100, null=True, blank=True, choices=st, default=1)
    deliverer   = models.ForeignKey(User, on_delete=models.CASCADE)
    description     = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return  self.name

    def get_absolute_url(self):
        return reverse('dashboard')

    class Meta:
        verbose_name_plural = "Order"

def stock_file(filename):
    # file will be uploaded to MEDIA_ROOT/stock/<m-Y>/<filename>
    from datetime import date
    date_time = date.now().strftime("%m/%Y")	
    return 'stock/{0}/{1}'.format(date_time, filename)

# for the expenses of the store (what you spend for store)
class Stock(models.Model):
    options = (('Piece', 'Piece'),('KG', 'KG'),('Liter', 'Liter'),('Gallon', ' Gallon'), ('Package', 'Package'))
    name = models.CharField(max_length=300, null=True, blank=True)
    quantity = models.SmallIntegerField()
    unit_type = models.CharField(max_length=150, null=True, blank=True, default="Piece", choices=options)
    Unit_price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    totol_price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to = stock_file, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Stock"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dashboard')
