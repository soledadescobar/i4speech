# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import django_filters
from i4speech_app import legibilidad
from django.db import models
from django.urls import reverse
from django.db.models import Avg



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Autores(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autores'

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

    class Meta:
        managed = False
        db_table = 'cr'

    def prom_cr(idautor, oca, ejes):
        prom = Cr.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_cr=Avg('resultado'))
        return prom.get('prom_cr')


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Escalafh(models.Model):
    inf = models.IntegerField(blank=True, null=True)
    sup = models.IntegerField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalafh'

    def __str__(self):
        return str(self.color)

class Escalain(models.Model):
    inf = models.IntegerField(blank=True, null=True)
    sup = models.IntegerField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalain'

    def __str__(self):
        return self.color

class Escalagu(models.Model):
    inf = models.FloatField(blank=True, null=True)
    sup = models.FloatField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalagu'

    def __str__(self):
        return self.color


class Escalasp(models.Model):
    inf = models.IntegerField(blank=True, null=True)
    sup = models.IntegerField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    tipopublicacion = models.CharField(max_length=255, blank=True, null=True)
    estudios = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalasp'

    def __str__(self):
        return str(self.color)


class Escalamu(models.Model):
    inf = models.IntegerField(blank=True, null=True)
    sup = models.IntegerField(blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalamu'

    def __str__(self):
        return self.color


class Fh(models.Model):
    idtexto = models.OneToOneField('Textos', models.DO_NOTHING, db_column='idtexto', primary_key=True, unique=True)
    resultado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'fh'

    def prom_fh(idautor, oca, ejes):
        prom = Fh.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_fh=Avg('resultado'))
        return prom.get('prom_fh')

class Gu(models.Model):
    idtexto = models.OneToOneField('Textos', models.DO_NOTHING, db_column='idtexto', primary_key=True, unique=True)
    resultado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'gu'

    def prom_gu(idautor, oca, ejes):
        prom = Gu.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_gu=Avg('resultado'))
        return prom.get('prom_gu')


class Mu(models.Model):
    idtexto = models.OneToOneField('Textos', models.DO_NOTHING, db_column='idtexto', primary_key=True, unique=True)
    resultado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mu'

    def prom_mu(idautor, oca, ejes):
        prom = Mu.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_mu=Avg('resultado'))
        return prom.get('prom_mu')

class Sp(models.Model):
    idtexto = models.OneToOneField('Textos', models.DO_NOTHING, db_column='idtexto', primary_key=True, unique=True)
    resultado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sp'

    def prom_sp(idautor, oca, ejes):
        prom = Sp.objects.filter(idtexto__idautor_id=idautor, idtexto__idocasion__in=oca,
                                 idtexto__ideje__in=ejes).aggregate(prom_sp=Avg('resultado'))
        return prom.get('prom_sp')


class Ejes(models.Model):
    eje = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ejes'

    def __str__(self):
        return self.eje


class Ocasiones(models.Model):
    ocasion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocasiones'

    def __str__(self):
        return self.ocasion


class Textos(models.Model):
    texto = models.TextField()
    idautor = models.ForeignKey('Autores', models.DO_NOTHING, db_column='idautor')
    fecha = models.DateField(blank=True, null=True)
    titulo = models.CharField(max_length=255)
    idocasion = models.ForeignKey('Ocasiones', models.DO_NOTHING, db_column='idocasion')
    ideje = models.ForeignKey(Ejes, models.DO_NOTHING, db_column='ideje', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'textos'

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

    class Meta:
        managed = False
        db_table = 'indices'


    def __str__(self):
        return self.indice