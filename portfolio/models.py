from django.db import models

class Bio(models.Model):
	name = models.CharField(max_length = 100, blank = True, null = True)
	role = models.CharField(max_length = 100, blank = True, null = True)
	email = models.CharField(max_length = 100, blank = True, null = True)
	github = models.CharField(max_length = 100, blank = True, null = True)
	linkedin = models.CharField(max_length = 100, blank = True, null = True)
	welcome_message = models.CharField(max_length = 100, blank = True, null = True)
	
	def __str__(self):
		return self.name

class Skill(models.Model):
	name = models.CharField(max_length = 100, blank = True, null = True)
	icon = models.CharField(max_length = 100, blank = True, null = True)
	
	def __str__(self):
		return self.name
	
class School(models.Model):
	title = models.CharField(max_length = 100, blank = True, null = True)
	name = models.CharField(max_length = 100, blank = True, null = True)
	icon = models.CharField(max_length = 100, blank = True, null = True)
	location = models.CharField(max_length = 100, blank = True, null = True)
	degree_type = models.CharField(max_length = 100, blank = True, null = True)
	major = models.CharField(max_length = 100, blank = True, null = True)
	grad_date = models.DateField(auto_now=False, blank = True, null = True)
	url = models.CharField(max_length = 100, blank = True, null = True)
	
	def __str__(self):
		return self.name
		
class Work(models.Model):
	employer = models.CharField(max_length = 100, blank = True, null = True)
	title = models.CharField(max_length = 100, blank = True, null = True)
	location = models.CharField(max_length = 100, blank = True, null = True)
	start_date = models.DateField(auto_now=False, blank = True, null = True)
	end_date = models.DateField(auto_now=False, blank = True, null = True)
	url = models.CharField(max_length = 100, blank = True, null = True)
	description = models.CharField(max_length = 200, blank = True, null = True)
	
	def __str__(self):
		return self.employer
	
class Project(models.Model):
	title = models.CharField(max_length = 100, blank = True, null = True)
	date = models.DateField(auto_now=False, blank = True, null = True)
	description = models.CharField(max_length = 200, blank = True, null = True)
	image = models.CharField(max_length = 100, blank = True, null = True)
	url = models.CharField(max_length = 100, blank = True, null = True)
	
	def __str__(self):
		return self.title
	
class ProjectSkill(models.Model):
	skill = models.ForeignKey(Skill, on_delete=models.CASCADE, blank = True, null = True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, blank = True, null = True)
	
