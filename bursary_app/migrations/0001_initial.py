# Generated by Django 3.2.6 on 2021-09-02 08:47

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import tree.fields
import tree.models
from tree.operations import CreateTreeTrigger


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_address', models.IntegerField()),
                ('postal_code', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('birth_cert_number', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Birth certificate number')),
                ('id_number', models.IntegerField(blank=True, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('other_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=6)),
                ('admission_no', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BursaryCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiscal_year', models.CharField(max_length=10)),
                ('allocation', models.PositiveBigIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=15, null=True, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='LearningInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Institution name')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('other_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('alive', models.BooleanField()),
                ('death_cert_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='death certificate number')),
            ],
        ),
        migrations.CreateModel(
            name='Sibling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_cert_number', models.CharField(max_length=20, verbose_name='Birth certificate number')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('other_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=6)),
                ('admission_no', models.CharField(max_length=50)),
                ('applicant', models.ManyToManyField(to='bursary_app.Applicant')),
                ('learning_institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bursary_app.learninginstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Administrative unit')),
                ('path', tree.fields.PathField()),
                ('top', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bursary_app.residence')),
            ],
            bases=(models.Model, tree.models.TreeModelMixin),
        ),
        migrations.CreateModel(
            name='ParentContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bursary_app.contact')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bursary_app.parent')),
            ],
        ),
        migrations.CreateModel(
            name='ParentalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parental_status', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=50)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bursary_app.applicant')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bursary_app.parent')),
            ],
        ),
        migrations.CreateModel(
            name='ParentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bursary_app.address')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bursary_app.parent')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='applicant_parent',
            field=models.ManyToManyField(through='bursary_app.ParentalStatus', to='bursary_app.Applicant'),
        ),
        migrations.CreateModel(
            name='InstitutionContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bursary_app.contact')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bursary_app.learninginstitution')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bursary_app.address')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bursary_app.learninginstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('branch', models.CharField(max_length=250)),
                ('account_name', models.CharField(max_length=250)),
                ('account_number', models.PositiveBigIntegerField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bursary_app.learninginstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('successful', models.BooleanField()),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='comment')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='amount awarded')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bursary_app.applicant')),
                ('application_cycle', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='bursary_app.bursarycycle')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantResidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bursary_app.applicant')),
                ('residence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bursary_app.residence')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_study', models.PositiveIntegerField()),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bursary_app.learninginstitution')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bursary_app.applicant')),
            ],
        ),
        CreateTreeTrigger('bursary_app.Residence')
    ]
