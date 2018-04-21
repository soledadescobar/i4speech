# -*- coding: utf-8 -*-
import django_filters
from i4speech_app import legibilidad
from django.db import models
from django.urls import reverse
from django.db.models import Avg
from django.utils import encoding



class Autores(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

    #def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
     #   return reverse('model-detail-view', kwargs={ 'pk': str(self.id) })


class Cr(models.Model):
    idtexto = models.OneToOneField('Textos', models.DO_NOTHING, db_column='idtexto', primary_key=True, unique=True)
    resultado = models.FloatField()

    def prom_cr(idautor, oca, ejes):
        prom = Cr.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_cr=Avg('resultado'))
        return prom.get('prom_cr')


class Escalafh(models.Model):
    inf = models.IntegerField(blank=True, null=True)
    sup = models.IntegerField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return str(self.color)


class Escalain(models.Model):
    inf = models.IntegerField(blank=True, null=True)
    sup = models.IntegerField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.color


class Escalagu(models.Model):
    inf = models.FloatField(blank=True, null=True)
    sup = models.FloatField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.color


class Escalasp(models.Model):
    inf = models.IntegerField(blank=True, null=True)
    sup = models.IntegerField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    tipopublicacion = models.CharField(max_length=255, blank=True, null=True)
    estudios = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return str(self.color)


class Escalamu(models.Model):
    inf = models.IntegerField(blank=True, null=True)
    sup = models.IntegerField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.color


class Fh(models.Model):
    idtexto = models.OneToOneField('Textos', models.DO_NOTHING, db_column='idtexto', primary_key=True, unique=True)
    resultado = models.FloatField()

    def prom_fh(idautor, oca, ejes):
        prom = Fh.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_fh=Avg('resultado'))
        return prom.get('prom_fh')


class Gu(models.Model):
    idtexto = models.OneToOneField('Textos', models.DO_NOTHING, db_column='idtexto', primary_key=True, unique=True)
    resultado = models.FloatField()

    def prom_gu(idautor, oca, ejes):
        prom = Gu.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_gu=Avg('resultado'))
        return prom.get('prom_gu')


class Mu(models.Model):
    idtexto = models.OneToOneField('Textos', models.DO_NOTHING, db_column='idtexto', primary_key=True, unique=True)
    resultado = models.FloatField()

    def prom_mu(idautor, oca, ejes):
        prom = Mu.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_mu=Avg('resultado'))
        return prom.get('prom_mu')


class Sp(models.Model):
    idtexto = models.OneToOneField('Textos', models.DO_NOTHING, db_column='idtexto', primary_key=True, unique=True)
    resultado = models.FloatField()

    def prom_sp(idautor, oca, ejes):
        prom = Sp.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_sp=Avg('resultado'))
        return prom.get('prom_sp')


class Ejes(models.Model):
    eje = models.CharField(max_length=255)

    def __str__(self):
        return self.eje


class Ocasiones(models.Model):
    ocasion = models.CharField(max_length=255, blank=True, null=True)

    @encoding.python_2_unicode_compatible
    def __str__(self):
        return encoding.smart_str(self.ocasion)


class Textos(models.Model):
    texto = models.TextField()
    idautor = models.ForeignKey('Autores', models.DO_NOTHING, db_column='idautor')
    fecha = models.DateField(blank=True, null=True)
    titulo = models.CharField(max_length=255)
    idocasion = models.ForeignKey('Ocasiones', models.DO_NOTHING, db_column='idocasion')
    ideje = models.ForeignKey(Ejes, models.DO_NOTHING, db_column='ideje', blank=True, null=True)

    def __str__(self):
        return self.texto

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        cr = Cr.objects.create(idtexto=self,resultado=legibilidad.crawford(self.texto))
        cr.save()
        mu = Mu.objects.create(idtexto=self,resultado=legibilidad.mu(self.texto))
        mu.save()
        fh = Fh.objects.create(idtexto=self,resultado=legibilidad.fernandez_huerta(self.texto))
        fh.save()
        sp = Sp.objects.create(idtexto=self,resultado=legibilidad.szigriszt_pazos(self.texto))
        sp.save()
        gu = Gu.objects.create(idtexto=self,resultado=legibilidad.gutierrez(self.texto))
        gu.save()

    def get_absolute_url(self):
        return reverse('textodetalle', kwargs={'pk': self.id})

    def savefromcsv(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.


class Indices (models.Model):
    indice = models.TextField(default='1')
    sigla = models.TextField()

    @encoding.python_2_unicode_compatible
    def __str__(self):
        return  encoding.smart_str(self.indice)