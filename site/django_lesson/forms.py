from django import forms


class Order(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={
                               "class": "form-control",
                               "placeholder": "ФИО полностью"
                           }),
                           label='Фамилия Имя Отчество',
                           required='')
    city = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={
                               "class": "form-control",
                               "placeholder": "Город, почтовый индекс"
                           }),
                           label='Город и  почтовый индекс',
                           required='')
    address = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={
                                  "class": "form-control",
                                  "placeholder": "Улица, дом квартира"
                              }),
                              label='Адрес',
                              required='')
    phone = forms.CharField(max_length=15,
                            widget=forms.TextInput(attrs={
                                "class": "form-control",
                                "placeholder": "Номер телефона"
                            }),
                            label='Телефон',
                            required='')
