import qrcode
from app.models import URL


class QRGenerator():
    def __init__(self):
        self.png_dir = "media/qr/png"
        self.svg_dir = "media/qr/svg/"
        self.pdf_dir = "media/qr/pdf/"

    def get_urls_no_qr(self):
        return URL.objects.filter(is_qr_generated=False)

    def generate_one_png(self, ins):
        data_to_qr = ins.get_short_url()
        ins_id = ins.uid
        qr_png = qrcode.make(data_to_qr)
        qr_png.save(f"{self.png_dir}{ins_id}.png")

    def generate_all(self, qs):
        counter = 0
        for ins in qs:
            self.generate_one_png(ins)
            ins.set_is_generated()
            ins.save()
            counter += 1
        print(f"{counter} QR codes generated")
