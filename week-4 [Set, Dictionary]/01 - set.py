# --------------------------------------
# ---- Set ----
# 
#
# [1] Set items are enclosed in curly braces {}
# [2] Set items are not ordered, and not indexed, and cant be sliced
# [3] Set can only contains immutable data types (number, string, boolean, Tuple). "List, Dict" are not
# [4] Set items are unique
# --------------------------------------


# هنايا مختالفة شوية set ال js دبا على عكس ال
# curly braces حيت اولا العناصر ديالها كيدارو وسط ال
# التحت كل مرة كيطلع ليك ترتيب معين للعناصر print العناصر غير مرتبة يعني فال
# set مخداماش فال slicing و ال indexing المسايل ديال ال

mySet = {"mohamed", "Obito", 100, True}

print(type(mySet)) # <class set>

print(mySet) # {'Obito', True, 'mohamed', 100}




# اتحطو فيها numbers string tuple كتقبل فقط set ال
# مكتقبلهمش list dict اما ال

mySet_2 = {"str", 100, True, (1, 2, 3)}
# mySet_3 = {"str", 100, True, (1, 2, 3), ["a", "b"]} # TypeError: unhashable type: "list"





# يعني مكيقبلوش التكرار unique كيكونو set عناصر ال js وكما فال

mySet_3 = {1, 2, 1, "a", "a", (1, 2), (1, 2)}
print(mySet_3) # {1, 2, (1, 2), 'a'}