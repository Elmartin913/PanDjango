# Generated by Django 2.0.4 on 2018-04-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_sms_send'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sms',
            old_name='send',
            new_name='sms_send',
        ),
        migrations.AlterField(
            model_name='sms',
            name='body',
            field=models.CharField(choices=[('nietypowa_propozycja', 'Mam nie typową propozycje. Proszę o kontakt.'), ('nawoczesna_firma', 'Chcę unowocześnić moją firmę.'), ('start_up', 'Ma pomysł na start-up.'), ('www', 'Potrzebuję strony internetowej.'), ('promocja', 'Chcę przeprzowadzić akcję promocyjną.'), ('kampania', 'Potrzebuję kampanii marketingowej.'), ('reaktywacja', 'Chcę reaktywować moją listę mailingową.')], max_length=126, verbose_name='Wiadomość'),
        ),
    ]
