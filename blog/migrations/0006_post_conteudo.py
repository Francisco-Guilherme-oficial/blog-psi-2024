# Generated by Django 5.1 on 2024-10-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_noticia_pessoa_alter_post_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='conteudo',
            field=models.TextField(default='conteudo', max_length=2000),
            preserve_default=False,
        ),
    ]
