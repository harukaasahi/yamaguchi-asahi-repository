from django.views import generic
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import SignUpForm, ChangeinfoForm
from .models import Address, User
from django.conf import settings
from django.contrib.auth import get_user_model
#User = settings.AUTH_USER_MODEL


def IndexView(request, account_number):
    address = Address.object.filter(Account_number=account_number)


class SignUpView(generic.CreateView):
    # 会員登録
    template_name = 'account/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class MemberinfoView(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'account/memberinfo.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        address = super().get_context_data(**kwargs)
        address.update({
            'address': Address.objects.select_related().filter(account_number_id__pk=user.pk),
        })
        return address


class ChangeinfoView(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = ChangeinfoForm
    template_name = 'account/changeinfo.html'

    def get_success_url(self):
        return resolve_url('account:memberinfo', pk=self.kwargs['pk'])
