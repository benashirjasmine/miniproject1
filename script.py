
# coding=utf-8
import random
def story():
    #creating the template
    templates = { 1 : (
                       'it was about {number} {time} ago when I arrived at the hospital in a {transportation} The hospital is an {adjective} place, there are a lot of {adjective2}  {noun} here\n'
                       'there are nurses here who have {colour} {part_of_body}. If someone wants to come into my room I told them that they have to {verb} I’ve decorated my room with {number2} {noun2}\n'
                       'today I talked to a doctor and they were wearing a {noun3} on their {part_of_body_2} I heard that all doctors {verb} {noun4} every day for breakfast. \n'
                       'The most {adjective3} thing about being in the hospital is the {silly_word} {noun} ! '),
                  2 : (
                      'his weekend I am going camping with {proper_noun}. I packed my lantern, sleeping bag, and {noun}. I am so {adjective_feeling} to {verb} in a tent.\n'
                      'I am (adjective_feeling_2} we might see an {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}\n'
                      'I have heard that the {color} lake is great for {verb_end_in_ing}. Then we will {adverb} hike through the forest for {number} {time}.\n '
                      ' If I see a {color} {animal} while hiking, I am going to bring it home as a pet!At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!! '),
                  3 : (
                      '  Dear {proper_noun}, I am writing to you from a {adjective} castle in an enchanted forest I found myself here one day after going for a ride on a {color} {animal} in {place}.\n'
                      ' There are {adjective2} {plural} and {adjective3} {plural2} here! In the {room} there is a pool full of {noun}.\n'
                      ' I fall asleep each night on a {noun2} of {plural3} and dream of {adjective4} {plural4}.It feels as though I have lived here for {number} {time}\n'
                      'I hope one day you can visit, although the only way to get here now is {verb_end_in_ing} on a {adjective5} {noun5}!!')}
    #ask the user to choose template
    print ("choose the template " )
    template_choice = int(input("enter the template(1-3) : "))
    #ask the user for input
    number = int(input("enter the number   : "))
    number2 = int(input("enter the number : "))
    time = int(input("enter the time : "))
    transportation = input("enter the mode of transportation : ")
    colour = input("enter the colour : ")
    part_of_body = input("enter the part of the body : ")
    part_of_body_2 = input("enter the part of the body 2 : ")
    adjective = input ("enter the adjective")
    adjective2 = input("enter the adjective 2 : ")
    adjective3 = input("enter the adjective 3 : ")
    adjective4 = input("enter the adjective 4 : ")
    adjective5 = input("enter the adjective 5 : ")
    adjective_feeling = input("enter the adjective(feeling):  ")
    adjective_feeling_2 = input("enter the adjective (feeling-2) : ")
    noun = input("enter the noun : ")
    noun2 = input("enter the noun 2 : ")
    noun3 = input("enter the noun 3 : ")
    noun4 = input("enter the noun 4  : ")
    noun5 = input("enter the noun 5 : ")
    verb = input("enter the verb : ")
    verb2 = input("enter the verb 2 : ")
    verb_end_in_ing =input("enter the verb ending in ing : ")
    proper_noun = input("enter the proper noun(person name) : ")
    silly_word = input ("enter the silly word  : ")
    animal = input("enter the animal : ")
    adverb = input("enter the adverb ending ly : ")
    place = input("enter the place : ")
    room = input("enter the room in the house : ")
    plural = input("enter the magical creature (plural) : ")
    plural2 = input("enter the magical creature (plural ) : ")
    plural3 = input("enter the noun(plural-3) : ")
    plural4 = input("enter the noun(plural-4 )  : ")
    # generate story
    filled_template = templates.get(template_choice)
    generate_story = filled_template.format(number = number, time = time,transportation = transportation, colour = colour ,part_of_body = part_of_body, part_of_body_2 = part_of_body_2,adjective = adjective , adjective2 = adjective2, adjective3 =adjective3, adjective4 = adjective4 , adjective5 = adjective5 ,adjective_feeling = adjective_feeling ,adjective_feeling_2 = adjective_feeling_2 ,verb = verb ,verb2 = verb2 , verb_end_in_ing = verb_end_in_ing ,noun = noun , noun2 = noun2 , noun3 = noun3 ,noun4 = noun4 ,noun5 = noun5, proper_noun = proper_noun ,silly_word =silly_word ,animal = animal, adverb = adverb , place = place , room = room ,plural =plural ,plural2 = plural2 , plural3 = plural4)
    print(generate_story )


story()
