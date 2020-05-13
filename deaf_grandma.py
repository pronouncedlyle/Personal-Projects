byeCount = 0
while byeCount < 2:
    answer1 = input("Say something to Grandma: ")
    if answer1 == (""):
        print("WHAT?!")
    elif any(c.islower() for c in answer1):
        print("SPEAK UP, KID!")
    elif answer1.isupper:
        if answer1 == "GOODBYE!":
            byeCount = byeCount + 1
            if byeCount == 1:
                print("LEAVING SO SOON?")
            if byeCount == 2:
                print("LATER, SKATER!")
        else:
            print("NO, NOT SINCE 1946!")

# If you don't input anything (just hit enter) she responds with WHAT?!
# If you ask a question with any lower-case letters, she responds with SPEAK UP, KID!
# If you talk to her in all upper-case letters, she responds with NO, NOT SINCE 1946!
# The first time you say GOODBYE! she says LEAVING SO SOON?
# The second time you say GOODBYE! she says LATER, SKATER! and the program exits.