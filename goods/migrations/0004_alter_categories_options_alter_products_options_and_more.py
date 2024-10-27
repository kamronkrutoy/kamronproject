# Generated by Django 5.1.2 on 2024-10-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_categories_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка в %'),
        ),
        migrations.AlterModelTable(
            name='categories',
            table='goods_category',
        ),
        migrations.AlterModelTable(
            name='products',
            table='goods_product',
        ),
    ]
