# ------------------------------------------
# --- pylint: For better Code ----
# ------------------------------------------
#
# syntax:
#
# pip install pylint
#
# pylint.exe currPyFilePath
# ------------------------------------------


def sayHi(name):
    print("hello ", name)


print(sayHi("moha"))


# // الفكرة ديالو انه كيقيم ليك الملف ديالك و كينبهك على بعض الممارسات لي خاص ديرهم باش تكون كاتب كود نقي


# currentPyFilePath:2:0: E0011: Unrecognized file option '----' (unrecognized-inline-option)
# currentPyFilePath:17:0: C0304: Final newline missing (missing-final-newline)     
# currentPyFilePath:1:0: C0114: Missing module docstring (missing-module-docstring)
# currentPyFilePath:1:0: C0103: Module name "04 - pylint for better code" doesn't conform to snake_case naming style (invalid-name)
# currentPyFilePath:13:0: C0116: Missing function or method docstring (missing-function-docstring)
# currentPyFilePath:13:0: C0103: Function name "sayHi" doesn't conform to snake_case naming style (invalid-name)
# ------------------------------------------------------------------
# Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)