from django.test import TestCase

from .models import Type

# Create your tests here.

query = Type.objects.all()
print(query)

t = Type()
t.name = "Limpieza"
t.save()

t = Type.objects.get(id = 1)
print(t)
t.name = "Supervisor"
t.save()

# t = Type.objects.get(id = 11)
# t.delete()

t = Type.objects.filter(name__icontains = "li").count()
print(t)

t = Type.objects.filter(name__startswith = "se")
print(t)
