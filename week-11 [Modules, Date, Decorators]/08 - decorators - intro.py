# --------------------------------------------
# ---- Generators - Intro ----
# --------------------------------------------
# 
# --------------------------------------------

# meta programming كيتسما ايضا decorator ال

# ديالك function بحال الا قلتي شغل تزيين على ال decoration ال


# و كيرجعا functionality و كيضيف عليها بعض ال arg ديالك ك function كياخذ ال decorator ال
# ديالك باش يحسن من السلوك ديالها function لل wrap يعني كيدير
# higher order function و كيتعتابر




# متبوعة بسمية ديالو @ ديالك كدير قبل من التعريف ديالها بسطر علامة function على ال decorator باش طبق ال
# كما كتشوف لتحت

def myDecorator(func): # Decorator
    def nestedFunction(): # any name just for decoration
        print("SomeThings After") # message from decorator
        func() # execute function
        print("SomeThings Before") # message from decorator
    return nestedFunction # return all data

@myDecorator
def myFunctionToSayHi():
    print("Hello Folks!")


myFunctionToSayHi()
# SomeThings After
# Hello Folks!     
# SomeThings Before



# decoration كيطبق عليها ال @decoratorName لي كدير قبل منها function مما يعني ان ال
# اما لي مكديروش فيها كتكون عادية