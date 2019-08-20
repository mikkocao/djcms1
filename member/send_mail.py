import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'djcms.settings'

if __name__ == '__main__':

    send_mail(
        '来自www的测试邮件',
        '欢迎访问www这里是xx站点，本站专注于xx内容的分享！',
        'mizuno@163.com',
        ['mikkocao@qq.com'],
    )


