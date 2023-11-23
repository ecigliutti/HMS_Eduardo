from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES=(
        ('A25', 'Apt A25 1 Bedroom'),
        ('A01', 'Apt A01 2 Bedrooms'),
        ('A19', 'Apt A19 2 Bedrooms'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])