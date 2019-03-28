from .models import Address
from django.contrib.auth import get_user_model
User = get_user_model()


# 会員登録時に空欄の住所登録

class UserToAddress_AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address


class UserToAddress_UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    relateduser = factory.RelatedFactory(UserToAddress_AddressFactory)
