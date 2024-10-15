# ------------------------------------
# --- Numbers ---
# ------------------------------------
#
# 3 numbers data types => int, float, complex
#
# [1] u can convert from "Int" to "float, complex"
# [2] u can convert from "Float" to "int, complex"
# [3] u cann't convert "Complex to any type"
# ------------------------------------


# عندنا تلاتة انواع ديال الارقام python فال
# لي هو عدد عشري float لي هو عدد صحيح و ال int عندنا ال
# complex numbers وعندنا نوع اخر خاص بالمهندسين وغير مستعمل بكثرة ولي هما الاعداد العقدية او ال

intNum = 100
floatNum = 100.99
complexNum = 9+2j

print(type(intNum)) # int
print(type(floatNum)) # float
print(type(complexNum)) # complex

# بالنسبة للاعداد العقدية وكما قريت فالباك فهوما كيتكونو من جوج اجزاء الجزء الحقيقي و التخيلي
# python تقد تفصل او تطبع الجزء لي بغيتي فال

print("real part is: {}".format(complexNum.real)) # real part is: 9.0
print("imaginary part is: {}".format(complexNum.imag)) # imaginary part is: 2.0




# هو الوحيد لي متقدش تحولو للانواع لوخرين complex وبالنسبة للتحويلات بيناتهم ف ال
# ديال انواع البيانات constructor وكما غتلاحظ التحت فطريقة التحويل كتم باستعمال ال
aFloatNum = 9.5

print(complex(aFloatNum)) # (9.5+0j)
print(int(aFloatNum)) # 9

aIntNum = 8

print(complex(aIntNum)) # (8+0j)
print(float(aIntNum)) # 8.0