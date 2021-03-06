# Generated by Django 2.0.5 on 2018-09-07 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0026_installerissuereply'),
    ]

    operations = [
        migrations.AddField(
            model_name='installerissue',
            name='solved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='installerissuereply',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='games.InstallerIssue'),
        ),
    ]
