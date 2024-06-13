# Generated by Django 5.0.6 on 2024-06-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=5000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
