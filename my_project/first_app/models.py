from django.db import models


class Topic(models.Model):
    top_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.top_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    urls = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
