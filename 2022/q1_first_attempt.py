strings, vowels, answer_strings = ["fksahnlgueyilfhnalfkjnhdssaokjfhndsfiwaourhnfdjgbalfkjshedfnsf", "mkjmnacioudhrieeqwthyiugueresjfgwatfhwghfnhgnffn", "elruoqywicwnjksakvfbsgyohuehnghiefhggadfgsfsfs"], ['a', 'e', 'i', 'o', 'u'], []
for string in strings:
    i, temp_list = 0, []
    while i < len(string):
        if(string[i] in vowels):
            temp_list.append(string[i+1])
            i+=2
        else: i+=1
    answer_strings.append(temp_list)
print(answer_strings)

#This doesn't fit with how it worked, this is just the very first thing we did. I would recommend to try something similar to refamliarize yourself with python and their question styles