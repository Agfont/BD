from django import forms
from . import models

CHARFIELD_LENGTH = 100

class ConflictForm(forms.ModelForm):
    class Meta:
        model = models.Conflict
        fields = '__all__'

    # codigo = forms.IntegerField()
    # nome = forms.CharField(max_length=CHARFIELD_LENGTH)
    # tipo = forms.CharField(max_length=CHARFIELD_LENGTH)
    # num_feridos = forms.IntegerField()
    # num_mortos = forms.IntegerField()


class MilitaryChiefForm(forms.ModelForm):
    class Meta:
        model = models.MilitaryChief
        fields = '__all__'


class PoliticalLeaderForm(forms.ModelForm):
    class Meta:
        model = models.PoliticalLeader
        fields = '__all__'


class ArmedGroupForm(forms.ModelForm):
    class Meta:
        model = models.ArmedGroup
        fields = '__all__'


class DivisionForm(forms.ModelForm):
    class Meta:
        model = models.Division
        fields = '__all__'


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = '__all__'


class WeaponForm(forms.ModelForm):
    class Meta:
        model = models.Weapon
        fields = '__all__'


class DealerForm(forms.ModelForm):
    class Meta:
        model = models.Dealer
        fields = '__all__'


# class SupplyWeaponArmedGroupDealerForm(forms.ModelForm):
#     class Meta:
#         model = models.SupplyWeaponArmedGroupDealer
#         fields = '__all__'


# class ConflictForm(forms.ModelForm):
#     class Meta:
#         model = models.Conflict
#         fields = '__all__'

