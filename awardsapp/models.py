from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    profile_photo = CloudinaryField('profile_photo', null=True)


class Project(models.Model):
    title = models.CharField(max_length = 60)
    project_image = CloudinaryField('project_image', null=True)
    description = models.TextField()
    link = models.CharField(max_length = 200, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    prof_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', null=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    rate_design = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
    rate_usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
    rate_content = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
