"""
Opgave "spell_consonants":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Forandre koden i funktionen spell_consonants() sådan at den gør hvad der står i dens dokumentation.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


def spell_consonants(text, letter_limit):
    non_consonants = ["a", "e", "i", "o", "u", "y"]
    """
    Spells/prints the first letter_limit letters of text.
    Prints only consonants and spaces (a, e, i, o, u, y do not get printed). """
    non_consonants_string = ""
    for i, char in enumerate(text):
        if i == letter_limit:
            break
        if char not in non_consonants:
            non_consonants_string += char
    print(non_consonants_string)


spell_consonants("Hello world", 9)  # should print "Hll wr"
spell_consonants("I love Python", 10)  # should print "I lv Pt"
