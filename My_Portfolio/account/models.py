from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager): #creating a new user

    def create_user(self,email,username,password = None): # passing needed parameters
        if not email: # check is there is any email
            raise ValueError("Please provide an email address")
        if not username: # check is there any username
            raise ValueError("Please provide a username")
        user = self.model(email=self.normalize_email(email), username=username) # creats the user with the usaer name and email
        user.set_password(password) # sets the users password
        user.save(using=self._db) # saves the user in database
        return user
    def create_superuser(self,email,username, password = None):
        user = self.create_user(email=self.normalize_email(email), username=username,password = password) # creats the user with the usaer name and email
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)  # saves the user in database
        return user
class Account(AbstractBaseUser): # creats a costum user model

    email = models.EmailField(verbose_name="email",unique=True) # creates an email field
    username = models.CharField(max_length= 30, unique = True) # creates an username field
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True) # mandatory django fields
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True) # mandatory django fields
    is_admin = models.BooleanField(default=False) # mandatory django fields checks if user has admin privileges flase by defualt
    is_active = models.BooleanField(default=True) # mandatory django fields checks if user account is active True by defualt
    is_staff = models.BooleanField(default=False) # mandatory django fields checks is user has staff privileges flase by defualt
    is_superuser = models.BooleanField(default=False) # mandatory django fields checks is user has superuser privileges flase by defualt
    USERNAME_FIELD = "email" # what we use to login
    REQUIRED_FIELDS = ["username"] # requierd fields

    objects = MyAccountManager() # telling our model where is our manager

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms (self, app_label):
        return True