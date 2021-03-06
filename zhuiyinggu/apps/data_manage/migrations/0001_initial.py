# Generated by Django 2.0.2 on 2018-10-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, help_text='请填写相关描述信息', max_length=200)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('book_type', models.CharField(choices=[['Hacker', [('book_type1', 'Python'), ('book_type2', 'Linux'), ('book_type3', '网络'), ('book_type4', '运维'), ('book_type5', '数据库'), ('book_type6', '前端'), ('book_type7', '测试')]], ('book_type7', '历史'), ('book_type8', '人物传记'), ('book_type9', '技能、训练'), ('book_type10', '思想哲学'), ('book_type11', 'IT行业'), ('book_type12', '小说'), ('book_type13', '其他')], max_length=20)),
                ('book_step', models.CharField(choices=[('book_step1', '待下载'), ('book_step2', '已下载'), ('book_step3', '已审核'), ('book_step4', '阅读中'), ('book_step5', '已读完')], max_length=20)),
                ('book_file', models.FileField(blank=True, upload_to='date_manage/book/')),
                ('creator', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '书籍管理',
                'verbose_name_plural': '书籍管理',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, help_text='请填写相关描述信息和备注')),
                ('game_type', models.CharField(blank=True, choices=[('game_type1', '射击'), ('game_type2', '第一人称射击'), ('game_type3', '第三人称射击'), ('game_type4', '动作'), ('game_type5', '角色扮演'), ('game_type6', '动作角色扮演'), ('game_type7', '策略'), ('game_type8', '竞速'), ('game_type9', '模拟器'), ('game_type10', '休闲')], max_length=20)),
                ('game_step', models.CharField(blank=True, choices=[('movie_step1', '待下载'), ('movie_step2', '已下载'), ('movie_step3', '已审核')], max_length=20)),
                ('seed_address', models.CharField(blank=True, max_length=200)),
                ('seed_type', models.CharField(blank=True, choices=[('seed_address1', '百度云'), ('seed_address2', '迅雷')], max_length=50)),
                ('creator', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '游戏管理',
                'verbose_name_plural': '游戏管理',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, help_text='请填写相关描述信息', max_length=200)),
                ('movie_type', models.CharField(blank=True, choices=[['电影', [('movie_type1', '大陆'), ('movie_type2', '香港'), ('movie_type3', '美国'), ('movie_type4', '欧洲'), ('movie_type5', '日韩'), ('movie_type6', '东南亚'), ('movie_type7', '其他')]], ['电视剧', [('movie_type8', '大陆'), ('movie_type9', '香港'), ('movie_type10', '美国'), ('movie_type11', '欧洲'), ('movie_type12', '日韩'), ('movie_type13', '其他')]]], max_length=20)),
                ('movie_step', models.CharField(blank=True, choices=[('movie_step1', '待下载'), ('movie_step2', '已下载'), ('movie_step3', '已审核')], max_length=20)),
                ('seed_address', models.CharField(blank=True, max_length=200)),
                ('seed_type', models.CharField(blank=True, choices=[('seed_address1', '百度云'), ('seed_address2', '迅雷')], max_length=50)),
                ('creator', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '电影管理',
                'verbose_name_plural': '电影管理',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, help_text='请填写相关描述信息', max_length=200)),
                ('singer', models.CharField(blank=True, max_length=50)),
                ('album', models.CharField(blank=True, max_length=100)),
                ('music_format', models.CharField(blank=True, choices=[('music_format1', 'FLAC'), ('music_format2', 'APE'), ('music_format3', 'mp3'), ('music_format4', 'WAV'), ('music_format5', '其他')], max_length=20)),
                ('music_type', models.CharField(blank=True, choices=[('music_type1', '轻音乐'), ('music_type2', '流行歌曲'), ('music_type3', '其他')], max_length=20)),
                ('music_step', models.CharField(blank=True, choices=[('book_step1', '待下载'), ('book_step2', '已下载'), ('book_step3', '已审核')], max_length=20)),
                ('music_file', models.FileField(blank=True, upload_to='date_manage/music/')),
                ('creator', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '音乐管理',
                'verbose_name_plural': '音乐管理',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, help_text='请填写相关描述信息', max_length=200)),
                ('video_type', models.CharField(blank=True, choices=[('video_type1', 'IT'), ('video_type2', '社会'), ('video_type3', '演讲'), ('video_type4', '科教'), ('video_type5', '纪录片'), ('video_type6', '其他')], max_length=20)),
                ('video_step', models.CharField(blank=True, choices=[('video_step1', '待下载'), ('video_step2', '已下载'), ('video_step3', '已审核')], max_length=20)),
                ('seed_address', models.CharField(blank=True, max_length=200)),
                ('seed_type', models.CharField(blank=True, choices=[('seed_address1', '百度云'), ('seed_address2', '迅雷')], max_length=50)),
                ('creator', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '视频管理',
                'verbose_name_plural': '视频管理',
                'ordering': ('name',),
            },
        ),
    ]
