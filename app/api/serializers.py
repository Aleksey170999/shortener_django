from rest_framework.serializers import ModelSerializer

from app.models import URL, Template, File


class ShortenerSerializer(ModelSerializer):
    class Meta:
        model = URL
        fields = ['created_at', 'long_url', 'template']


class ShortenerAllFieldsSerializer(ModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'


class TemplateAllFieldsSerializer(ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'