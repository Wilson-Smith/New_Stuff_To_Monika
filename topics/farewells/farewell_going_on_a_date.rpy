init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_going_on_a_date",
            unlocked=True,
            prompt="We're going on a date.",
            pool=True
        ),
        code="BYE"
    )

label bye_going_on_a_date:
    m 1hub "Oh, okay!"
    m 3tub "Taking me somewhere special today, isn't it?"
    m 1hua "Yay!"
    jump bye_going_somewhere_post_aff_check

label bye_going_somewhere_post_aff_check:

    jump mas_dockstat_iostart
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
