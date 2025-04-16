def code_message(message):
    message_copy = message.split()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for i in range(len(message_copy)):
        step = 0
        for j in range(len(message_copy[i])):
            if message_copy[i][j].isalpha(): step += 1
        for k in range(len(message_copy[i])):
            if message_copy[i][k].isalpha():
                indx = alphabet.index(message_copy[i][k].lower()) + step
                if indx >= len(alphabet) : indx -= len(alphabet)
                if message_copy[i][k].isupper() : result += alphabet[indx].upper()
                else: result += alphabet[indx]
            else:
                result += message_copy[i][k]
        result += " "

    return result


print(code_message(input("введи строку которую хочешь зашифровать?\n")))
