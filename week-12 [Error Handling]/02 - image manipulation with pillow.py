# -----------------------------------------------------------
# ---- Pillow: image manipulation ----
# -----------------------------------------------------------
#
# -----------------------------------------------------------

from os import path

from PIL import Image


# Open the image

myImage = Image.open(fr"{path.dirname(__file__)}\testimg.jpg")

# show image

myImage.show()


# rotate image and save it

rotatedImg = myImage.rotate(60)

rotatedImg.save(fr"{path.dirname(__file__)}\rotated.jpeg", "jpeg")


# كاينة ولي كدير اي حاجة بغيتيها على الصور pillow هاد ال الدرس فقط باش نعرفو بلي حاجة بحال
# بحد داتو كبييير بزاااف module ال