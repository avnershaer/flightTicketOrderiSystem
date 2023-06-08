from django import forms
from .models import UserRole, Users, Adminstrators, Customers, AirLineCompanies, Countries, Flights, Tickets


class UserRoleForm(forms.ModelForm):
    roleName = forms.CharField(
        widget=forms.TextInput(attrs={'maxlength': 25, 'cols': 40, 'rows': 1}),
    )

    class Meta:
        model = Users
        fields = '__all__'
  