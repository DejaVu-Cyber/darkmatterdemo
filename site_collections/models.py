from django.db import models
from django.utils import timezone
#individiual targets. will have many collections under it that can be expanded
class collection_target(models.Model):
    #fields
    type_choices = [
        ("website", "Website")
    ]
    type = models.CharField(max_length=20, choices= type_choices)
    name = models.CharField(max_length=20, unique=True)
    time_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    collected = models.BooleanField(default=False)
    #add more languages later, perhaps dialects?
    language_choices = [
        ("English", "English"),
        ("Mandarin", "Mandarin")
    ]
    language = models.CharField(max_length=20, choices=language_choices)


    def __str__(self):
        return self.name

class collection(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    translated_url = models.URLField()
    original_url = models.URLField()
    target = models.ForeignKey(collection_target, on_delete=models.CASCADE)
    collection_point = models.CharField(max_length=30)
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.target.last_modified = timezone.now()
        self.target.save(update_fields = ["last_modified"])


#Type: web page (for now other types added later)
#Date Collected: Full timestamp down to second
#Collected: Boolean (yes/no)
#Language:

