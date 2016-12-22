from django.db import models

class AlphaKnowledge(models.Model):
	question = models.CharField(max_length=200)
	response = models.CharField(max_length=500)


	def __unicode__(self):
		return self.question



class AlphaReminder(models.Model):
	reminder = models.CharField(max_length=500)

	def __unicode__(self):
		return self.reminder


