from django.db import models
from django.db.models import Sum

class Poll(models.Model):
    TYPES_OF_POLLS = (
        ('text', 'Text'),
        ('select_one', 'Select One'),
        ('select_multiple', 'Select Multiple'),
    )
    question = models.CharField(max_length=200)
    start = models.DateField(null=True, blank=True)
    finish = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=4000, null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPES_OF_POLLS, verbose_name='Types of polls', default='text')

    def __str__(self):
        return self.question

    @property
    def total(self):
        return Option.objects.filter(poll__id=self.id).aggregate(Sum('count'))['count__sum']


class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=30, null=True, blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    def toFixed(numObj, digits=0):
        return f"{numObj:.{digits}f}"

    @property
    def percent(self):
        number = int(self.count)/int(self.poll.total)*100

        def toFixed(numObj, digits=0):
            return f"{numObj:.{digits}f}"

        if number==float(int(number)):
            return toFixed(number, digits=0)
        else:
            return toFixed(number, digits=2)







