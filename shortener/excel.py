import json
import pandas as pd
from shortener.models import ExcelRow, URL, File, Template


class ExcelUtils():
    def parse_excel_file(self, file, template_uid):
        template_ins = Template.objects.get(uid=template_uid)
        excel_data = pd.read_excel(file)
        for i in range(len(excel_data.values)):
            res_dict = {}
            for col_name, data in excel_data.items():
                res_dict[col_name] = str(data[i])
            ins = ExcelRow(template_passes=res_dict,
                           template=template_ins)
            ins.save()

    def get_not_parsed_files(self):
        return File.objects.filter(is_parsed=False)

    def parse_not_parsed_files(self):
        qs = self.get_not_parsed_files()
        for file in qs:
            self.parse_excel_file(file.excel, template_uid=file.template.uid)
            file.set_parsed()
            file.save()

    @staticmethod
    def create_excel_row(excel_file, tmp_ins):
        excel_data = pd.read_excel(excel_file)
        qs = []
        for i in range(len(excel_data.values)):
            res_dict = {}
            for col_name, data in excel_data.items():
                res_dict[col_name] = str(data[i])
            ins = ExcelRow(template_passes=res_dict,
                           template=tmp_ins)
            ins.save()
            qs.append(ins)
        return qs

    def create_url_from_rows(self, row_qs):
        for row in row_qs:
            dict_passes = json.loads(row.template_passes)
            url = row.template.template_url
            for k in dict_passes.keys():
                url = url.replace("{" + f"{k}" + "}", dict_passes[k])
            url_ins = URL(long_url=url,
                          template=row.template)
            url_ins.save()
            row.set_is_url_generated()
            row.save()

    def get_excel_rows_not_generated_url(self):
        return ExcelRow.objects.filter(is_url_generated=False)
