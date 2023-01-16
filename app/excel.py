import json
import pandas as pd
from app.models import ExcelRow, URL, File, Template


class ExcelUtils():
    @staticmethod
    def parse_excel_file(file, template_uid):
        template_ins = Template.objects.get(uid=template_uid)
        excel_data = pd.read_excel(file)
        for i in range(len(excel_data.values)):
            res_dict = {}
            for col_name, data in excel_data.items():
                res_dict[col_name] = str(data[i])
            ins = ExcelRow(template_passes=res_dict,
                           template=template_ins)
            ins.save()

    @staticmethod
    def get_not_parsed_files():
        try:
            file = File.objects.filter(is_parsed=False).order_by("?")[0]
            return file
        except IndexError:
            pass

    def parse_not_parsed_files(self):
        file = self.get_not_parsed_files()
        if file:
            self.parse_excel_file(file.excel, template_uid=file.template.uid)
            file.set_parsed()
            file.save()
            print(f"file {file.excel.name} parsed")
