from typing import List

import pandas as pd

from shortener.models import ExcelRow, URL


def get_excel_data(file):
    return pd.read_excel(file)


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


def create_url_from_row(ins):
    dict_passes: dict = ins.template_passes
    url = ins.template.template_url
    for k in dict_passes.keys():
        url = url.replace("{" + f"{k}" + "}", dict_passes[k])
    url_ins = URL(long_url=url,
                  template=ins.template)
    url_ins.save()
    return url_ins
