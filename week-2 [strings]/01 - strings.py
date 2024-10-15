# ------------------------------
# --- Strings ---
#
#
#  كيردو قيمة جديدة و مكيعدلوش على القيمة الاصلية string methods اول حاجة خاص تعرفها وهي ان غاع ال
#
# ------------------------------


# للسطر escape كنا كنديرو multiple line string دبا فاللول باش طبع
# triple sigle quotes اولا triple quotes كتستعمل escape char ولكن باش فعلا طبع اكثر من سطر بلا مدير

# back slash بحال ال chars لل escape كدير triple quotes هاد ال
# escape فاخر اللاين يعني غيخدم بيه و مغديش يدير \ ولكن فاش غتحط ال

multiplLineString_1 = """first line
second line "test" 'test'
third line"""

multiplLineString_2 = '''fourth line
sixth line "test" \ 'test'
seventh line'''

print(multiplLineString_1)
print(multiplLineString_2)