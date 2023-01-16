from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from app.excel import ExcelUtils
from app.models import URL, Template, File

from app.api.serializers import ShortenerSerializer, ShortenerAllFieldsSerializer, TemplateAllFieldsSerializer, \
    FileSerializer
from app.qr_generator import QRGenerator


class ShortUrls(ModelViewSet):
    serializer_class = ShortenerSerializer
    queryset = URL.objects.all()
    lookup_field = 'code'

    def retrieve(self, request, *args, **kwargs):
        try:
            url_instance = URL.objects.get(code=kwargs['code'])

            serializer = ShortenerSerializer(url_instance)
            return Response(serializer.data)
        except:
            return Response(
                {"error_msg": "Ссылки с кодом '{}' не существует или срок ее жизни истек".format(kwargs['code'])})

    def list(self, request, *args, **kwargs):
        queryset = URL.objects.all()
        serializer = ShortenerAllFieldsSerializer(queryset, many=True)
        return Response(serializer.data)


class TemplateViewSet(ModelViewSet):
    serializer_class = TemplateAllFieldsSerializer
    queryset = Template.objects.all()
    lookup_field = 'title'

    def create(self, request, *args, **kwargs):
        try:
            ins = Template.objects.get(title=request.data['title'],
                                       template_url=request.data['template_url'])
            return Response(data={"msg": "Такой шаблон уже существует"})
        except:
            instance = Template(title=request.data['title'],
                                template_url=request.data['template_url'])
            instance.save()
            return Response(data={"template_title": request.data['title'],
                                  "template_url": request.data['template_url']})


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        if request.FILES:
            excel_file = request.FILES['input_excel_file']
            template_instance = Template.objects.get(uid=request.data['template_pk'])
            File.objects.create(excel=excel_file,
                                template=template_instance)
            return Response({"msg": f"file {excel_file} succesfully uploaded."})
        return Response({"msg": "No file"})
