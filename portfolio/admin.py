from django.contrib import admin
from .models import Hobby, PortfolioItem, Contact

# Register your models here.

admin.site.register(Hobby)
admin.site.register(PortfolioItem)
admin.site.register(Contact)