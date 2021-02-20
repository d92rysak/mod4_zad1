def palindrom(word):
    """
    Funkcja przyjmuje za argument słowo czyli string i sprawdza, czy jest ono palindromem. 
    Sprawdzenie czy string jest palindromem odbywa się na zasadzie porównania kolejno 
    pierwszej i ostatniej litery w słowie, drgiej i przedostatniej itd. Jeśli litery 
    w którejkolwiek parze są różne, funkcja zwraca bool False. Jeśli funkcja przejdzie przez całe słowo,
    to zanaczy, że słowo jest palindromem i funkcja zwraca bool True.
    """
    word_lenght=len(word)
    half_word_lenght=int(word_lenght/2)
    for i in range (half_word_lenght):
        print(i)
        a=word_lenght-i-1
        print(word[i])
        print(word[a])
        if word[i]!=word[a]:
            return(False)
        else:
            continue
    return(True)


print(bool(palindrom("kajek")))