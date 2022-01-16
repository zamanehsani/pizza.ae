import decimal
from os import truncate
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.shortcuts import get_object_or_404
from django.urls import reverse

def customer_profile_location(instance, filename):
    return '/profiles/customer/{0}/{1}'.format(instance.user.username, filename)

class Customer(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    date        = models.DateTimeField(auto_now_add=True)
    email_confirmed = models.BooleanField(default=False)
    phone       = models.PositiveIntegerField("what is your phone?",null=True, blank=True)
    address     = models.CharField("where do you live?",max_length=500,null=True, blank=True)
    photo       = models.ImageField("Upload a square picture of yourself.",default='default.png', upload_to = customer_profile_location, null=True, blank=True)

    def __str__(self):
        return self.user.email
    
    def get_absolute_url(self):
        return reverse('dashboard:customer')

    class Meta:
        verbose_name_plural = "Customer"


def profile_location(instance, filename):
    return 'profiles/{0}/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField("tell me about yourself",null=True, blank=True)
    phone = models.PositiveIntegerField("what is your phone?",null=True, blank=True)
    address = models.CharField("where do you live?",max_length=500,null=True, blank=True)
    photo = models.ImageField("Upload a square picture of yourself.",default='default.png', upload_to = profile_location, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.photo.path)
    #     if img.height > 400 or img.width > 400:
    #         output_size = (400,400)
    #         img.thumbnail(output_size)
    #         img.save(user.photo.path)
    #         print("your photo was large, so we resized and saved")

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('dashboard:profile')

    class Meta:
        verbose_name_plural = "Profile"


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
        return reverse('dashboard:dashboard')

    class Meta:
        verbose_name_plural = "About Company"


# as menu has many categories of drink, appitid  ..
# this is the category for menu items
class Menu_category(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField()
    sort = models.SmallIntegerField(blank=True, null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard:menulist')

    class Meta:
        verbose_name_plural = "Menu Category"
        

class Areas(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150, null=True, blank=True)
    charge = models.DecimalField(max_digits=10, decimal_places=3)
    min_order = models.SmallIntegerField(null=True, blank=True)
    geojson = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Area"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dashboard:area')


# this is the menu item and can be added to a category of menu
class Menu(models.Model):
    name            = models.CharField(max_length=150, null=True, blank=True)
    price           = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    photo           = models.ImageField(default='default-pizza.png', upload_to = "menu", null=True, blank=True)
    date            = models.DateField(auto_now_add=True, auto_now=False)
    category        = models.ForeignKey(Menu_category, on_delete=models.CASCADE, default=1)
    new             = models.BooleanField(default=False)
    sort            = models.SmallIntegerField(blank=True, null=True)
    available       = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard:menulist')

    class Meta:
        verbose_name_plural = "Menu"


class Ingrediants(models.Model):
    name    = models.CharField(max_length=100, null=True, blank=True)
    amount  = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard:dashboard')

    class Meta:
        verbose_name_plural = "Ingrediant"

class Menu_tags(models.Model):
    menu        = models.ManyToManyField(Menu)
    ingrediant  = models.ManyToManyField(Ingrediants)

    def __str__(self) -> str:
        return self.name


class OTP(models.Model):
    date = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)

    def __str__(self) ->str:
        return str(self.otp)
        

class Order(models.Model):
    name        = models.CharField(max_length=200, null=True, blank=True)
    date        = models.DateTimeField(auto_now=False, auto_now_add=True)
    location    = models.TextField(null=True, blank=True)
    number      = models.IntegerField(null=True, blank=True)
    status      = models.CharField(max_length=100, null=True, blank=True)
    deliverer   = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True) 
    address     = models.TextField(blank=True, null=True)
    payment     = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    area        = models.ForeignKey(Areas, on_delete=models.CASCADE, null=True, blank=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    order_source    = models.CharField(max_length=70, blank=True, null=True)
    order_pay_ref   = models.CharField(max_length=150, blank=True, null=True)
    is_complete     = models.BooleanField(default=True)

    def __str__(self) -> str:
        return  str(self.name)

    def get_absolute_url(self):
        return reverse('dashboard:order')

    @property
    def menu_items(self):
        print(self.order_item_list.all())
        return self.order_item_list.all()
    @property
    def area_charge(self):
        if self.area:
            return float("{:.2f}".format(self.area.charge))
        else:
            return 0
            

    @property
    def vat(self):
        # float("{:.2f}".format(13.949999999999999))
        vat = (float(self.get_totol) * 5) / 100
        return float("{:.2f}".format(vat))

    @property
    def get_totol(self):
        "get the price order"
        price = self.order_item_list.all()
        tot = 0
        for i in price:
            tot += i.quantity * i.menu_item.price  

        # get the vat without the delivery charge (objects vat only)
        vat = (tot * 5) /100
        tot += vat
        # add area charge as well
        if self.area:
            tot += self.area.charge 
             
        return  float("{:.2f}".format(tot))

    @property
    def coordinate(self):
        "get the location coordinate"
        # if location exist for the record swap let to longt
        if self.location:
            loca = self.location.split(',')
            b = ''
            b += loca[1]
            b += ','
            b += loca[0]
            return b
      

    class Meta:
        verbose_name_plural = "Order"

class Order_items(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_item_list")
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    def __str__(self) -> str:
        return  str(self.order  ) + str(self.menu_item)

    def get_absolute_url(self):
        return reverse('dashboard:order')


    class Meta:
        verbose_name_plural = "Order Items"

def stock_file(filename):
    # file will be uploaded to MEDIA_ROOT/stock/<m-Y>/<filename>
    from datetime import date
    date_time = date.now().strftime("%m/%Y")	
    return 'stock/{0}/{1}'.format(date_time, filename)


# for the expenses of the store (what you spend for store)
class Stock(models.Model):
    options     = (('Piece', 'Piece'),('KG', 'KG'),('Liter', 'Liter'),('Gallon', ' Gallon'), ('Package', 'Package'))
    name        = models.CharField(max_length=300, null=True, blank=True)
    quantity    = models.SmallIntegerField()
    unit_type   = models.CharField(max_length=150, null=True, blank=True, default="Piece", choices=options)
    Unit_price  = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    totol_price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    date        = models.DateTimeField(auto_now=False, auto_now_add=True)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    file        = models.FileField(upload_to = stock_file, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Stock"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dashboard:stock')


# what the store member eat
class Staff_Salary(models.Model):
    months = (('January', 'January'),('February', 'February'),('March', 'March'),('April', ' April'), 
              ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'),
              ('October', 'October'), ('November', 'November'), ('December', 'December'))

    pay_by  = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name    = models.ForeignKey(User, on_delete=models.CASCADE,related_name="staff")
    salary  = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    month   = models.CharField(max_length=150, null=True, blank=True, choices=months)
    Pay     = models.DecimalField(max_digits=10, decimal_places=3)
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Staff Salary"
    
    def __str__(self):
        return self.name.username + " - " + self.month
    
    def get_absolute_url(self):
        return reverse('dashboard:salary')

