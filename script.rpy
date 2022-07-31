# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define GGchar = Character("[GGname]")



# The game starts here.

label start:
python:
    GGname = renpy.input("What is your name?", length=32)
    GGname = GGname.strip()

    if not GGname:
         GGname = "Slim Shady"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

show eileen happy

    # These display lines of dialogue.

e "Look, if you had one shot or one opportunity"

e "To seize everything you ever wanted in one moment"
e "Would you capture it, or just let it slip? Yo"

    #make GG choose right lyrics to win

default NotLoser = False
menu:

    "It's \"Lose Yourself\"!":
        $ NotLoser = True
        jump .win

    "I have bad taste in music":
        jump .lose

label .win:

    GGchar "His palms are sweaty, knees weak, arms are heavy"
    GGchar "There's vomit on his sweater already, mom's spaghetti"
    GGchar "He's nervous, but on the surface he looks calm and ready"
    GGchar "To drop bombs, but he keeps on forgetting"
    e "What he wrote down, the whole crowd goes so loud"
    e "He opens his mouth, but the words won't come out"
    e "He's choking, how? Everybody's joking now"
    e "The clock's run out, time's up, over, blaow"
    GGchar "Snap back to reality, ope there goes gravity, ope"
    GGchar "There goes Rabbit, he choked, he's so mad but he won't"
    GGchar "Give up that easy, no, he won't have it, he knows"
    GGchar "His whole back's to these ropes, it don't matter, he's dope"
    e "He knows that but he's broke, he's so stagnant, he knows"
    e "When he goes back to this mobile home, that's when it's"
    e "Back to the lab again, yo, this old rhapsody"
    e "Better go capture this moment and hope it don't pass him, and"

    jump .marry

label .lose:
    GGchar "Sorry i don't know the lyrics"


    jump .death
if NotLoser:
    label .marry:

        "So, anyway, we married now."
        hide eileen

        "Good Ending"
else:
    label .death:
        e " *dies of cringe* "
        show eileen with fade
        "Bad Ending"






    # This ends the game.
return
