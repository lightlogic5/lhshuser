# Generated by Django 2.1.4 on 2018-12-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrintForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_category', models.CharField(max_length=200, verbose_name='故障类型')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='提交日期')),
                ('receive_date', models.DateTimeField(blank=True, null=True, verbose_name='接收日期')),
                ('over_date', models.DateTimeField(blank=True, null=True, verbose_name='处理完毕日期')),
                ('back_date', models.DateTimeField(blank=True, null=True, verbose_name='取回日期')),
                ('repair_man', models.CharField(max_length=200, verbose_name='报修人')),
                ('unit', models.CharField(max_length=200, verbose_name='报修单位')),
                ('content', models.TextField(verbose_name='故障描述')),
                ('telephone', models.TextField(verbose_name='联系电话')),
                ('state', models.CharField(choices=[('1', '提交中'), ('2', '已接收'), ('3', '已修好'), ('4', '已确认取回')], default=1, max_length=1)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='管理员备注')),
            ],
        ),
    ]