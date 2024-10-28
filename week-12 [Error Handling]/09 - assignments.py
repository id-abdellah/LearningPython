from PIL import Image, ImageFilter, ImageOps
from os import path
# assign 1

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    my_data.extend(data)

my_data = "".join(my_data).capitalize()

print(my_data) # Elzero



# assign 2

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple1 = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data1 = []

for item1, item2, item3 in zip(my_list1, my_tuple1, my_list2):
    my_data1.append(item1)

my_data1 = "".join(my_data1[:-2]).capitalize()
print(my_data1)




# assign 2

my_image = Image.open(fr"{path.dirname(__file__)}\elzero-pillow.png")


# # cropping L letter image
lImg = my_image.crop((400, 0, 800, 400))
# # Grayscale Filter
lImg = lImg.convert("L")
# # saving it
lImg.save(fr"{path.dirname(__file__)}\elzero-pillow-L.png")


# # # cropping second half
lImg2 = my_image.crop((0, 400, 1200, 800))
# # # grayscale filter
lImg2 = lImg2.convert("L")
lImg2 = ImageOps.flip(lImg2)
lImg2.save(fr"{path.dirname(__file__)}\elzero-pillow-flipped.png")




# assign 1 - second tasks


num = input("add ur number ")
if int(num) < 0:
    raise ValueError("Number must be larger than 0")
elif len(num) > 1:
    raise IndexError("Only one character allowed")
elif num not in "123456789":
    raise Exception("Only number allowe")
else:
    print("The number is ", num)