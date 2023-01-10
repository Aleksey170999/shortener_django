import qrcode


class QRGenerator():
    def __init__(self):
        self.png_dir = "qrcodes/png/"
        self.svg_dir = "qrcodes/svg/"
        self.pdf_dir = "qrcodes/pdf/"

    def generate_one_png(self, ins):
        data_to_qr = ins.get_short_url()
        ins_id = ins.uid
        qr_png = qrcode.make(data_to_qr)
        qr_png.save(f"{self.png_dir}{ins_id}.png")

    def generate_all(self, qs):
        for ins in qs:
            self.generate_one_png(ins)
