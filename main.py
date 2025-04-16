def code_message(message):
    message_copy = message.lower().split()
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    result = ""

    for i in range(len(message_copy)):
        step = 0
        for j in range(len(message_copy[i])):
            if message_copy[i][j].isalpha(): step += 1
        for k in range(len(message_copy[i])):
            if message_copy[i][k].isalpha():
                indx = alphabet.index(message_copy[i][k]) + step
                if indx >= len(alphabet) : indx -= len(alphabet)
                result += alphabet[indx]
            else:
                result += message_copy[i][k]
        result += " "
    #message_copy = " ".join(message_copy)

    # for i in range((len(message_copy))):
    #     if message_copy[i].isalpha() and message_copy[i].isupper():
    #         result = result[:i] + message_copy[i].upper() + result[i+1:]

    return result


print(code_message(input("введи строку которую хочешь зашифровать?")))
# хмммммм почему не работает гит ДА БЛЯТЬ ЕБАТЬ ЕГО В РОТ