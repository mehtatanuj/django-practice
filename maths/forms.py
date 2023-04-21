from django import forms


class MyForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()
    action = forms.ChoiceField(choices=[('1', 'ADD'), ('2', 'SUB'), ('3', 'MULTI'), ('4', 'DIVIDE')])
