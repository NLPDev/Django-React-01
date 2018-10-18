from django.db import models

# Create your models here.
class Lead(models.Model):
	"""docstring for Lead"""

	name=models.CharField(max_length=100)
	email=models.EmailField()
	message=models.CharField(max_length=300)
	created_at=models.DateTimeField(auto_now_add=True)

	
	# def __init__(self, arg):
	# 	super(Lead, self).__init__()
	# 	self.arg = arg
		