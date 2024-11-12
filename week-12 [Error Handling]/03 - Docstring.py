# -----------------------------------------------------------
# ---- Doc string & commenting vs documentings ----
# -----------------------------------------------------------
# 
# Documentation string for Class, Module, or Function
# Can be accessed from help(funcName) or .__doc__
# Made for understanding the functionality of the complex code
# -----------------------------------------------------------

# // commenting دبا فاش كنستعملو الشباك بحال التعليقات الفوق هدا كيتسما

# // معقدين فالخدمة ديالهم module اولا class اولا function هي الوصف لي كتشرح فيه شي documenting اما ال


def sayHi(name):
    '''
    This is Function to say hello to a person name
    params:
        name => str
    output:
        just printing in the console
    '''
    print("Hello sir ", name)


# __doc__ attr اولا help func عن طريق يما documentation تقد توصل لل

help(sayHi)
print(sayHi.__doc__)

# This is Function to say hello to a person name
# params:
#     name => str
# output:
#     just printing in the console
