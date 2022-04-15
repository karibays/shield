from django.db import models


class Products(models.Model):
    p_name = models.CharField(max_length=150)
    p_type = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    p_price = models.IntegerField()
    p_amount = models.IntegerField()

    def __str__(self):
        return self.p_name

    class Meta:
        ordering = ['p_type']