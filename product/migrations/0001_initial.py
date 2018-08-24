# Generated by Django 2.0.2 on 2018-08-22 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('votes_total', models.PositiveIntegerField()),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
                ('icon', models.ImageField(upload_to='images/')),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
