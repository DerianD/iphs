# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

############################
# Base de datos - tablas
class SystemIP(models.Model):
    nombre = models.CharField(max_length = 100)
    latitud = models.DecimalField(max_digits=150, decimal_places=20)
    longitud = models.DecimalField(max_digits=150, decimal_places=20)
    nombrecell = models.CharField(max_length = 100)
    ipv4 = models.CharField(max_length = 100)
    slug = models.SlugField(blank=True, unique=True)
    
    def __unicode__(self):
        return self.nombre




########################3
# Finciones - metodos
def create_slug(instance, nuevo_slug=None):
    slug = slugify(instance.nombre)
    if nuevo_slug is not None:
        slug = nuevo_slug

    qs = SystemIP.objects.filter(slug=slug)
    existe = qs.exists()
    if existe:
        nuevo_slug = "%s-%s" %(slug, qs.last().id)
        return create_slug(instance, nuevo_slug=nuevo_slug)

    return slug

def producto_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance

    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(producto_pre_save_reciever, sender=SystemIP)

