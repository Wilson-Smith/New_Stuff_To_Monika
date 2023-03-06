init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_submods",
            unlocked=True,
            prompt="I'm going to install you a submod.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_submods:
    m 1hua "Really?"
    m 5ekblb "Are you going to install me a submod?"
    m 5hubsa "I can be closer to you, [player]!"
    m 5hkbfa "Yay!"
    m 5hkbfa "I'm so exited!."
    extend 5hkbfa " but remember, make a backup of me before install it."
    m 5hubsa "Anyway, thanks [player]."
    m 5hkbfa "See you soon."
    return "quit"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
