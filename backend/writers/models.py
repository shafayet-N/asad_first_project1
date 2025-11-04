from django.db import models
from django.contrib.auth.models import User

class WriterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="writer_profile")
    bio = models.TextField(blank=True)
    expertise_domains = models.CharField(max_length=255, blank=True, help_text="Comma-separated domains")
    rate_per_word = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"WriterProfile<{self.user.username}>"
