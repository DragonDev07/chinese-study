import random

characters = ["初", "单程", "往返", "航空", "查", "航班", "千", "直飞", "打折", "转机", "靠", "窗户", "走道", "份", "素餐", "旅馆", "租", "中国国际航空公司", "西北航空公司"]
pinyin = ["chu", "dan cheng", "wang fan", "hang kong", "cha", "hang ban", "qian", "zhi fei", "da zhe", "zhuan ji", "kao", "chuang hu", "zou dao", "fen", "su can", "lü guan", "zu", "zhong guo guo ji hang kong gong si", "xi bei hang kong gong si"]
english = ["beginning", "one-way trip", "make a round trip, go there and back", "aviation", "to check, to look into", "scheduled flight", "thousand", "fly directly", "to sell at a discount", "change planes", "to lean on, to lean against", "window", "aisle", "(measure word for meal orders, jobs)", "vegetarian meal", "hotel", "to rent", "air china", "northwest airlines"]
already_prompted = []

for i in range(len(characters)):
    randint = 0
    prompt = random.randint(1, 3)
    if prompt == 1:
        randint = random.randint(0, 18)
        while(randint in already_prompted):
            randint = random.randint(0, 18)
        already_prompted.append(randint)
        print(f"Prompt: {pinyin[randint]}")
    elif prompt == 2:
        randint = random.randint(0, 18)
        while(randint in already_prompted):
            randint = random.randint(0, 18)
        already_prompted.append(randint)
        print(f"Prompt: {english[randint]}")
    elif prompt == 3:
        randint = random.randint(0, 18)
        while(randint in already_prompted):
            randint = random.randint(0, 18)
        already_prompted.append(randint)
        print(f"Prompt: {characters[randint]}")
    
    show_ans = input("Enter 'y' to show answer: ")
    if show_ans == 'y':
        print("--Answer Below--")
        print(f"Character: {characters[randint]} \nPinyin: {pinyin[randint]} \nEnglish: {english[randint]}")
    print("--------------------------------------------------------------------------------------------------")
