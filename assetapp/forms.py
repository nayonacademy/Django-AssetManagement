from django import forms
from django.contrib.contenttypes import fields

from assetapp.models import Member, Asset, Distribution


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

class DistributionForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = '__all__'
