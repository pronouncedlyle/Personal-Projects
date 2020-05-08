print()
print("Army Meeting Simulator 2019")
print()
print()
char_name=str(input("What is your last name?:"))
print()
char_rank=str(input ("What rank are you?:"))
print()
char_name=char_rank + " " + char_name
while True:
    level_f = int(input(
        "On a scale of 1 to 10 how excited are you about being in the Army right now? (10 being a bright-eyed, bushy-tailed 2LT, 1 being a SPC with 5 years TIS facing imminent chapter):"))
    if 1<=level_f<=10:
        break
    else:
        print("Try again dummy:")
        print()
print()
print("You," + char_name + ", find yourself sitting in a meeting surrounded by people with whom you do not normally work.")
print("Your thoughts begin to wander when suddenly you are pulled abruptly into reality.")
print("\"" + char_name + ", what do you think we should do about the upcoming ball?\". All eyes turn to you.")
print()
if 8 <= level_f <= 10:
    print("You firmly plant your hands flat on the table, look the man straight in the eye and reply, ")
    print("\"Sir, this is the most important event of the year, we cannot disappoint the brigade commander\"")
    print("The officers in the room nod their heads approvingly, and you see one of the FRG leaders tear up. The Kool-Aid never tasted so good")

if 4 <= level_f <= 7:
    print("You look up, caught slightly off-guard and say, ")
    print("\"Uh, sounds good to me sir, whatever you need.\"")
    print("That was a close one.")
if 1 <= level_f <= 3:
    print("You look up from your phone and think to yourself that you probably shouldn't say anything, but what the heck: ")
    print("\"Sir, I'm really not sure why we are wasting money, time, and man hours planning asinine details of what is essentially a work party.")
    print("This reminds me of the party planning committee from The Office, not an Infantry Brigade Combat Team of the United States Army, is this really the best use of our time?\"")
    print("The room falls quiet. You done messed up A-Aron.")
