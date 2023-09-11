import re


def check_uk_text(check_text):
    pattern = re.compile('^[а-яїєґі\s.,!?-]+$')
    return bool(pattern.match(check_text.lower()))


def check_diff(txt_1):
    text_2 = input("Введіть текст 2: ")
    if check_uk_text(text_2):
        if len(txt_1) > len(text_2):
            return print(f"Рядок 1 більший за рядок 2 на '{len(txt_1)-len(text_2)}'")
        elif len(text_2) > len(txt_1):
            return print(f"Рядок 2 більший за рядок 1 на '{len(text_2)-len(txt_1)}'")
        else:
            return print("Рядки є однаковими")
    else:
        return print("Рядок не є україномовним")


text_1 = input("Введіть текст: ")
if check_uk_text(text_1):
    print("Рядок є україномовним")
    check_diff(text_1)
else:
    print("Рядок не є україномовним")