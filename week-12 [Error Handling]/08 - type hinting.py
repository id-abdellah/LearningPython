# ----------------------------------------------
# --- Type Hinting ---
# ----------------------------------------------
#
# ----------------------------------------------


# // typeScript فال types annotations كتعقل على ال
# // python فال types hinting وراه بحالها بحال ال

# // يعني تلميح لنوع المتغير hint كيخدمو فقط ك type hinting ال python ولكن هنا فال
# // error ف سواء درتيه اولا لا مغيطرا والو ومغيطلع لك تا


age: int = 20
fullName: str = "Mohamed ID-ABDELLAH"
isHired: bool = False

def sayHello(name: str, age: int, isHired: bool) -> str :
    return f"hello {name} your age is {age} and u are {"hired" if isHired else "Not hired"}"

skills: list[str] = ["html", "css", "js"]

pTails: dict[str, float] = {"a": 1.80, "b": 1.20}

tp: tuple[str, int] = ("student 1", 80)