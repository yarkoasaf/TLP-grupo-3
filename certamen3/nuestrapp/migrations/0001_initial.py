# Generated by Django 4.2.5 on 2023-11-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=300)),
                ('tipo_tipo', models.CharField(choices=[('V', 'Vacaciones'), ('F', 'Feriado'), ('S1', 'Suspención de actividades'), ('S2', 'Suspención de actividades PM'), ('P', 'Periodo Lectivo')], default='F', max_length=10)),
                ('tipo_segmento', models.CharField(choices=[('C', 'Comunidad USM'), ('E', 'Estudiante'), ('P', 'Profesor'), ('J', 'Jefe de Carrera')], default='C', max_length=10)),
            ],
        ),
    ]