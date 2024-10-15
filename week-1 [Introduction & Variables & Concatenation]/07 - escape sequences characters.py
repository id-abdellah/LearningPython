# ------------------------------------
# --- Escape Sequencese characters ---
# ------------------------------------
#
# 
# \     => Escape new line and \ itself
# \"    => Escape double quote
# \'    => Escape single quote
# \b    => Back space
# \n    => Line feed (new line)
# \r    => Carriage return
# \t    => Horizontal tab
# ------------------------------------

# طبعا هاد الموضوع انا عارفو من قبل
# special character كتعتابر back slash \ وهو ان ال
# معينة. functionality يعني عندها شي حروف فاش كيجيو مراها كيديرو شي



# Back space
# كيتمسح الحرف او الكاراكتر لي قبل منها back space هاد ال
print("Hello\bPython") # HellPython



# Escape new line
# للسطورة escape على اكثر من نص لهذا يمكن ليك دير string بطبيعة الحال ميمكنش ليك تفرق ال
print("hello \
python")


# Line feed
print("first line\nsecond line")


# Carriage return
# هادي كتاخذ غاع الكاراكترز لي قدامها وتبدلهم ليهم البلاصة وتحطهم فاللول بنفس الطول
# شوف غا المثال التحت غتفهم
print("123456\rabc") # abc456
print("123456\rabcd") # abcd56
print("123456\rabcde") # abcde6



# Horizontal tab
print("Obito\tUchiha") # Obito   Uchiha



# Hex value
# ديال شي كراكتر وكيرجع ليك الكراكتر باللغة الانجليزية hex value هادي كتعطيها ال
print("\x4F") # O
print("\x46") # E
print("\x50") # P