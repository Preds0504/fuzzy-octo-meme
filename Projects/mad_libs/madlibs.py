# way to concatenate a strong "print(f"subscribe to {youtuber"}"
#GOAL: to create a madlib game with random mad libs each time.  With 3 different madlibs.
# THe number before the underscore refers to which order in the mad lib it exists in
# The number past the underscore refers to the madlib it belongs to
import random

total = [1,2,3]
play = random.randint(1, 3)
if play == 1 and 1 in total:
    adj1_1 = input("Adjective: ")
    verb1_1 = input("Verb: ")
    verb2_1 = input("Verb: ")
    famous_person_1 = input("Famous Person: ")
    madlib_1 = f"Computer programming is so {adj1_1}! It makes me so excited all the time because \
    I love to {verb1_1}.  Stay hydrated and {verb2_1} Like you are {famous_person_1}!"
    total = [2,3]
    print(madlib_1)
elif play == 2 and 2 in total:
    adj1_2 = input("Adjective: ")
    verb1_2 = input("Verb: ")
    verb2_2 = input("Verb: ")
    verb3_2 = input("Verb: ")
    noun1_1 = input("Noun: ")
    famous_event1_2 = input("Famous Event: ")
    madlib_2 = f"You couldn't {verb1_2}?  You know the {famous_event1_2} doesn't start till {noun1_1}.  Anyway are you gonna {verb2_2} or {verb3_2}? \
    Hopefully this {adj1_2} person moves over to let us in."
    total = [1,3]
    print(madlib_2)
elif play == 3 and 3 in total:
    noun1_3 = input("Noun: ")
    verb1_3 = input("Verb: ")
    noun2_3 = input("Noun: ")
    noun3_3 = input("Noun: ")
    verb2_3 = input("Verb: ")
    verb3_3 = input("Verb: ")
    madlib_3 = f"Once the {noun1_3} had {verb1_3}.  We had to remove its {noun2_3} from the {noun3_3}.  He said to our surprise {verb2_3} \
        Your transgression will not be {verb3_3}."
    total = [2,3]
    print(madlib_3)


