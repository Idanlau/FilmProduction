# Generated by Django 3.1.3 on 2020-12-01 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20201130_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('display_img', models.ImageField(default='default.png', upload_to='media/gallery/')),
            ],
        ),
        migrations.RenameModel(
            old_name='images',
            new_name='behind_the_scenese',
        ),
    ]
