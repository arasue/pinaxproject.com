from django import forms

from example_sites.models import Site



class SiteSubmissionForm(forms.ModelForm):
    
    class Meta:
        model = Site
        fields = [
            "name",
            "description",
            "url",
            "contact_name",
            "contact_email",
        ]
