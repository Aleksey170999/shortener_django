from django.contrib import admin

from shortener.models import URL, Template, ExcelRow


class URLAdmin(admin.ModelAdmin):
    list_display = ('uid', 'long_url')


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('uid', 'title', 'template_url')


class ExcelRowAdmin(admin.ModelAdmin):
    list_display = ('uid', 'template_passes')


admin.site.register(ExcelRow, ExcelRowAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(URL, URLAdmin)
