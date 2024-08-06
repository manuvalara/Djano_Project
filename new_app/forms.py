from django import forms

from new_app.models import food


class food_form(forms.ModelForm):

    class Meta:
        model = food
        fields = ("__all__")
