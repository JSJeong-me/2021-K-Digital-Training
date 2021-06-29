from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        managed = False

class Publisher(BaseModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    is_active = models.BooleanField()
    
    def __str__(self):
        return "{}: {}".format(self.id, self.name)

    class Meta:
        managed = False
        db_table = 'publisher'
