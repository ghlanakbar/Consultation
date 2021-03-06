# Generated by Django 2.1.7 on 2020-03-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('date_naissance', models.DateTimeField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('sexe', models.CharField(choices=[('femme', 'Femme'), ('homme', 'Homme')], max_length=200)),
                ('groupe_sanguin', models.CharField(choices=[('o-', 'O-'), ('o+', 'O+'), ('b+', 'B+'), ('b-', 'B-'), ('a-', 'A-'), ('a+', 'A+'), ('ab-', 'AB-'), ('ab+', 'AB+')], max_length=200)),
                ('poids', models.FloatField(default=0.0)),
                ('taille', models.FloatField(default=0.0)),
                ('observations', models.CharField(max_length=2000)),
            ],
        ),
    ]
