import json

import pandas as pd
from django.conf import settings
from random import choice
from string import ascii_letters, digits

from app.models import ExcelRow, URL

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAIABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAIABLE_CHARS):
    """
    Creates a random string with the predetermined size
    """
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


def create_shortened_url(model_instance):
    random_code = create_random_code()
    # Gets the model class

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        # Run the function again
        return create_shortened_url(model_instance)

    return random_code


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


def create_url_from_rows(row_qs):
    counter = 0
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
        counter += 1
    print(f"{counter} urls generated")


def get_excel_rows_not_generated_url():
    return ExcelRow.objects.filter(is_url_generated=False)
