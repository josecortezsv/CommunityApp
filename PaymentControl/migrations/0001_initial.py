# Generated by Django 2.2.5 on 2021-07-11 02:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesanio', models.DateField(unique=True)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CuentasBancarias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('cuenta', models.CharField(max_length=50)),
                ('tipocuenta', models.CharField(choices=[('01', 'Ahorro'), ('02', 'Corriente'), ('03', 'A Plazo')], default='01', max_length=2)),
                ('principal', models.BooleanField()),
                ('comentario', models.CharField(max_length=250)),
                ('inactiva', models.BooleanField(default=False)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=50)),
                ('telefonotrabajo', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=250)),
                ('correoalterno', models.CharField(max_length=250)),
                ('inactivo', models.BooleanField(default=False)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=250)),
                ('nit', models.CharField(max_length=50, unique=True)),
                ('comentarios', models.TextField()),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('fechainicio', models.DateField()),
                ('fechafinal', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cuotaproyecto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('numerocuotas', models.IntegerField()),
                ('cuotaasociada', models.IntegerField()),
                ('inactiva', models.BooleanField(default=False)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCuotas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inactiva', models.BooleanField(default=False)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEgresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
                ('inactiva', models.BooleanField(default=False)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoIngresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
                ('inactiva', models.BooleanField(default=False)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInmuebles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('inactiva', models.BooleanField(default=False)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('inactiva', models.BooleanField(default=False)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Inmuebles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuentacontable', models.CharField(max_length=50, unique=True)),
                ('numerocasa', models.CharField(max_length=5)),
                ('propietario_desde', models.DateField()),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.Personas')),
                ('tipocuota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.TipoCuotas')),
                ('tipoinmueble', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.TipoInmuebles')),
            ],
        ),
        migrations.CreateModel(
            name='Ingresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('numerorecibo', models.CharField(max_length=50)),
                ('nombrerecibo', models.CharField(max_length=255)),
                ('concepto', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comentario', models.TextField()),
                ('anulado', models.BooleanField(default=False)),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
                ('mesanio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.Calendarios')),
                ('numerocasa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.Inmuebles')),
                ('tipoingreso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.TipoIngresos')),
                ('tipopago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.TipoPagos')),
            ],
        ),
        migrations.CreateModel(
            name='Egresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('numerodocumento', models.DateField(max_length=50)),
                ('tipodocumento', models.CharField(choices=[('01', 'factura'), ('02', 'recibo'), ('03', 'credito fiscal')], default='01', max_length=2)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numerocheque', models.CharField(max_length=255)),
                ('anulado', models.BooleanField(default=False)),
                ('comentarios', models.TextField()),
                ('fechacreacion', models.DateField(default=django.utils.timezone.now)),
                ('fechamodificacion', models.DateField(default=django.utils.timezone.now)),
                ('usuariocreacion', models.CharField(max_length=30)),
                ('usuarioactualizacion', models.CharField(max_length=30)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.Proveedores')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.Proyectos')),
                ('tipoegreso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.TipoEgresos')),
                ('tipopago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PaymentControl.TipoPagos')),
            ],
        ),
    ]