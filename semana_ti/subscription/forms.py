# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

from .models import Subscription

class SubscriptionForm(forms.ModelForm):
	def clean_registration(self):
		if self.cleaned_data['person_type'] == 'Academico FASA' and self.cleaned_data['registration'] == '':
			raise ValidationError("Este campo é obrigatório.")

		return self.cleaned_data['registration']

	class Meta:
		model = Subscription
		fields = '__all__'
		widgets = {
			'person_type': forms.Select(attrs={
				'onchange': 'check_input()',
			}),
			'event': forms.CheckboxInput(),
		}
