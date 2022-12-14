# Generated by Django 4.1.2 on 2022-11-11 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_crew_alter_movie_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='moviecrew',
            name='crew',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_crew', to='movies.crew'),
        ),
        migrations.AlterField(
            model_name='moviecrew',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_crew', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='moviecrew',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_crew', to='movies.role'),
        ),
    ]
