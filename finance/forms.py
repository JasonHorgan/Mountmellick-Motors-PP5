from django import forms
from .models import FinanceApplication
from products.models import Stock


class FinanceApplicationForm(forms.ModelForm):
    class Meta:
        model = FinanceApplication
        fields = [
            "full_name",
            "date_of_birth",
            "address",
            "phone_number",
            "email",
            "employment_status",
            "monthly_income",
            "loan_term",
            "preferred_contact_method",
            "car",
        ]

    car = forms.ModelChoiceField(
        queryset=Stock.objects.all(),
        empty_label="Select a car",
        widget=forms.Select(attrs={"class": "form-control"}),
        to_field_name="id",
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["car"].queryset = Stock.objects.all()
        self.fields["car"].label_from_instance = self.car_label_from_instance

    def car_label_from_instance(self, obj):
        """Customize the way each car is displayed in the dropdown."""
        return f"{obj.reg_number} - {obj.make} {obj.model}"

    def clean_monthly_income(self):
        monthly_income = self.cleaned_data["monthly_income"]
        if monthly_income <= 0:
            raise forms.ValidationError(
                "Monthly income must be a positive value."
            )
        return monthly_income

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if len(phone_number) < 10:
            raise forms.ValidationError(
                "Phone number must have at least 10 digits."
            )
        return phone_number
