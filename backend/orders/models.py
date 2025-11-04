from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    CONTENT_TYPES = [
        ("blog", "Blog Post"),
        ("web_copy", "Web Copy"),
        ("product_desc", "Product Description"),
        ("social", "Social Media Content"),
        ("technical", "Technical Writing"),
        ("other", "Other"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    title = models.CharField(max_length=200)
    content_type = models.CharField(max_length=32, choices=CONTENT_TYPES, default="blog")
    word_count = models.PositiveIntegerField(default=500)
    instructions = models.TextField()
    status = models.CharField(max_length=32, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_content_type_display()})"
