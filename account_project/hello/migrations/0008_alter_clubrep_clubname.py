# Generated by Django 4.1.2 on 2023-01-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_delete_mymodel_remove_clubrep_names_clubrep_clubname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubrep',
            name='clubName',
            field=models.ManyToManyField(blank=True, to='hello.clubname'),
        ),
    ]
