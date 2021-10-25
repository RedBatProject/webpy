from django.db import models
import json
import time
# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
def function(self):
	# time.sleep(5)
	obj = {}
	obj['0']="3"
	with open('hello/static/simple.json','w+') as file:
		json.dump(obj, file)