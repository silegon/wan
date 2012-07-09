from django import forms
from django.conf import settings
import os.path

class UploadForm(forms.Form):
    file = forms.FileField()

    def save(self, uploaded_file, name):
        with open(uploaded_file, 'r') as f:
            destination = open(os.path.join(settings.MEDIA_ROOT, name), 'wb+')
            destination.write(f.read())
            destination.close()
        print 'File "%s" would presumably be saved to disk now.'%uploaded_file
        pass
