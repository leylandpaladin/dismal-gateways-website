from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    purpose = forms.CharField(
            widget=forms.Textarea(
                attrs={'rows': 20,
                    'cols': 120}
                )
            )
    links = forms.CharField()
