from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=128)
    profile_picture = models.CharField(max_length=256)
    languages = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name


class Subscription(models.Model):
    user_id = models.IntegerField()

    def __str__(self):
        return str(self.user_id)

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    profile_picture = models.CharField(max_length=256)
    suscribed = models.BooleanField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    prev_suscriber = models.BooleanField()

    def __str__(self):
        return self.first_name

class Fan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SavedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)

    def __str__(self):
        return self.content[:25]

class Topic(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    header_image = models.CharField(max_length=512, blank=True)
    fans = models.ForeignKey(Fan, blank=True, on_delete=models.CASCADE)
    saved = models.ForeignKey(SavedItem, blank=True, on_delete=models.CASCADE)
    user_comments = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True )
    content = models.TextField()
    parent_course = models.ForeignKey(Course,on_delete=models.CASCADE,  blank=True)
    parent_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    prog_lang = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:28]
