bullet = [f"<li>{i}</li>" for i in input("BULLET POINTS: ").split(", ")]
number = [f"<li>{i}</li>" for i in input("NUMBER LIST: ").split(", ")]


def tag(name: str, items: list[str]):
    nt = "\n\t"
    return f"<{name}>\n\t{nt.join(items)}\n</{name}>"


with open("output.html", "w") as f:
    f.write(tag("ul", bullet))
    f.write("\n" * 3)
    f.write(tag("ol", number))
