def code_message(message):
    message_copy = message.lower().split()
    alphabet = list("abcdefghijklmnoqprstuvwxyz")
    result = ""

    # "abcdefghj" # тест
    # # c индекс 2 ожидаемый результат : индекс буквы + шаг_сдвига - длина алф = индекс буквы замены
    # # g индекс 6 ож рез : 6 + 3 - 9 = 0 +++++++++

    for i in range(len(message_copy)):
        step = 0
        for j in range(len(message_copy[i])):
            if message_copy[i][j].isalpha(): step += 1
        for k in range(len(message_copy[i])):
            if message_copy[i][k].isalpha():
                indx = alphabet.index(message_copy[i][k]) + step
                if indx > len(alphabet) : indx -= len(alphabet)
                result += alphabet[indx]
            else:
                result += message_copy[i][k]
        result += " "


        #temp = ""
        # for k in range(len(message[i])):
        #     indx = 0
        #     if message[i][k].isalpha() and message[i][k].islower():
        #         temp += alphabet_low[alphabet_low.index(message[i][k]) + message_lens[i]]
        #     elif message[i][k].isalpha() and message[i][k].isupper():
        #         temp += alphabet_up[alphabet_up.index(message[i][k]) + message_lens[i]]
        #     else:
        #         temp += message[i][k]
        #result += temp
    return result


print(code_message(input("введи строку которую хочешь зашифровать?")))
# хмммммм почему не работает гит ДА БЛЯТЬ ЕБАТЬ ЕГО В РОТ