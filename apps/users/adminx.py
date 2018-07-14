import xadmin
from .models import EmailVerifyRecord, Banner

class GlobalSettings(object):
    # 修改title
    site_title = '后台管理界面'
    # 修改footer
    site_footer = 'Hjz'
    # 收起菜单
    menu_style = 'accordion'


#xadmin中这里是继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']

class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

# 将基本配置管理与view绑定
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)

# 将title和footer信息进行注册
xadmin.site.register(xadmin.views.CommAdminView,GlobalSettings)