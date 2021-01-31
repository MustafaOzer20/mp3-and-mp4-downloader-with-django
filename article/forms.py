from django import forms
from .models import Link
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['vid_link',]

from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )

        