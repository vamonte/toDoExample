from django.db import models


class Todo(models.Model):
    PENDING = 'pending'
    FINISHED = 'finished'
    CLOSED = 'closed'
    STATUS_CHOICES = ((PENDING, 'pending'),
                      (FINISHED, 'finished'),
                      (CLOSED, 'closed'))

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default=PENDING)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title
