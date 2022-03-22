from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, name, phone_number, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.name = name
        user.phone_number = phone_number
        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user
        
        
    def create_superuser(self, email, name, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.name = name
        user.phone_number = phone_number
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    name = models.CharField(null=True, blank=False, max_length=255)
    phone_number = models.IntegerField(null=True,blank=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_spam = models.BooleanField(default=False)
    username = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']


class Contact(models.Model):
    main_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='main_user')
    added_contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='added_contact')
    contact_name = models.CharField(max_length=50)

