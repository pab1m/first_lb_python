import re


def check(check_text):
    pattern = re.compile('^[а-яїєґі\s.,!?-]+$')
    return bool(pattern.match(check_text.lower()))


text_1 = input("Введіть текст: ")

if check(text_1):
    print("Рядок є україномовним")

    text_2 = input("Введіть текст 2: ")

    if len(text_1) > len(text_2):
        print(f"Рядок 1 більший за рядок 2 на '{len(text_1)-len(text_2)}'")

    elif len(text_2) > len(text_1):
        print(f"Рядок 2 більший за рядок 1 на '{len(text_2)-len(text_1)}'")

    else:
        print("Рядки є однаковими")