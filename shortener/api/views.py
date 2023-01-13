from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from shortener.excel import ExcelUtils
from shortener.models import URL, Template

from shortener.api.serializers import ShortenerSerializer, ShortenerAllFieldsSerializer, TemplateAllFieldsSerializer
from shortener.qr_generator import QRGenerator


class ShortUrls(ModelViewSet):
    serializer_class = ShortenerSerializer
    queryset = URL.objects.all()
    lookup_field = 'code'

    def create(self, request, *args, **kwargs):
        """
        Нам приходят: номер шаблона и файл эксель, или его ID
        Нам нужно распарсить эксель, проитерироваться по строкам в нем и подставить значения из строк в шаблон
        Получившуюся ссылку нужно сохранить в URL и сделать возможным получение сокращенной версии этой ссылки из URL
        """
        if request.FILES:
            excel_file = request.FILES['input_excel_file']
            template_instance = Template.objects.get(uid=request.data['template_pk'])

            qs = ExcelUtils.create_excel_row(excel_file, template_instance)
            url_qs = []
            for q in qs:
                url_qs.append(ExcelUtils.create_url_from_rows(q))
            qr_gen = QRGenerator()
            qr_gen.generate_all(url_qs)

            return Response({"msg": f"Сгенерировано {len(url_qs)} ссылок"})

        return Response({"msg": "No file"})

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
