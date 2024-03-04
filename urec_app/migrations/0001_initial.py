# Generated by Django 4.2.7 on 2024-02-27 20:27

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import urec_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrecUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('count_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time_submission', models.DateTimeField(auto_now_add=True)),
                ('location_count', models.SmallIntegerField()),
                ('staff_netid', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Erp',
            fields=[
                ('filename', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1023)),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ErpUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
            ],
        ),
        migrations.CreateModel(
            name='IncidentReportIncident',
            fields=[
                ('incident_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Incident ID')),
                ('incident_nature', models.CharField(max_length=255, verbose_name='Incident Nature')),
                ('incident_description', models.TextField(max_length=1023, verbose_name='Incident Description')),
                ('action_taken', models.TextField(max_length=1023, verbose_name='Action Taken')),
            ],
            options={
                'verbose_name': 'Incident Report Incident',
            },
            bases=(models.Model, urec_app.models.ModelHelpers),
        ),
        migrations.CreateModel(
            name='InjuryIllnessReportInjury',
            fields=[
                ('injury_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Injury ID')),
                ('injury_type', models.CharField(max_length=255, verbose_name='Injury Type')),
                ('injury_description', models.TextField(max_length=1023, verbose_name='Injury Description')),
                ('care_provided', models.TextField(max_length=1023, verbose_name='Care Provided')),
            ],
            options={
                'verbose_name': 'Injury/Illness Report Injury',
                'verbose_name_plural': 'Injury/Illness Report Injuries',
            },
            bases=(models.Model, urec_app.models.ModelHelpers),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=255)),
                ('task_description', models.CharField(blank=True, max_length=255)),
                ('date_time_due', models.DateTimeField()),
                ('text_input_required', models.BooleanField(default=False)),
                ('completion_text', models.CharField(blank=True, max_length=255)),
                ('task_completion', models.BooleanField(default=False)),
                ('date_time_completion', models.DateTimeField(null=True)),
                ('staff_netid', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UrecContact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Contact ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Middle Name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Last Name')),
                ('email_address', models.EmailField(blank=True, max_length=255, verbose_name='E-Mail Address')),
                ('personal_phone_number', models.CharField(blank=True, max_length=255, verbose_name='Personal Phone Number')),
                ('home_phone_number', models.CharField(blank=True, max_length=255, verbose_name='Home Phone Number')),
                ('street_address', models.CharField(blank=True, max_length=255, verbose_name='Street Address')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='State')),
                ('zip', models.CharField(blank=True, max_length=255, verbose_name='Zip Code')),
                ('minor_status', models.CharField(max_length=255, verbose_name='Is Minor')),
            ],
            bases=(models.Model, urec_app.models.ModelHelpers),
        ),
        migrations.CreateModel(
            name='UrecFacility',
            fields=[
                ('facility_id', models.AutoField(primary_key=True, serialize=False)),
                ('facility_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Facility',
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='UrecLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=255)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='urec_app.urecfacility')),
            ],
            options={
                'verbose_name': 'Location',
            },
        ),
        migrations.CreateModel(
            name='UrecReport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Report ID')),
                ('date_time_submission', models.DateTimeField(verbose_name='Date/Time Submitted')),
                ('severity', models.CharField(choices=[('Minor', 'Minor'), ('Moderate', 'Moderate')], max_length=255, verbose_name='Severity Level')),
                ('ems_called', models.BooleanField(verbose_name='EMS / Fire Called')),
                ('police_called', models.BooleanField(verbose_name='Police Called')),
                ('staff_netid', models.CharField(max_length=255, verbose_name='Staff NetID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='urec_app.ureclocation', verbose_name='Facility / Location')),
            ],
            bases=(models.Model, urec_app.models.ModelHelpers),
        ),
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('urecreport_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='urec_app.urecreport')),
                ('activity_during_incident', models.CharField(max_length=255, verbose_name='Activity During Incident')),
            ],
            options={
                'verbose_name': 'Incident Report',
            },
            bases=('urec_app.urecreport',),
        ),
        migrations.CreateModel(
            name='IncidentReportContactPatient',
            fields=[
                ('ureccontact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='urec_app.ureccontact')),
            ],
            options={
                'verbose_name': 'Incident Report Patient Contact',
            },
            bases=('urec_app.ureccontact',),
        ),
        migrations.CreateModel(
            name='IncidentReportContactWitness',
            fields=[
                ('ureccontact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='urec_app.ureccontact')),
            ],
            options={
                'verbose_name': 'Incident Report Witness Contact',
            },
            bases=('urec_app.ureccontact',),
        ),
        migrations.CreateModel(
            name='InjuryIllnessReport',
            fields=[
                ('urecreport_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='urec_app.urecreport')),
                ('activity_causing_injury', models.CharField(max_length=255, verbose_name='Activity Causing Injury')),
            ],
            options={
                'verbose_name': 'Injury/Illness Report',
            },
            bases=('urec_app.urecreport',),
        ),
        migrations.CreateModel(
            name='InjuryIllnessReportContactPatient',
            fields=[
                ('ureccontact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='urec_app.ureccontact')),
                ('injury_illness_relation', models.CharField(default='wip', max_length=255, verbose_name='Relation to Witnesses')),
            ],
            options={
                'verbose_name': 'Injury/Illness Report Patient Contact',
            },
            bases=('urec_app.ureccontact',),
        ),
        migrations.CreateModel(
            name='InjuryIllnessReportContactWitness',
            fields=[
                ('ureccontact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='urec_app.ureccontact')),
                ('injury_illness_relation', models.CharField(default='wip', max_length=255, verbose_name='Relation to Patient')),
            ],
            options={
                'verbose_name': 'Injury/Illness Report Witness Contact',
            },
            bases=('urec_app.ureccontact',),
        ),
        migrations.CreateModel(
            name='UrecReportSpecific',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.urecreport')),
            ],
            bases=(models.Model, urec_app.models.ModelHelpers),
        ),
        migrations.AddConstraint(
            model_name='urecfacility',
            constraint=models.UniqueConstraint(fields=('facility_name',), name='unique_facility_name'),
        ),
        migrations.AddField(
            model_name='count',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='urec_app.ureclocation'),
        ),
        migrations.AddField(
            model_name='urecuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='urecuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddConstraint(
            model_name='ureclocation',
            constraint=models.UniqueConstraint(fields=('facility', 'location_name'), name='unique_facility_location_pair'),
        ),
        migrations.AddField(
            model_name='injuryillnessreportinjury',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.injuryillnessreport'),
        ),
        migrations.AddField(
            model_name='injuryillnessreportcontactwitness',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.injuryillnessreportcontactpatient'),
        ),
        migrations.AddField(
            model_name='injuryillnessreportcontactwitness',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.injuryillnessreport'),
        ),
        migrations.AddField(
            model_name='injuryillnessreportcontactpatient',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.injuryillnessreport'),
        ),
        migrations.AddField(
            model_name='incidentreportincident',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.incidentreport'),
        ),
        migrations.AddField(
            model_name='incidentreportcontactwitness',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.incidentreportcontactpatient'),
        ),
        migrations.AddField(
            model_name='incidentreportcontactwitness',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.incidentreport'),
        ),
        migrations.AddField(
            model_name='incidentreportcontactpatient',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.incidentreport'),
        ),
    ]
