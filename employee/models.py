from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    hire_date = models.DateField(auto_now_add=True)
    salary = models.IntegerField()
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    def __str__(self) -> str:
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ['name']
