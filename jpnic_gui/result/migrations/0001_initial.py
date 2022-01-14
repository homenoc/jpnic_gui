# Generated by Django 4.0.1 on 2022-01-14 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jpnic_gui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JPNICHandle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_date', models.DateTimeField(verbose_name='取得時刻')),
                ('is_ipv6', models.BooleanField(verbose_name='IPv6')),
                ('jpnic_handle', models.CharField(db_index=True, max_length=20, verbose_name='JPNICハンドル')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='名前')),
                ('name_en', models.CharField(db_index=True, max_length=20, verbose_name='名前(英語)')),
                ('email', models.CharField(db_index=True, max_length=50, verbose_name='メールアドレス')),
                ('org', models.CharField(db_index=True, max_length=30, verbose_name='組織名')),
                ('org_en', models.CharField(db_index=True, max_length=30, verbose_name='組織名(英語)')),
                ('division', models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='部署')),
                ('division_en', models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='部署(英語)')),
                ('tel', models.CharField(blank=True, db_index=True, max_length=20, null=True, verbose_name='部署(英語)')),
                ('fax', models.CharField(blank=True, db_index=True, max_length=20, null=True, verbose_name='部署(英語)')),
                ('update_date', models.DateTimeField(verbose_name='更新時刻')),
                ('asn', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jpnic_handle', to='jpnic_gui.jpnic')),
            ],
        ),
        migrations.CreateModel(
            name='V6List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_date', models.DateTimeField(verbose_name='取得時刻')),
                ('ip_address', models.CharField(db_index=True, max_length=100, verbose_name='IPアドレス')),
                ('network_name', models.CharField(max_length=20, verbose_name='ネットワーク名')),
                ('assign_date', models.DateTimeField(verbose_name='割振・割当年月日')),
                ('return_date', models.DateTimeField(blank=True, null=True, verbose_name='返却年月日')),
                ('org', models.CharField(db_index=True, max_length=30, verbose_name='組織名')),
                ('org_en', models.CharField(db_index=True, max_length=30, verbose_name='組織名(英語)')),
                ('resource_admin_short', models.CharField(max_length=30, verbose_name='資源管理者略称')),
                ('recep_number', models.CharField(max_length=10, verbose_name='受付番号')),
                ('deli_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='審議番号')),
                ('division', models.CharField(choices=[('allocate', '割振'), ('assign_infra', 'インフラ割当'), ('assign_user', 'ユーザ割当'), ('sub_allocate', '再割当')], max_length=30, verbose_name='区分')),
                ('post_code', models.CharField(db_index=True, max_length=20, verbose_name='郵便番号')),
                ('address', models.CharField(db_index=True, max_length=200, verbose_name='住所')),
                ('address_en', models.CharField(db_index=True, max_length=200, verbose_name='住所(英語)')),
                ('name_server', models.CharField(blank=True, max_length=100, null=True, verbose_name='ネームサーバ')),
                ('ds_record', models.CharField(blank=True, max_length=100, null=True, verbose_name='DSレコード')),
                ('notify_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='通知アドレス')),
                ('admin_jpnic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='v6lists', to='result.jpnichandle')),
                ('asn', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='v6lists', to='jpnic_gui.jpnic')),
                ('tech_jpnic', models.ManyToManyField(to='result.JPNICHandle')),
            ],
        ),
        migrations.CreateModel(
            name='V4List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_date', models.DateTimeField(verbose_name='取得時刻')),
                ('ip_address', models.CharField(db_index=True, max_length=100, verbose_name='IPアドレス')),
                ('size', models.IntegerField(verbose_name='サイズ')),
                ('network_name', models.CharField(max_length=20, verbose_name='ネットワーク名')),
                ('assign_date', models.DateTimeField(verbose_name='割振・割当年月日')),
                ('return_date', models.DateTimeField(blank=True, null=True, verbose_name='返却年月日')),
                ('org', models.CharField(max_length=30, verbose_name='組織名')),
                ('org_en', models.CharField(db_index=True, max_length=30, verbose_name='組織名(英語)')),
                ('resource_admin_short', models.CharField(max_length=30, verbose_name='資源管理者略称')),
                ('recep_number', models.CharField(max_length=10, verbose_name='受付番号')),
                ('deli_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='審議番号')),
                ('type', models.CharField(choices=[('pa', 'PA'), ('historical_pi', '歴史的PI'), ('special_pi', '特殊用途PI')], max_length=30, verbose_name='種別')),
                ('division', models.CharField(choices=[('allocate', '割振'), ('assign_infra', 'インフラ割当'), ('assign_user', 'ユーザ割当'), ('sub_allocate', 'SUBA')], max_length=30, verbose_name='区分')),
                ('post_code', models.CharField(db_index=True, max_length=20, verbose_name='郵便番号')),
                ('address', models.CharField(db_index=True, max_length=200, verbose_name='住所')),
                ('address_en', models.CharField(db_index=True, max_length=200, verbose_name='住所(英語)')),
                ('name_server', models.CharField(blank=True, max_length=100, null=True, verbose_name='ネームサーバ')),
                ('ds_record', models.CharField(blank=True, max_length=100, null=True, verbose_name='DSレコード')),
                ('notify_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='通知アドレス')),
                ('admin_jpnic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='v4lists', to='result.jpnichandle')),
                ('asn', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='v4lists', to='jpnic_gui.jpnic')),
                ('tech_jpnic', models.ManyToManyField(to='result.JPNICHandle')),
            ],
        ),
    ]
