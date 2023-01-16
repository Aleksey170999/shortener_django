from django.contrib import admin

from app.models import URL, Template, ExcelRow, File


class URLAdmin(admin.ModelAdmin):
    list_display = ('uid', 'long_url', 'is_qr_generated')


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('uid', 'title', 'template_url')


class ExcelRowAdmin(admin.ModelAdmin):
    list_display = ('uid', 'template_passes', 'is_url_generated')


class FileAdmin(admin.ModelAdmin):
    list_display = ('uid', 'excel', 'is_parsed')


admin.site.register(File, FileAdmin)
admin.site.register(ExcelRow, ExcelRowAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(URL, URLAdmin)
