# ------------------------------------
# --- Tuples Methods p1 ---
# ------------------------------------
#
# [1] Tuple items are enclosed in parentheses
# [2] * You can remove parenthese if u want to
# [3] Tuple are ordered, use indexing to access theme
# [4] * Tuple are immutable. which means u cannot add/edit/remove
# [5] Tuple items is not unique
# [6] Tuple can have different data types
# ------------------------------------


# parentheses هوما عناصر بيانات مقفولين بال tuple ال
# وتقد تستغني عن الاقواس لبغيتي

myTuple1 = ("ahmed", 2, "Mohamed", True)
myTuple2 = "Mohamed", False, "Obito"

print(myTuple1, type(myTuple1)) # ('ahmed', 2, 'Mohamed', True) <class 'tuple'>
print(myTuple2, type(myTuple2)) # ('Mohamed', False, 'Obito') <class 'tuple'>



# باش توصل ليهم index عبارة عن عناصر مرتبة وتقد تستعمل ال tuple قاليك اسيدي ال

myTuple3 = (1, 2, 3, ["a", "b", "c"], 4)

print(myTuple3[0]) # 1
print(myTuple3[-1]) # 4
print(myTuple3[-2][-1]) # c



# يعني متقد لا تضيف ولا تعدل ولا تمسح immutable كتعتابر tuples ال
# بمعنى اخر للقراءة فقط

myTuple4 = (1, 2, 3, 4)
# myTuple4[0] = "One" # TypeError: 'tuple' object does not support item assignment



# يعني تقد تحط عناصر معاودة unique ماشي tuples ايضا العناصر فال
# و تقد تحط اي نوع بيانات بغيتي