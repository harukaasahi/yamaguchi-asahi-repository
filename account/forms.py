from .models import Address
from django.contrib.auth.forms import UserCreationForm
from django import forms


from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
    # ユーザー登録用フォーム
    class Meta:
        model = User
        fields = ('username', 'email')


class ModelFormWithFormSetMixin:

    def __init__(self, *args, **kwargs):
        super(ModelFormWithFormSetMixin, self).__init__(*args, **kwargs)
        self.formset = self.formset_class(
            instance=self.instance,
            data=self.data if self.is_bound else None,
        )

    def is_valid(self):
        return super(ModelFormWithFormSetMixin, self).is_valid() and self.formset.is_valid()

    def save(self, commit=True):
        saved_instance = super(ModelFormWithFormSetMixin, self).save(commit)
        self.formset.save(commit)
        return saved_instance


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('postcode', 'prefecture', 'city',
                  'zip', 'building', 'room','tell',)


AddressFormSet = forms.inlineformset_factory(
    parent_model=User,
    model=Address,
    form=AddressForm,
    extra=1
)


class ChangeinfoForm(ModelFormWithFormSetMixin, forms.ModelForm):
    # ユーザー情報更新フォーム
    # AddressFormとくっつける
    formset_class = AddressFormSet

    class Meta:
        model = User
        fields = ('email', 'last_name', 'first_name',)

    ''' def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
 '''
