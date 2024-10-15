# --------------------------------------
# ---- Set Methods p1----
# --------------------------------------
#
# clear() => clears a set
# union(sets)
#   return a union of sets as new set
#   u can also use pipeline to union sets => {1, 2} | {3, 4}
#
# add(value) => add a new element to set 
# copy() => return a shallow copy of a set
#
# remove(value)
#   remove a value from a set
#   if value does not exist, will throw an error
# discard(value)
#   also remove a value from a set
#   but, if value does not exist. won't throw any thin
#
# pop() => return and remove an arbitrary element from set
# update(iterable) => Update a set with the union of itself and other iterables.
# --------------------------------------



# --------------------------------------
# clear()

a = {"a", 2, 3, True}
a.clear()
print(a) # set()



# --------------------------------------
# union(Sets)

# وحدة set ف set وكتعني اتحاد اي انك كدمج كتير من

# هاد العملية كتم عن طريق جوج طرق
# union method يما تستعمل ال
# pipeline | اولا تعستعمل ال

b = {1, 2, 3}
c = {"one", "two", "Three"}
d = {"Uno", "dos", "tres"}

print(b | c | d) # {'two', 1, 2, 3, 'Three', 'Uno', 'tres', 'dos', 'one'}
print(b.union(c, d)) # {1, 2, 3, 'dos', 'Uno', 'Three', 'tres', 'one', 'two'}



# --------------------------------------
# add(value) => only one argument

e = {1, 2, 3, 4}
e.add(5)
e.add(6)
print(e) # {1, 2, 3, 4, 5, 6}




# --------------------------------------
# copy()

f = {"a", "b", "c"}
g = f.copy()

print(g) # {'a', 'b', 'c'}




# --------------------------------------
# remove(element) & discard(element)

# set بجوجهم كيديرو نفس الخدمة وهي انهم كيمسحو عنصر من ال

# error كيرجع ليك set الا عطيتي ليه قيمة مكيناش فال remove غار ال
# الا ملقاش كيدوزها و مكيرجع والو discard اما ال

h = {1, 2, 3, 4, 5, 6}

h.remove(4)
# h.remove(8) # KeyError: 8
h.discard(6)
h.discard(10)
print(h) # {1, 2, 3, 5}




# --------------------------------------
# pop() 

# element وهي انها كتمسح وكترجع ليك list هنا كدير نفس الخدمة ديال pop() ال

# index بحال argument ولكن الاختلاف لي كاين فهادي وهي انها مكتقبلش
# و فاش كترجعو ليك كتمسحو set من ال random value حيت هي كترجع ليك


i = {True, "A", "B", 1, 2}

random = i.pop()

print(random, i) # B {True, 2, 'A'}




# --------------------------------------
# update(iterable)

# union كدير نفس الخدمة ديال

# اخرين sets كتقبل منك فقط union الاختلاف لي كاين وهي ان ال
# strings lists tuples sets بحال iterable كتقبل منك اي update اما ال

j = {1, 2, 3, 4}
k = {1, "A", "B", 2}
j.update(k)
j.update(["Html", "Css", "JS"])
j.update(("ReactJS", "AngularJS", "VueJS"))
j.update("Obito")

print(j) 
# {'Html', 1, 2, 3, 4, 'ReactJS', 't', 'o', 'AngularJS', 'i', 'B', 'VueJS', 'JS', 'A', 'O', 'Css', 'b'}
# --------------------------------------
