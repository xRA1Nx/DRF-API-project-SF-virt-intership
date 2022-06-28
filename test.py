mystring = """ f ds fsd     fdfsf   
fdsfdsf
fddf"""

first = """
раз 
два
три
четыре
пять
"""


def change_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as output, open(path, "r+", encoding="utf-8") as input:
        line = 0
        while True:
            text = output.readline()
            line += 1
            if not text:
                break
            else:
                input.write(f"{line} {text}")


change_text("mytest.txt")
