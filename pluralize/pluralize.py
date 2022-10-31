def pluralize(stuff: list) -> list:
    tmp = {}
    for i in stuff:
        if tmp.get(i) is None:
            tmp[i] = 1
            continue
        tmp[i] += 1
    output_list = []
    for key, value in tmp.items():
        output_list.append(key) if value == 1 else output_list.append(f"{key}s")

    return output_list


print(pluralize(["cow", "chair", "chair", "horse", "cow", "door", "cow"]))
