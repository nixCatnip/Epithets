define fuy = Character("Fuyuhiko")
define har = Character("Haruki")
define rei = Character("Rei")
define him = Character("Hime")
define yoi = Character("Yoikishi")
define tfuy = Character("Fuyuhiko", color="#1d8f5f")
define thar = Character("Haruki", color="#1d8f5f")
define trei = Character("Rei", color="#1d8f5f")
define thim = Character("Hime", color="#1d8f5f")
define tyoi = Character("Yoikishi", color="#1d8f5f")
define nar = Character("")
transform left:
    xalign 0.25
    yalign 1.0
transform right:
    xalign 0.75
    yalign 1.0
transform farleft:
    xalign 0.05
    yalign 1.0
transform farright:
    xalign 0.95
    yalign 1.0
transform center:
    xalign 0.5
    yalign 1.0
transform truecenter:
    xalign 0.5
    yalign 0.5
#Spacer

#Basic introduction into the gist of the story
label start:
    play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0
    nar "Ah, San Francisco, the salty air of the sea mixed with the salty attitudes of young adults experiencing true independence for the first time in their lives."
    nar "Five of these young adults attend the local university, hailing from across the sea, here to expand their minds and hearts."
    nar "Ah, here comes one now. Arriving home after a long day of less than enjoyable work. perhaps the saltiest of them all, Fuyuhiko Shiro."
    scene apartment night
    show fuyu really
    with Dissolve(.5)
    fuy "I can't believe that woman!"
    fuy "She always thinks she knows what's best for me. She's not my fucking mom!"
    nar "He stomps across his small apartment and flips open a laptop, furiously scrolling through social media."
    nar "perhaps we should have him recall a few of his companions to take his mind off of things."
    nar "Noncanonically, of course."
    jump recallMenu
#Spacer

#Recall menu, featuring the descriptions of the other Epithets
label recallMenu:
    menu:
        "Haruki Supai":
            show fuyu what
            fuy "Haruki? He's a Computer Science Major. I've known him for the longest. He's been a chaotic bastard since the day we met."
            show fuyu really
            fuy "He's arrogant, somewhat violent, and worse of all, flirty. Guy's gay and he owns it, maybe a bit too much."
            fuy "Sometimes it feels like everything he says is specifically meant to make me uncomfortable, or annoyed."
            jump recallMenu
        "Yoikishi Konpeki":
            show fuyu neut
            fuy "A History Major. He's obsessed with both the Code of Chivalry and the Bushido Code, especially famous upholders of each."
            fuy "Not to mention he's super immature. Lately, he's taken to naming us after seasons."
            fuy "He's also very protective of his sister, Hime. It's hard to imagine him without her, and it's clear he has a great love for her."
            jump recallMenu
        "Himiko Konpeki":
            show fuyu neut
            fuy "Right, Himiko. She goes by Hime, and she's the only one of us that doesn't attend college."
            fuy "She works as a Graffiti Artist and Cashier and hates that part-time job as much as I."
            show fuyu smile
            fuy "She's even told me that she started tagging the area around her workplace."
            show fuyu neut
            fuy "Her nickname comes from a childhood love of princesses, and it stuck. Thanks to her brother, that is."
            jump recallMenu
        "Rei Amanshi":
            show fuyu neut
            fuy "A Theology Major. He practices some weird niche religon, one that his family holds a lot of power in."
            show fuyu down
            fuy "Sometimes, I pity him in a weird way. We were both put in such a bad situation by our parents."
            fuy "But Rei doesn't seem to notice that the pressure on him is unhealthy and barely listens to me when I talk to him about it."
            fuy "Worse yet, he was one of the people to see me at my worst earlier today."
            jump recallMenu
        "Move Foward":
            jump textMessage
#Spacer

#Text Message time
label textMessage:
    show fuyu neut
    nar "As the boy finishes his recollection, his phone begins to buzz. When he picks it up, a message from someone appears on the screen."
    nar "A message from..."
    menu:
        "Haruki":
            jump HarukiMessage
        "Yoikishi":
            jump YoikishiMessage
        "Hime":
            jump HimeMessage
        "Rei":
            jump ReiMessage
        "Work":
            jump WorkMessage
    return
#Spacer

label HarukiMessage:
    nar "...Haruki."
    $ chat = 1
    show fuyu really at farleft
    with moveinright
    show haruki smug at farright
    with Dissolve(0.5)
    thar "Heya there, Fuyu. Are you up to anything? I'd love to swing by and snatch you up~."
    tfuy "Not now Haruki, gods, especially not right now."
    show haruki frown
    thar "What do you mean?"
    thar "Are you alright, Fuyu?"
    $ renpy.pause(2.5)
    thar "Fuyu?"
    tfuy "Stop calling me that."
    thar "What?"
    stop music fadeout 1.0
    $ renpy.pause(2.0)
    thar "What do you mean, Fuyu?"
    show fuyu snap
    tfuy "MY NAME IS FUYUHIKO."
    show fuyu really
    tfuy "It's not \"Fuyu\"."
    tfuy "It's not \"sweetheart\" or \"doll\"."
    tfuy "It's Fuyuhiko."
    $ renpy.pause(2.0)
    thar "Fuyu..."
    tfuy "I'm done talking with you."
    play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0
    nar "The boy powers off his phone. If Haruki continued messaging him, he wouldn't recieve it."
    show fuyu down at center
    with moveinleft
    hide haruki frown
    with Dissolve(0.5)
    nar "Exhausted, the boy crawls into bed, and begins to fall into unconsciousness. The events of the day racing through his head and dreams."
    scene black
    with Dissolve(0.5)
    jump Day2
#Spacer

label YoikishiMessage:
    nar "...Yoikishi."
    $ chat = 2
    show fuyu neut at farleft
    with moveinright
    show yoikishi excited at farright
    with Dissolve(0.5)
    tyoi "winter! you HAVE to see this!"
    show yoikishi err
    tyoi "oh right"
    tfuy "It's fine, Yoikishi."
    tyoi "if its fine then why are you calling me that! >:("
    tfuy "Okay then,"
    show fuyu smile
    tfuy "Fall."
    show fuyu neut
    show yoikishi hap
    tyoi "there you go!"
    show yoikishi excited
    tyoi "oh right! i had a video to show you, you'll love it!"
    scene black
    with Dissolve(0.5)
    nar "The boys continued chatting about nothing of importance. It was a nice distraction for Fuyuhiko, one he really needed."
    jump Day2
#Spacer

label HimeMessage:
    nar "...Hime."
    $ chat = 3
    show fuyu neut at farleft
    with moveinright
    show hime yo at farright
    with Dissolve(0.5)
    thim "You are going to love what I just did."
    nar "Hime sends a image of her tagging her store along with a transcription."
    show fuyu smile
    tfuy "Amazing."
    thim "I know right!?"
    show hime cool
    thim "I've been waiting to do this for so long."
    tfuy "What broke the camel's back?"
    $ renpy.pause(2.0)
    show hime uncomfy
    thim "My asshat of a manager threatened my job because I refused to go out with him."
    show fuyu down
    tfuy "Oh."
    thim "Yeah."
    $ renpy.pause(3.0)
    tfuy "I tried to get out of my \"Accessibility Benefits\" again today."
    show hime cool
    thim "And how'd that go?"
    tfuy "Not great."
    thim "Our bosses suck, huh?"
    show fuyu neut
    tfuy "Yup"
    thim "I'll see you tomorrow, Fuyuhiko."
    hide hime cool
    with Dissolve(0.5)
    tfuy "You too, Hime."
    show fuyu down at center
    with moveinleft
    fuy "I really need to work on my people skills."
    scene black
    with Dissolve(0.5)
    jump Day2
#Spacer

label ReiMessage:
    nar "...Rei."
    $ chat = 4
    show fuyu down at farleft
    with moveinright
    show rei cautious at farright
    with Dissolve(0.5)
    trei "Shiro, are you there?"
    $ renpy.pause(3.0)
    trei "Shiro, please."
    $ renpy.pause(1.0)
    trei "Shiro."
    tfuy "What do you want, Rei?"
    trei "I just wanted to make sure you were okay."
    tfuy "I'm fine. Leave me alone."
    trei "Are you sure, Shiro?"
    tfuy "Don't make me block you, Rei."
    $ renpy.pause(1.0)
    nar "Fuyu sits for a few moments, waiting for a text that will never come."
    scene black
    with Dissolve(0.5)
    nar "Instead, he simply powers off his phone and heads to bed, trying to forget the events of the day."
    jump Day2
#Spacer

label WorkMessage:
    nar "...Her."
    $ chat = 5
    hide fuyu neut
    show the email at truecenter
    with Dissolve(0.5)
    nar "It was her."
    show fuyu snap
    hide the email
    fuy "That fucking bitch."
    fuy "She just aired our private conversation to the whole cafe!"
    fuy "It's bad enough putting up with her shit when it was just us."
    fuy "I bet she thinks she's doing what's best for me."
    fuy "I'M NOT A FUCKING KID ANYMORE DAD!"
    $ renpy.pause(2.0)
    show fuyu what
    fuy "I-"
    $ renpy.pause(2.0)
    show fuyu down
    fuy "I need some sleep."
    scene black
    with Dissolve(0.5)
    jump Day2
#Spacer

label Day2:
    nar "End of Day 1."
    nar "Start of Day 2."
    scene apartment day
    with Dissolve(0.5)
    nar "The next day passed mostly uneventfully"
    scene hallway day
    with Dissolve(0.5)
    nar "The same classes in the same order and the same motions."
    scene classroom evening
    with Dissolve(0.5)
    nar "That was until after school."
    show hime cool at farleft
    show yoikishi hap at left
    show rei distracted at right
    #checks if Haruki was texted last night
    if chat = 1:
        show haruki frown at farright
    else:
        show haruki smug at farright
    with Dissolve(0.5)
    nar "Club time, that is."
