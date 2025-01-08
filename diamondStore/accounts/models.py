from django.db import models
from django.utils.timezone import now
#from django.contrib.auth.models import AbstractUser


class Users(models.Model):
    ROLE_CHOICES = [
        (0, 'Guest'),
        (1, 'Customer'),
        (2, 'Sales'),
        (3, 'Staff'),
        (4, 'Delivery Staff'),
        (5, 'Manager'),
        (6, 'Admin'),
    ]

    userid = models.AutoField(db_column='USERID', primary_key=True)
    username = models.CharField(db_column='USERNAME', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(db_column='EMAIL', unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    password = models.CharField(db_column='PASSWORD', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    userphone = models.CharField(db_column='UserPhone', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address = models.CharField(db_column='ADDRESS', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    role = models.IntegerField(db_column='ROLE', choices=ROLE_CHOICES, blank=True, null=True)
    create_at = models.DateTimeField(db_column='CREATE_AT', blank=True, null=True)
    update_at = models.DateTimeField(db_column='UPDATE_AT', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Users'

    def get_role_display(self):
        """Get human-readable role name."""
        return dict(self.ROLE_CHOICES).get(self.role, 'Unknown')

# class User(models.Model):
#     ROLE_CHOICES = (
#         (1, 'Admin'),
#         (2, 'Manager'),
#         (3, 'Customer'),
#         (4, 'Salesman'),
#         (5, 'Delivery Staff'),
#     )
#     USERID = models.AutoField(primary_key=True)
#     USERNAME = models.CharField(max_length=50, null=False)
#     EMAIL = models.EmailField(max_length=50, unique=True, null=False)
#     PASSWORD = models.CharField(max_length=255, null=False)
#     UserPhone = models.CharField(max_length=15, blank=True, null=True)
#     ADDRESS = models.CharField(max_length=255, blank=True, null=True)
#     ROLE = models.IntegerField(blank=True, null=True)
#     CREATE_AT = models.DateTimeField(default=now)
#     UPDATE_AT = models.DateTimeField(default=now)


#     def __str__(self):
#         return self.USERNAME



# class User(models.Model):
#     USERID = models.AutoField(primary_key=True)
#     USERNAME = models.CharField(max_length=50, null=False)
#     EMAIL = models.EmailField(max_length=50, unique=True, null=False)
#     PASSWORD = models.CharField(max_length=255, null=False)
#     UserPhone = models.CharField(max_length=15, blank=True, null=True)
#     ADDRESS = models.CharField(max_length=255, blank=True, null=True)
#     ROLE = models.IntegerField(blank=True, null=True)
#     CREATE_AT = models.DateTimeField(default=now)
#     UPDATE_AT = models.DateTimeField(default=now)

#     def __str__(self):
#         return self.USERNAME

# class Customer(AbstractUser):
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)


# class User(AbstractUser):
#     is_admin = models.BooleanField(default=False) 
#     is_customer = models.BooleanField(default=False)
#     #is_salesman = models.BooleanField(default=False)
#     #is_deleveryStaff = models.BooleanField(default=False)
#     is_manager = models.BooleanField(default=False)
