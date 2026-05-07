from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha', '0009_dori_foydalanuvchi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BolalarMalumot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=200, verbose_name='Sarlavha')),
                ('matn', models.TextField(verbose_name='Matn')),
                ('icon', models.CharField(default='📌', max_length=50, verbose_name='Icon (emoji)')),
                ('rang', models.CharField(default='#3b82f6', max_length=7, verbose_name='Rang kodi')),
                ('tartib', models.PositiveIntegerField(default=0, verbose_name='Tartib')),
            ],
            options={
                'verbose_name': "Bolalar ma'lumoti",
                'verbose_name_plural': "Bolalar ma'lumotlari",
                'ordering': ['tartib'],
            },
        ),
        migrations.AddField(
            model_name='videoqollanma',
            name='video_fayl',
            field=models.FileField(blank=True, null=True, upload_to='videolar/fayllar/', verbose_name='Video fayl (MP4)'),
        ),
        migrations.AlterField(
            model_name='videoqollanma',
            name='youtube_url',
            field=models.URLField(blank=True, verbose_name='YouTube havolasi'),
        ),
    ]
