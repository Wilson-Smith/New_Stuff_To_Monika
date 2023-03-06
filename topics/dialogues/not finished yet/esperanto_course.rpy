
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="esperanto_0",category=['esperanto'],prompt="Saluton [player]",pool=True,unlocked=True,random=True))
init offset = 5
label esperanto_0:
    m 2etc "Saluton [player], Kiel vi fartas? Mi estas tre bone"
$ _history_list.pop()
menu:
    "*Huh?*":
        m 2tfa "Saluton [player], Kiel vi fartas?"
$ _history_list.pop()
menu:
    "*What?*":
        m 2tfd "[player]! Kiel vi fartas?"
$ _history_list.pop()
menu:
    "I don't understand.":
        m 2dka "It's Esperanto, [player]! "
        m 2tta "I told you I was learning that."
$ _history_list.pop()
menu:
    "Oh, I see.":
        m 2ekbla "[player]..."
$ _history_list.pop()
menu:
    "Yeah?":
        m 2eta "Do you want to learn esperanto with me?"
$ _history_list.pop()
menu:
    "Yes.":
        m 2ekbsa "Oh{w=0.6} [player]! I'm so glad to hear that."
        m 1tsbfb "Let's learn it togheter, darling~"


init python:
    addEvent(Event(persistent.event_database,eventlabel="esperanto_1",category=['esperanto', 'languages'],prompt="Esperanto 1",pool=True,unlocked=True,random=True))
label esperanto_1:
    m 2etc "Hello [player], this is the first Esperanto lesson. {w=0.6} I'm going to teach you how to say greet someone in Esperanto."
    m 2etc "First, I'm going to teach you how to say hello."
    m 2etc "In Esperanto, you say 'Saluton' to someone to say hello. It's very simple."
    m 2etc "Ok, now let's say 'Thanks' in Esperanto."
    m 2etc "In Esperanto, you say 'Dankon' to someone to say thanks."
    m 2etc "Ok, now let's say 'Goodbye' in Esperanto."
    m 2etc "In Esperanto, you say 'Adiaŭ' to someone to say goodbye."
    m 2etc "Ok, now let's say 'How are you' in Esperanto."
    m 2etc "In Esperanto, you say 'Kiel vi faras?' to someone to say how are you."
    m 2etc "Ok, now let's do a test."
    m 2etc "'Saluton' is 'Hello' in Esperanto?"

$ _history_list.pop()
menu:
    "Yes.":
        m 2ekbsa "Good job, [player]! You're doing great!"
        m 2ekbsa "Now, let's go to the next question."
        m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
    "No.":
        m 2ekbsa "Oh, that's not correct. Let's try again."
        m 2ekbsa "'Saluton' is 'Hello' in Esperanto?"
        $ _history_list.pop()
        menu:
            "Yes.":
                m 2ekbsa "Good job, [player]! You're get it right!"
                m 2ekbsa "Now, let's go to the next question."
                m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
            "No.":
                m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                m 2ekbsa "'Saluton' is 'Hello' in Esperanto?"
                $ _history_list.pop()
                menu:
                    "Yes.":
                        m 2ekbsa "Good job, [player]! You're get it right!"
                        m 2ekbsa "Now, let's go to the next question."
                        m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
                    "No.":
                        m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                        m 2ekbsa "'Saluton' is 'Hello' in Esperanto?"
                        $ _history_list.pop()
                        menu:
                            "Yes.":
                                m 2ekbsa "Good job, [player]! You're get it!"
                                m 2ekbsa "Now, let's go to the next question."
                                m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
                            "No.":
                                m 2ekbsa "Com'on [player], you are better than that do! Concentrate and relax."
                                m 2ekbsa "'Saluton' is 'Hello' in Esperanto?"
                                $ _history_list.pop()
                                menu:
                                    "Yes.":
                                        m 2ekbsa "Good job, [player]! You're get it right!"
                                        m 2ekbsa "Now, let's go to the next question."
                                        m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
                                    "No.":
                                        m 2ekbsa "[player], you can do it! I know you can get it right this time."
                                        m 2ekbsa "'Saluton' is 'Hello' in Esperanto?"
                                        $ _history_list.pop()
                                        menu:
                                            "Yes.":
                                                m 2ekbsa "Good job, [player]! You're get it right!"
                                                m 2ekbsa "Now, let's go to the next question."
                                                m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
                                            "No.":
                                                m 2ekbsa "[player], 'Saluton' is 'Hello' in Esperanto"
                                                m 2ekbsa "Anyway, let's go thru."
                                                m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"

$ _history_list.pop()
menu:
    "Yes.":
        m 2ekbsa "Good job, [player]! You're doing great!"
        m 2ekbsa "Now, let's go to the next question."
        m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
    "No.":
        m 2ekbsa "Oh, that's not correct. Let's try again."
        m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
        $ _history_list.pop()
        menu:
            "Yes.":
                m 2ekbsa "Good job, [player]! You're get it right!"
                m 2ekbsa "Now, let's go to the next question."
                m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
            "No.":
                m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
                $ _history_list.pop()
                menu:
                    "Yes.":
                        m 2ekbsa "Good job, [player]! You're get it right!"
                        m 2ekbsa "Now, let's go to the next question."
                        m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
                    "No.":
                        m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                        m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
                        $ _history_list.pop()
                        menu:
                            "Yes.":
                                m 2ekbsa "Good job, [player]! You're get it!"
                                m 2ekbsa "Now, let's go to the next question."
                                m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
                            "No.":
                                m 2ekbsa "Com'on [player], you are better than that do! Concentrate and relax."
                                m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
                                $ _history_list.pop()
                                menu:
                                    "Yes.":
                                        m 2ekbsa "Good job, [player]! You're get it right!"
                                        m 2ekbsa "Now, let's go to the next question."
                                        m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
                                    "No.":
                                        m 2ekbsa "[player], you can do it! I know you can get it right this time."
                                        m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
                                        $ _history_list.pop()
                                        menu:
                                            "Yes.":
                                                m 2ekbsa "Good job, [player]! You're get it right!"
                                                m 2ekbsa "Now, let's go to the next question."
                                                m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
                                            "No.":
                                                m 2ekbsa "[player], 'Thanks' is 'Dankon' in Esperanto"
                                                m 2ekbsa "Anyway, let's go thru."
                                                m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"

$ _history_list.pop()
menu:
    "Yes.":
        m 2ekbsa "Good job, [player]! You're doing great!"
        m 2ekbsa "Now, let's go to the next question."
        m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
    "No.":
        m 2ekbsa "Oh, that's not correct. Let's try again."
        m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
        $ _history_list.pop()
        menu:
            "Yes.":
                m 2ekbsa "Good job, [player]! You're get it right!"
                m 2ekbsa "Now, let's go to the next question."
                m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
            "No.":
                m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
                $ _history_list.pop()
                menu:
                    "Yes.":
                        m 2ekbsa "Good job, [player]! You're get it right!"
                        m 2ekbsa "Now, let's go to the next question."
                        m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
                    "No.":
                        m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                        m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
                        $ _history_list.pop()
                        menu:
                            "Yes.":
                                m 2ekbsa "Good job, [player]! You're get it!"
                                m 2ekbsa "Now, let's go to the next question."
                                m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
                            "No.":
                                m 2ekbsa "Com'on [player], you are better than that do! Concentrate and relax."
                                m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
                                $ _history_list.pop()
                                menu:
                                    "Yes.":
                                        m 2ekbsa "Good job, [player]! You're get it right!"
                                        m 2ekbsa "Now, let's go to the next question."
                                        m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
                                    "No.":
                                        m 2ekbsa "[player], you can do it! I know you can get it right this time."
                                        m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
                                        $ _history_list.pop()
                                        menu:
                                            "Yes.":
                                                m 2ekbsa "Good job, [player]! You're get it right!"
                                                m 2ekbsa "Now, let's go to the next question."
                                                m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"
                                            "No.":
                                                m 2ekbsa "[player], 'Adiaŭ' is 'Goodbye' in Esperanto"
                                                m 2ekbsa "Anyway, let's go thru."
                                                m 2ekbsa "Is 'Dankon' 'Thanks' in Esperanto?"

$ _history_list.pop()
menu:
    "Yes.":
        m 2ekbsa "Good job, [player]! You're doing great!"
        m 2ekbsa "Now, let's do more difficult stuff."
        m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
    "No.":
        m 2ekbsa "Oh, that's not correct. Let's try again."
        m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
        $ _history_list.pop()
        menu:
            "Yes.":
                m 2ekbsa "Good job, [player]! You're get it right!"
                m 2ekbsa "Now, let's do more difficult stuff."
                m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
            "No.":
                m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
                $ _history_list.pop()
                menu:
                    "Yes.":
                        m 2ekbsa "Good job, [player]! You're get it right!"
                        m 2ekbsa "Now, let's do more difficult stuff."
                        m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
                    "No.":
                        m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                        m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
                        $ _history_list.pop()
                        menu:
                            "Yes.":
                                m 2ekbsa "Good job, [player]! You're get it!"
                                m 2ekbsa "Now, let's do more difficult stuff."
                                m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
                            "No.":
                                m 2ekbsa "Com'on [player], you are better than that do! Concentrate and relax."
                                m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
                                $ _history_list.pop()
                                menu:
                                    "Yes.":
                                        m 2ekbsa "Good job, [player]! You're get it right!"
                                        m 2ekbsa "Now, let's do more difficult stuff."
                                        m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
                                    "No.":
                                        m 2ekbsa "[player], you can do it! I know you can get it right this time."
                                        m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
                                        $ _history_list.pop()
                                        menu:
                                            "Yes.":
                                                m 2ekbsa "Good job, [player]! You're get it right!"
                                                m 2ekbsa "Now, let's do more difficult stuff."
                                                m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"
                                            "No.":
                                                m 2ekbsa "[player], 'Adiaŭ' is 'Goodbye' in Esperanto"
                                                m 2ekbsa "Anyway, let's go thru."
                                                m 2ekbsa "Is 'Kiel vi faras?' 'Hello' in Esperanto?"

$ _history_list.pop()
menu:
    "Yes.":
        m 2ekbsa "NO [player]! 'Kiel vi faras?' is NOT 'Hello' in Esperanto!"
        m 2ekbsa "In Esperanto, you say 'Kiel vi faras?' to someone to say 'how are you?'"
        m 2ekbsa "Also in Esperarnto you say 'Saluton' to someone to say 'Hello'."
        m 2ekbsa "Anyway, I'll leave some exercises for you to elaborate on."
        m 2ekbsa "They are in the 'Exercises' menu and they are labeled as 'Esperanto 1'."
        m 2ekbsa "Anyway, let's go to the next lesson."
    "No.":
        m 2ekbsa "Very good! [player]! 'Kiel vi faras?' is not 'Hello' in Esperanto!"
        m 2ekbsa "Anyway, I'll leave some exercises for you to elaborate on."
        m 2ekbsa "They are in the 'Exercises' menu and they are labeled as 'Esperanto 1'."
        m 2ekbsa "Anyway, let's go to the next lesson."
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
