from rest_framework.serializers import ModelSerializer

from shortener.models import URL, Template


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
