import base64
import hashlib
import qrcode
from io import BytesIO


def calcHash(str):
    return hashlib.sha256(str.encode(encoding='UTF-8')).hexdigest()


def generateQR(id):
    domain = "config your own"  # TODO
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L
    )
    qr.add_data('https://' + domain + '/cpyPosts/view/' + str(id) + '/')
    qr.make(fit=True)

    temp = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(temp)
    base64_data = base64.b64encode(temp.getvalue())
    return 'data:image/jpg;base64,' + str(base64_data)[2:][:-1]
