from django.db import models


# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to='car_images/')  # For cover image
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
  

    def __str__(self):
        return f"{self.make} {self.model}"

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='car_gallery_images/')

    def __str__(self):
        return self.car.__str__()

class CarDocument(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to='car_documents/')

    def __str__(self):
        return self.name

class CarExpense(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='expenses')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name