init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_we_going_to_church",
            unlocked=True,
            prompt="We're going at the church",
            pool=True
        ),
        code="BYE"
    )

label bye_we_going_to_church:
    m 1eub "Oh, okay!"
    jump bye_going_somewhere_post_aff_check

label bye_going_somewhere_post_aff_check:
    # il file creato proviene da mas_dockstat_iostart, quindi è questo il generativo di Moni
    jump mas_dockstat_iostart
