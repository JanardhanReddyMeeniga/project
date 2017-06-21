
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.utils import timezone
from seller.managers import CustomUserManager
#from django.utils.translation import ugettext_lazy as _
#from django.dispatch import receiver
#from allauth.account.signals import password_changed


class Seller(AbstractBaseUser, PermissionsMixin):
    '''
    seller login credentials
    '''
    seller_id = models.AutoField(primary_key=True)
    #seller_email = models.EmailField(_('email address'), max_length=254, unique=True, db_index=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    #password = models.CharField(max_length=254)
    seller_firstname = models.CharField(max_length=254, null=False, blank=False)
    seller_lastname = models.CharField(max_length=254, null=False, blank=False)
    subscription_grand_date = models.DateTimeField(default=timezone.now)#, help_text="Date when User is modified.")
    subscription_end_date = models.DateTimeField(blank=True, null=True)
    grant_access = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.seller_firstname, self.seller_lastname)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.seller_firstname

# class SellersEmailSettings():
#     seller = models.ForeignKey(Seller)
#     username = models.CharField(max_length=254)
#     password = models.CharField(max_length=254)
#     from_email = models.EmailField()
#     email_server = models.EmailField()
#     ssl_port = models.IntegerField()
#     tls_port = models.IntegerField()
