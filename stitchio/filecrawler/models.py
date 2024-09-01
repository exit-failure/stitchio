from tabnanny import verbose
from django.db import models

# some common linux file systems only allow a file name length of 255 character
FILE_NAME_LENGTH_LIMIT = 255
FILE_EXTENSION_LENGTH_LIMIT = 4

# most Linux distributions allow a total path length of 4096 characters including the file name and extension

# BE AWARE that Windows per default only allows a total path length of 256 characters
# please take care of that, if you are planning on running this software on a windows system

# calculation: PATH_LENGTH/FILE_NAME_LENGTH.FILE_EXTENSION_LENGTH
PATH_LENGTH_LIMIT = 4096 - FILE_NAME_LENGTH_LIMIT - FILE_EXTENSION_LENGTH_LIMIT - 2

class File_Extension(models.Model):
	extension = models.CharField(verbose_name="Extension", max_length=4)
	extension.unique = True

	def __str__(self):
		return self.extension

class Embroidery_Machine(models.Model):
	manufacturer = models.CharField(verbose_name="Manufacturer", max_length=30, help_text='The make of the machine. 30 characters max.')
	model = models.CharField(verbose_name="Model", max_length=30, help_text='The model name of the machine. 30 characters max.')
	info = models.CharField(verbose_name="Info", max_length=100, help_text='Additional information like the location, current status or identifier if you have multiple machines of the same make and model. 100 characters max.')
	info.null = True
	info.blank = True

	def __str__(self):
		return '%s %s (%s)' % (self.manufacturer, self.model, self.info)

class Embroidery_File(models.Model):
	name = models.CharField(verbose_name="Name", max_length=FILE_NAME_LENGTH_LIMIT)
	ext = models.ForeignKey(File_Extension, on_delete=models.DO_NOTHING)
	path = models.CharField(verbose_name="Path", max_length=PATH_LENGTH_LIMIT)
	on_machine = models.ForeignKey(Embroidery_Machine, on_delete=models.DO_NOTHING)
	on_machine.null = True
	on_machine.blank = True

	def __str__(self):
		return '%s.%s (%s)' % (self.name, self.ext, self.path)
