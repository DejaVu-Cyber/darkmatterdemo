from django.db import models

#individiual targets. will have many collections under it that can be expanded
class collection_target(models.Model):
    #fields
    type_choices = [
        ("website", "Website")
    ]
    type = models.CharField(max_length=20, choices= type_choices)
    name = models.CharField(max_length=20)
    time_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    collected = models.BooleanField()
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

#Type: web page (for now other types added later)
#Date Collected: Full timestamp down to second
#Collected: Boolean (yes/no)
#Language:

