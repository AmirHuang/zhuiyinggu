from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    # app名字后台显示中文
    verbose_name = '用户管理'

    # 配置信号量
    def ready(self):
        import accounts.signals