from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager
from django.core.validators import MaxValueValidator,MinValueValidator
class MyAccountManager(BaseUserManager):

    # what happens when a user and superuser is created
    def create_user(self,username,phone,password=None): # add the fields which are required for user

        user = self.model(      # here we called self.model
            phone= phone,
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,phone,password):
        user = self.create_user(    # here we called self.create_user
            phone= phone,
            password=password,
            username=username
        )
        user.is_admin =True
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    phone = models.BigIntegerField(verbose_name='phone_number',validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)],unique=True)
    username = models.CharField(verbose_name='username',max_length=50,unique=True)
    email=models.EmailField(blank=True,null=True,unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_joined',auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username' # whatever you want to login with
    REQUIRED_FIELDS = ['phone']

    objects = MyAccountManager() # tell Account where is Account manager located

    def __str__(self): # what will be printed when we will refer to this user object
        return str(self.username)
    # required functions

    def has_perm(self,perm,obj=None): # what permission would this type of user have (staff,buyer,seller)
        return self.is_admin

    def has_module_perms(self,app_label):
        return True




