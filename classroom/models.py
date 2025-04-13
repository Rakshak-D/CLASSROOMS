from django.db import models

class Block(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('free', 'Free'), ('occupied', 'Occupied')], default='free')

    def __str__(self):
        return f"{self.name} ({self.block.name})"
