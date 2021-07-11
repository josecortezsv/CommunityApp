import datetime
from django.db import models
from datetime import datetime
from django.utils import timezone


class Calendario(models.Model):
    mesanio = models.DateField(unique=True)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)

    def __str__(self):
        return str(self.mesanio)


class TipoCuota(models.Model):
    descripcion = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    inactiva = models.BooleanField(default=False)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)

    def __str__(self):
        return "{} ({:.2f})".format(self.descripcion, self.valor)


class TipoIngreso(models.Model):
    descripcion = models.CharField(max_length=100)
    cuentacontable = models.CharField(max_length=100)
    inactiva = models.BooleanField(default=False)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)




class TipoEgreso(models.Model):
    descripcion = models.CharField(max_length=100)
    cuentacontable = models.CharField(max_length=100)
    inactiva = models.BooleanField(default=False)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)


class TipoInmueble(models.Model):
    descripcion = models.CharField(max_length=100)
    inactiva = models.BooleanField(default=False)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)


class TipoPago(models.Model):
    descripcion = models.CharField(max_length=100)
    inactiva = models.BooleanField(default=False)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)


class CuentasBancaria(models.Model):
    descripcion = models.CharField(max_length=100)
    numerocuenta = models.CharField(max_length=50)
    cuentacontable = models.CharField(max_length=100)
    AHORRO='01'
    CORRIENTE='02'
    A_PLAZO='03'
    TIPOCUENTA_IN_CUENTABANCARIA=[
        (AHORRO, 'Ahorro'),
        (CORRIENTE, 'Corriente'),
        (A_PLAZO, 'A Plazo')
    ]
    tipocuenta=models.CharField(max_length=2, choices=TIPOCUENTA_IN_CUENTABANCARIA, default=AHORRO)
    principal = models.BooleanField()
    comentario = models.CharField(max_length=250)
    inactiva = models.BooleanField(default=False)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fechainicio = models.DateField()
    fechafinal = models.DateField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    cuotaproyecto = models.DecimalField(max_digits=5, decimal_places=2)
    numerocuotas = models.IntegerField()
    cuotaasociada = models.IntegerField()
    inactiva = models.BooleanField(default=False)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)


class Persona(models.Model):
    nombre = models.CharField(max_length=250)
    telefono = models.CharField(max_length=50)
    telefonotrabajo = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    correo = models.CharField(max_length=250)
    correoalterno = models.CharField(max_length=250)
    inactivo = models.BooleanField(default=False)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)


class Proveedore(models.Model):
    nombre = models.CharField(max_length=250)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    nit = models.CharField(max_length=50, unique=True)
    comentarios = models.TextField()
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)


class Inmueble(models.Model):
    cuentacontable = models.CharField(max_length=50, unique=True)
    tipoinmueble = models.ForeignKey(TipoInmueble, on_delete=models.PROTECT)
    numerocasa = models.CharField(max_length=5)
    tipocuota = models.ForeignKey(TipoCuota, on_delete=models.PROTECT)
    propietario = models.ForeignKey(Persona, on_delete=models.PROTECT)
    propietario_desde = models.DateField()
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)


class Ingreso(models.Model):
    fecha = models.DateField(default=timezone.now)
    mesanio = models.ForeignKey(Calendario, on_delete=models.PROTECT)
    tipoingreso = models.ForeignKey(TipoIngreso, on_delete=models.PROTECT)
    tipopago = models.ForeignKey(TipoPago, on_delete=models.PROTECT)
    numerorecibo = models.CharField(max_length=50)
    numerocasa = models.ForeignKey(Inmueble, on_delete=models.PROTECT)
    nombrerecibo = models.CharField(max_length=255)
    concepto = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    comentario = models.TextField()
    anulado = models.BooleanField(default=False)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)


class Egreso(models.Model):
    fecha = models.DateField(default=timezone.now)
    numerodocumento = models.DateField(max_length=50)
    FACTURA='01'
    RECIBO='02'
    CREDITO_FISCAL='03'
    TIPODOCUMENTO_IN_EGRESOS=[
        (FACTURA, 'factura'),
        (RECIBO, 'recibo'),
        (CREDITO_FISCAL, 'credito fiscal')
    ]
    tipodocumento=models.CharField(max_length=2, choices=TIPODOCUMENTO_IN_EGRESOS, default=FACTURA)
    proveedor = models.ForeignKey(Proveedore, on_delete=models.PROTECT)
    tipoegreso = models.ForeignKey(TipoEgreso, on_delete=models.PROTECT)
    tipopago = models.ForeignKey(TipoPago, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    numerocheque = models.CharField(max_length=255)
    anulado = models.BooleanField(default=False)
    comentarios = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)
    fechacreacion = models.DateField(default=timezone.now)
    fechamodificacion = models.DateField(default=timezone.now)
    usuariocreacion = models.CharField(max_length=30)
    usuarioactualizacion=models.CharField(max_length=30)

