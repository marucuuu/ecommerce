from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

<<<<<<< HEAD

=======
    # Add any other fields you might need
>>>>>>> 601c6d75a269cb2bec6678887e99fec4e6f99c66
