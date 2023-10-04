from django.db import models
class TwixProduct(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    def __str__(self):
        return self.name