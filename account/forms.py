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
    
import pandas as pd
import os

def function1(request):
    
    os.chdir("C:/Users/haruka/Downloads")
    df= pd.read_csv("AllPrefecture.csv",encoding="SHIFT-JIS")
    #conn = sqlite3.connect('db.sqlite3')
    #conn.text_factory = lambda x: str(x, 'latin1')
    #c = conn.cursor()
    #c.execute("select pre where newPostal ==  (?) ",(request,))
    #pre = str(c.fetchall())
    #conn.commit()
    #conn.close()
    return (df.loc[df['newPostal'] == request, 'Pre']).iat[0]

def function2(request):

    os.chdir("C:/Users/haruka/Downloads")
    df= pd.read_csv("AllPrefecture.csv",encoding="SHIFT-JIS")
#    conn = sqlite3.connect('db.sqlite3')
#    conn.text_factory = lambda x: str(x, 'latin1')
#    c = conn.cursor()
#    c.execute("select City from AddressTable where newPostal ==  (?) ",(request,))
#    pre = str(c.fetchall())
#    conn.close()
#    return str(pre)
    return (df.loc[df['newPostal'] == request, 'City']).iat[0]
    

def function3(request):

    os.chdir("C:/Users/haruka/Downloads")
    df= pd.read_csv("AllPrefecture.csv",encoding="SHIFT-JIS")
#    conn = sqlite3.connect('db.sqlite3')
#    conn.text_factory = lambda x: str(x, 'latin1')
#    c = conn.cursor()
#    c.execute("select Zips from AddressTable where newPostal ==  (?) ",(request,))
#    pre = str(c.fetchall())
#    conn.commit()
#    conn.close()
#    return str(pre)
    return (df.loc[df['newPostal'] == request, 'Zips']).iat[0]

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('postcode','prefecture', 'city',
                  'zip', 'building', 'room','tell',)
        widgets = {
            'postcode':forms.TextInput(
                attrs={'placeholder':'記入例:1234567',},
                ),
            'prefecture': forms.TextInput(
                attrs={'class': 'p-region','placeholder':'記入例:鹿児島県','value':function1(640941)},
                ),
            'city': forms.TextInput(
                #attrsでp-locality p-street-address p-extended-addressを指定
               attrs={'placeholder':'記入例:鹿児島市中央町','value':function2(640941)},
                ),
            'zip': forms.TextInput(
                #attrsでp-locality p-street-address p-extended-addressを指
                attrs={'class': '','placeholder': '記入例：１０－１','value':function3(640941)},
                ),
            'building' : forms.TextInput(    
               #attrsでp-locality p-street-address p-extended-addressを指定
                attrs={'class': '','placeholder': '記入例：キャンセビル'},                    
                ),
            'room': forms.TextInput(               
                attrs={'class': '','placeholder': '記入例：１２３号室'},
                ),
            'tell': forms.TextInput(
                attrs={'class': '','placeholder': '記入例：090-1234-5678'},
                ),

            }


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
