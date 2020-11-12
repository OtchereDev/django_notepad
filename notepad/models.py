from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

LABELS=(
    ('primary','primary'),
    ('secondary','secondary'),
    ('success','success'),
    ('danger','danger'),
    ('warning','warning'),
    ('info','info'),
    ('light','light'),
    ('dark','dark'),
)

class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date=models.DateTimeField(default=timezone.now)
    label=models.CharField(choices=LABELS,max_length=15)
    finished = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

    def get_delete_url(self):
        return reverse(
            'notepad:delete',kwargs={
                'pk':self.id,
            }
        )
    def get_finish_url(self):
        return reverse(
            'notepad:finish',kwargs={
                'pk':self.id,
            }
        )

    def get_recover_url(self):
        return reverse(
            'notepad:recover',kwargs={
                'pk':self.id,
            }
        )


    # def get_delete_url(self):
    #     return reverse(
    #         'finish',kwargs={
    #             pk:self.id,
    #         }
    #     )