import os
from django.core.exceptions import ValidationError

def validateImportFile(file):
	ext = os.path.splitext(file.name)[1]
	valid_extensions = ['.srsnote']
	if not ext.lower() in valid_extensions:
		raise ValidationError(u'Unsupported file extension (.srsnote files only).')