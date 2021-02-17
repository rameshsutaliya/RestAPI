from django.utils import timezone
from django.db import models

# Create your models here.


class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=150)

    class Meta:
        """Meta definition for Category."""
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class TodoList(models.Model):
    """Model definition for TodoList."""

    # TODO: Define fields here
    title = models.CharField(max_length=300)
    discription = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(
        Category, default="Primary", on_delete=models.DO_NOTHING)

    class Meta:
        """Meta definition for TodoList."""
        ordering = ["-created"]

    def __str__(self):
        """Unicode representation of TodoList."""
        return self.title
