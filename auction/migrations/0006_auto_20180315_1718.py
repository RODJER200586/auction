# Generated by Django 2.0.2 on 2018-03-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20180315_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='status',
            field=models.CharField(choices=[('opened', 'Открыт'), ('closed', 'Закрыт'), ('canceled', 'Отменен')], default='opened', max_length=8, verbose_name='Статус'),
        ),
    ]
