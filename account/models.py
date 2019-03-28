from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator


''' class User(AbstractUser):
    pass
 '''


class UserManager(BaseUserManager):
    ''' def _create_user(self, username, email, password, **extra_fields):
        username = models.CharField(max_length=7)
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user '''

    def create_user(self, username, email, password):
        if not email:
            raise ValueError('Users must have an email')
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username, email=email, password=password)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    # ユーザー(email,username,last_name,first_name)
    email = models.EmailField(_('email address'))
    username = models.CharField(
        verbose_name='会員番号', max_length=10, unique=True)
    last_name = models.CharField(verbose_name='姓', max_length=10, blank=True)
    first_name = models.CharField(verbose_name='名', max_length=10, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class Address(models.Model):
    # 住所(account_number(UserのusernameよりForeignKey),postcode,prefecture,city,zip,building,room,created_times)
    account_number = models.ForeignKey(
        User, on_delete=models.CASCADE)  # ,verbose_name='会員番号'settings.AUTH_USER_MODEL
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$')
    postcode = models.CharField(
        '郵便番号', validators=[postal_code_regex], max_length=7, blank=True)  # 郵便番号
    prefecture = models.CharField('都道府県', max_length=10, blank=True)  # 県
    city = models.CharField('市区町村', max_length=30, blank=True)  # 市町村区
    zip = models.CharField('丁番号', max_length=10, blank=True)  # 丁番号
    building = models.CharField('建物名', max_length=30, blank=True)  # 建物
    room = models.CharField('部屋番号', max_length=10, blank=True)  # 部屋番号
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$')
    tell = models.CharField(
        '電話番号', validators=[tel_number_regex], max_length=11, blank=True)
    created_times = models.DateTimeField('作成日', default=timezone.now)
