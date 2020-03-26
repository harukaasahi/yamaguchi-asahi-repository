from .models import Address
from django.contrib.auth.forms import UserCreationForm
from django import forms
import sqlite3
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

    #辞書機能の追加を試みた(が上手くいかない)
    #今回の変更箇所はこの1ブロックのみ
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['postcode'].widget.attrs.update({'class': 'special',})
#        self.fields['prefecture'].widget.attrs.update({'class': 'special',})
#        self.fields['city'].widget.attrs.update({'class': 'special',})  
#        self.fields['zip'].widget.attrs.update({'class': 'special',})
#        self.fields['building'].widget.attrs.update({'class': 'special',})
#        self.fields['room'].widget.attrs.update({'class': 'special',})
#        self.fields['tell'].widget.attrs.update({'class': 'special',})


    class Meta:
        model = Address
        fields = ('postcode','prefecture', 'city', 'town', 
                  'zip', 'building', 'room','tell',)


#        def __init__(self, *args, **kwargs):
#            super().__init__(*args, **kwargs)
#            for field in iter(self.fields):
#                self.fields[field].widget.attrs.update({'class': 'special',})    

        widgets = {
            'postcode':forms.TextInput(
                attrs={'class': 'p-postal-code','placeholder':'記入例:1234567',},
               ),
            'prefecture': forms.TextInput(
                attrs={'class': 'p-region','placeholder':'記入例:鹿児島県',},
                ),
            'city': forms.TextInput(
               #attrsでp-locality p-street-address p-extended-addressを指定
               attrs={'class': 'p-locality','placeholder':'記入例:鹿児島市',},
                ),
            'town': forms.TextInput(
                #attrsでp-locality p-street-address p-extended-addressを指
               attrs={'class': 'p-street-address','placeholder': '記入例：中央町',},
                ),
            'zip': forms.TextInput(
                #attrsでp-locality p-street-address p-extended-addressを指
               attrs={'class': 'p-extended-address','placeholder': '記入例：１０－１',},
                ),    
            'building' : forms.TextInput(    
               #attrsでp-locality p-street-address p-extended-addressを指定
                attrs={'placeholder': '記入例：キャンセビル',},                    
                ),
            'room': forms.TextInput(               
                attrs={'placeholder': '記入例：１２３号室',},
                ),
            'tell': forms.TextInput(
                attrs={'placeholder': '記入例：090-1234-5678',},
                ),

            }




AddressFormSet = forms.inlineformset_factory(

    parent_model=User,

    model=Address,

    form=AddressForm,

    extra=0

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