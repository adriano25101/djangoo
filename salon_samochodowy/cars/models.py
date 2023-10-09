from django.db import models

class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class CarListing(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"Listing for {self.car}"
