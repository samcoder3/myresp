from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	name=models.CharField(max_length=255)
	email=models.EmailField(blank=True, null=True)
	bio=models.TextField()
	profile_pic=models.ImageField(null=True, blank=True, upload_to='profile')
	facebook_url=models.CharField(max_length=255,null=True,blank=True)
	instagram_url=models.CharField(max_length=255,null=True,blank=True)
	twitter_url=models.CharField(max_length=255,null=True,blank=True)

	def __str__(self):
		return str(self.user)



class Post(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User, default=True, on_delete=models.CASCADE)
	body=models.TextField()
	images=models.ImageField(null=True, blank=True, upload_to='images/')
	date_created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title + '|' + str(self.author)

class Comment(models.Model):
	post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	name=models.CharField(max_length=255)
	body=models.TextField()
	date_commented=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)