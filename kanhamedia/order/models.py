from django.db import models

# Create your models here.
class Template(models.Model):
    template_name   = models.CharField(max_length=100)
    image_link      = models.TextField()
    demo_link       = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.template_name
    
class Hosting(models.Model):
    type_hosting    = models.CharField(max_length=50)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type_hosting
    
class User(models.Model):
    no_ktp          = models.CharField(max_length=20)
    name            = models.CharField(max_length=100)
    email           = models.CharField(max_length=100)
    password        = models.CharField(max_length=255)
    no_phone        = models.CharField(max_length=15)
    files_link      = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    PENDING         = 'pending'
    COMPLETED       = 'completed'
    FAILED          = 'Failed'
    PAYMENT_STATUS  = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]

    domain_name     = models.CharField(max_length=100)
    payment_status  = models.CharField(max_length=10, choices=PAYMENT_STATUS, default=PENDING )
    id_user         = models.ForeignKey(User, on_delete=models.CASCADE)
    id_template     = models.ForeignKey(Template, on_delete=models.CASCADE)
    id_hosting      = models.ForeignKey(Hosting, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domain_name