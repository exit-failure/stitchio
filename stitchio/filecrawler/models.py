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
    extension = models.CharField(max_length=4)
    extension.unique = True

class Embroidery_Machine(models.Model):
	manufacturer = models.CharField(max_length=30)
	model = models.CharField(max_length=30)

class Embroidery_File(models.Model):
    name = models.CharField(max_length=FILE_NAME_LENGTH_LIMIT)
    ext = models.ForeignKey(File_Extension)
    path = models.CharField(max_length=PATH_LENGTH_LIMIT)
    on_machine = models.ForeignKey(Embroidery_Machine)
