define fuy = Character("Fuyuhiko", color="#8ceffa")
define har = Character("Haruki", color="#fa8c8c")
define rei = Character("Rei", color="#93fa8c")
define him = Character("Hime", color="#faf48c")
define ryu = Character("Ryuji", color="#8c95fa")
define tfuy = Character("Fuyuhiko", color="#1d8f5f")
define thar = Character("Haruki", color="#1d8f5f")
define trei = Character("Rei", color="#1d8f5f")
define thim = Character("Hime", color="#1d8f5f")
define tryu = Character("Ryuji", color="#1d8f5f")
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

#Day 1
#Basic introduction into the gist of the story
label start:
    #Flag Defines
    $ HarukiChat = False
    $ RyujiChat = False
    $ HimeChat = False
    $ ReiChat = False
    $ WorkChat = False
    #Spacer
    play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0
    nar "Ah, San Francisco, the salty air of the sea mixed with the salty attitudes of young adults experiencing true independence for the first time in their lives."
    nar "Five of these young adults attend the local prestigious university, hailing from across the sea, here to expand their hearts and minds."
    nar "Ah, here comes one now, arriving home after a long day of work. Perhaps the saltiest of them all, Fuyuhiko Shiro."
    scene apartment night
    show fuyu really
    with Dissolve(0.5)
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
            with Dissolve(0.5)
            fuy "Haruki? He's a Computer Science major. I've known him for the longest. He's been a chaotic bastard since the day we met."
            show fuyu really
            with Dissolve(0.5)
            fuy "He's arrogant, somewhat violent, and worse of all, flirty. Guy's attractive and he owns it, maybe a bit too much."
            fuy "Sometimes it feels like everything he says is specifically meant to make me uncomfortable, or annoyed."
            jump recallMenu
        "Ryuji Konpeki":
            show fuyu neut
            with Dissolve(0.5)
            fuy "A History major. He's obsessed with ancient knights and samurai, especially the way they fought."
            fuy "Not to mention he's super immature. Lately, he's taken to nicknaming us after seasons."
            fuy "He's also very protective of his sister, Hime. The two of them are always together. It's hard to imagine him without her, and vice versa."
            jump recallMenu
        "Himiko Konpeki":
            show fuyu neut
            with Dissolve(0.5)
            fuy "Right, Himiko. She goes by Hime, and she's the only one of us that doesn't attend college."
            fuy "She works as a graffiti artist and a cashier and hates that dead-end job as much as I hate mine."
            show fuyu smile
            with Dissolve(0.5)
            fuy "She's even told me that she started tagging the area around her workplace."
            show fuyu neut
            with Dissolve(0.5)
            fuy "Her nickname comes from a childhood love of princesses, and it stuck. Thanks to her brother, that is."
            jump recallMenu
        "Rei Amanshi":
            show fuyu neut
            with Dissolve(0.5)
            fuy "A Theology major. He practices some weird niche religon, one that his family holds a lot of power in. He stands to inheirit that responsibility."
            show fuyu down
            with Dissolve(0.5)
            fuy "Sometimes, I pity him in a weird way. We were both put in such a bad situation by our parents."
            fuy "But Rei doesn't seem to notice that all the pressure being put on him is unhealthy."
            fuy "And, worse yet, he was one of the people to see me at my worst earlier today."
            jump recallMenu
        "Move Foward":
            jump textMessage
#Spacer

#Text Message time
label textMessage:
    show fuyu neut
    with Dissolve(0.5)
    nar "As the boy finishes his recollection, his phone begins to buzz. When he picks it up, a message from someone appears on the screen."
    nar "A message from..."
    menu:
        "Haruki":
            jump HarukiMessage
        "Ryuji":
            jump RyujiMessage
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
    $ HarukiChat = True
    show fuyu really at farleft
    with moveinright
    show haruki smug at farright
    with Dissolve(0.5)
    thar "Heya there, Fuyu. Are you up to anything? I'd love to swing by and snatch you up~."
    tfuy "Not now Haruki, God, especially not right now."
    show haruki frown
    with Dissolve(0.5)
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
    with Dissolve(0.5)
    tfuy "It's not \"Fuyu\"."
    tfuy "It's not \"sweetheart\" or \"doll\"."
    tfuy "It's Fuyuhiko."
    $ renpy.pause(2.0)
    thar "Fuyu..."
    tfuy "I'm done talking with you."
    play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0
    nar "The boy powers off his phone. If Haruki continued messaging him, he didn't recieve it."
    show fuyu down at center
    with moveinleft
    hide haruki frown
    with Dissolve(0.5)
    nar "Exhausted, the boy crawls into bed, and begins to fall into unconsciousness. The events of the day racing through his head and dreams."
    scene black
    with Dissolve(0.5)
    jump Day2
#Spacer

label RyujiMessage:
    nar "...Ryuji."
    $ RyujiChat = True
    show fuyu neut at farleft
    with moveinright
    show ryuji excited at farright
    with Dissolve(0.5)
    tryu "winter! you HAVE to see this!"
    $ renpy.pause(2.0)
    show ryuji err
    with Dissolve(0.5)
    nar "Nothing happens, Ryuji must have sent Winter a picture without any text for his screen-reader to pick up on, again."
    tryu "oh right"
    tryu "sorry winter"
    tfuy "It's fine, Ryuji."
    tryu "if its fine then why are you calling me that! >:("
    tfuy "Okay then,"
    show fuyu smile
    with Dissolve(0.5)
    tfuy "Fall."
    show fuyu neut
    show ryuji hap
    with Dissolve(0.5)
    tryu "there you go!"
    show ryuji excited
    with Dissolve(0.5)
    tryu "here! i'll describe it to you! oh, and i have waaay more to talk to you about!"
    scene black
    with Dissolve(0.5)
    nar "The boys continued chatting about nothing of importance. It was a nice distraction for Fuyuhiko, one he really needed."
    jump Day2
#Spacer

label HimeMessage:
    nar "...Hime."
    $ HimeChat = True
    show fuyu neut at farleft
    with moveinright
    show hime yo at farright
    with Dissolve(0.5)
    thim "You are going to love what I just did."
    nar "Hime sends a image of her tagging her store with a huge middle-finger along with an audio transcription."
    show fuyu smile
    with Dissolve(0.5)
    tfuy "Amazing."
    thim "I know right!?"
    show hime cool
    with Dissolve(0.5)
    thim "I've been waiting to do this for so long."
    tfuy "What broke the camel's back?"
    $ renpy.pause(2.0)
    show hime uncomfy
    with Dissolve(0.5)
    thim "My asshat of a manager threatened my job because I refused to go out with him."
    show fuyu down
    with Dissolve(0.5)
    tfuy "Oh."
    thim "Yeah."
    $ renpy.pause(3.0)
    show fuyu neut
    with Dissolve(0.5)
    tfuy "I tried to get out of my so-called \"Accessibility Accomodations\" again today."
    tfuy "All that and they can't spare the resources to actually let me do my job myself."
    show hime cool
    with Dissolve(0.5)
    thim "And how'd that go?"
    tfuy "Not great."
    thim "Our bosses suck, huh?"
    show fuyu neut
    with Dissolve(0.5)
    tfuy "Yup."
    thim "I'll see you tomorrow, Fuyuhiko."
    hide hime cool
    with Dissolve(0.5)
    tfuy "You too, Hime."
    show fuyu down at center
    with moveinleft
    fuy "I think I need to work on my people skills."
    scene black
    with Dissolve(0.5)
    jump Day2
#Spacer

label ReiMessage:
    nar "...Rei."
    $ ReiChat = True
    show fuyu down at farleft
    with moveinright
    show rei cautious at farright
    with Dissolve(0.5)
    trei "Shiro, are you there?"
    $ renpy.pause(3.0)
    trei "Shiro, please."
    $ renpy.pause(1.0)
    trei "Shiro I can see the read message."
    tfuy "What do you want, Rei?"
    trei "I just wanted to make sure you were okay."
    tfuy "I'm fine. Leave me alone."
    trei "Are you sure, Shiro?"
    tfuy "Don't make me block you, Rei."
    $ renpy.pause(1.0)
    nar "Fuyu sits for a few moments, waiting, daring for a text that will never come."
    scene black
    with Dissolve(0.5)
    nar "Instead, he simply powers off his phone and heads to bed, trying to forget the events of the day."
    jump Day2
#Spacer

label WorkMessage:
    nar "...Her."
    $ WorkChat = True
    hide fuyu neut
    show the email at truecenter
    with Dissolve(0.5)
    nar "It was her."
    show fuyu snap
    hide the email
    fuy "That fucking bitch."
    fuy "She just aired our private conversation to the whole cafe!"
    fuy "It's bad enough putting up with her shit when it was just us."
    fuy "I bet she thinks she's doing what's best for me. I-"
    nar "Winter seethes, fury threatening to cloud his mind."
    fuy "I'M NOT A FUCKING KID ANYMORE DAD!"
    $ renpy.pause(2.0)
    show fuyu what
    with Dissolve(0.5)
    fuy "I-"
    $ renpy.pause(2.0)
    show fuyu down
    with Dissolve(0.5)
    fuy "I need some sleep."
    scene black
    with Dissolve(0.5)
    jump Day2
#Spacer





#Day 2
label Day2:
    nar "End of Day 1."
    nar "Start of Day 2."
    scene apartment day
    with Dissolve(0.5)
    nar "The next day passed mostly uneventfully."
    scene hallway day
    with Dissolve(0.5)
    nar "The same classes in the same order and the same motions."
    scene classroom evening
    with Dissolve(0.5)
    nar "That was until after school."
    show ryuji hap at left
    show hime cool at farleft
    show rei distracted at right
    show haruki smug at farright
    with Dissolve(0.5)
    #checks if Haruki was texted last night
    if HarukiChat:
        show haruki frown at farright
        with Dissolve(0.5)
    nar "Club time, that is."
    show fuyu neut at center
    with Dissolve(0.5)
    fuy "Really, our club was just an excuse to use this classroom after school hours, we never really did anything with it but talk and hang out. It was convienent."
    fuy "But club time does bring up the question of who to spend it with."
    menu:
        "Ryuji and Hime":
            hide haruki
            hide rei
            with Dissolve(0.5)
            show ryuji at farright
            with moveinleft
            show hime at farleft
            with moveinleft
            jump RyujiandHime
        "Haruki and Rei":
            hide ryuji
            hide hime
            with Dissolve(0.5)
            show haruki at farright
            with moveinright
            show rei at farleft
            with moveinright
            jump HarukiandRei
        "Nobody":
            hide ryuji
            hide hime
            hide rei
            hide haruki
            with Dissolve(0.5)
            jump Nobody
#Spacer

label RyujiandHime:
    if HimeChat:
        ryu "Hey Winter!"
        him "Nice to see you, Fuyuhiko."
        show fuyu smile
        with Dissolve(0.5)
        fuy "You too, Hime"
        show ryuji excited
        with Dissolve(0.5)
        ryu "Hey! Can you help us resolve something?"
        ryu "Which looks cooler, the pen or the sword?"
        show fuyu what
        with Dissolve(0.5)
        him "No offense Fuyuhiko, but did you just ask the blind kid about if fighting or art looks cooler Ryuji?"
        him "Like, looks, in specific?"
        show ryuji err
        with Dissolve(0.5)
        ryu "Just because he's going to pick the much cooler swords doesn't mean he's biased."
        nar "Normally this would be the point in the the story where a couple text boxes show up for who Fuyuhiko should agree with."
        nar "Unfortunately..."
        show fuyu neut
        with Dissolve(0.5)
        fuy "Yeah that is pretty stupid."
        fuy "I mean, coolness is such an arbitary thing, and I. Can't. See. Shit."
        fuy "But, for the sake of agruement, Hime wins."
        show ryuji huh
        show hime yo
        ryu "what"
        show ryuji err
        with Dissolve(0.5)
        ryu "But whyyyyy."
        him "Just face the fact that I'm better, bro."
        ryu "No fair!"
        show hime cool
        with Dissolve(0.5)
        him "Life isn't fair."
        him "Your brilliant decision does remind me Fuyuhiko, I have some art stuff back home I could show you after school if you want."
        show ryuji excited
        with Dissolve(0.5)
        ryu "Oh! Please come over!"
        ryu "I got some new games I wanna show you!"
        show ryuji hap
        with Dissolve(0.5)
        fuy "Well, I don't have anything else to do so..."
        show fuyu smile
        with Dissolve(0.5)
        fuy "Why not?"
        jump KonpekiHouse
    if RyujiChat:
        ryu "Winter, Hey!!!"
        him "Hanging out with the cool kids huh, Fuyuhiko?"
        show fuyu smile
        with Dissolve(0.5)
        fuy "You know it."
        show ryuji excited
        with Dissolve(0.5)
        ryu "Hey! Can you help us resolve something?"
        ryu "Which looks cooler, the pen or the sword?"
        show fuyu what
        with Dissolve(0.5)
        him "No offense Fuyuhiko, but did you just ask the blind kid about if fighting or art looks cooler Ryuji?"
        him "Like, looks, in specific?"
        show ryuji err
        with Dissolve(0.5)
        ryu "Just because he's going to pick the much cooler swords doesn't mean he's biased."
        nar "Normally this would be the point in the the story where a couple text boxes show up for who Fuyuhiko should agree with."
        nar "Unfortunately..."
        show fuyu neut
        with Dissolve(0.5)
        fuy "Yeah that is pretty stupid."
        fuy "I mean, coolness is such an arbitary thing, and I. Can't. See. Shit."
        ryu "I guess that's fair..."
        him "There's the Fuyuhiko we know and love."
        show ryuji excited
        with Dissolve(0.5)
        ryu "Oh! Speaking of loving you!"
        ryu "Do you wanna come over after club?"
        ryu "I got some new games I wanna show you!"
        him "We could also paint some shit in my room."
        fuy "I don't have anything else to do so..."
        show fuyu smile
        with Dissolve(0.5)
        fuy "Why not?"
        jump KonpekiHouse
    else:
        ryu "Hey Winter!"
        him "Hanging out with the cool kids huh, Fuyuhiko?"
        show fuyu smile
        with Dissolve(0.5)
        fuy "You know it."
        show ryuji excited
        with Dissolve(0.5)
        ryu "Hey! Can you help us resolve something?"
        ryu "Which looks cooler, the pen or the sword?"
        show fuyu what
        with Dissolve(0.5)
        him "No offense Fuyuhiko, but did you just ask the blind kid about if fighting or art looks cooler Ryuji?"
        him "Like, looks, in specific?"
        show ryuji err
        with Dissolve(0.5)
        ryu "Just because he's going to pick the much cooler swords doesn't mean he's biased."
        nar "Normally this would be the point in the the story where a couple text boxes show up for who Fuyuhiko should agree with."
        nar "Unfortunately..."
        show fuyu neut
        with Dissolve(0.5)
        fuy "Yeah that is pretty stupid."
        fuy "I mean, coolness is such an arbitary thing, and I. Can't. See. Shit."
        ryu "I guess that's fair..."
        him "There's the Fuyuhiko we know and love."
        show ryuji excited
        with Dissolve(0.5)
        ryu "Oh! Speaking of loving you!"
        ryu "Do you wanna come over after club?"
        $ renpy.pause(1.0)
        show ryuji err
        with Dissolve(0.5)
        ryu "Oh, um, not like... that..."
        show ryuji excited
        with Dissolve(0.5)
        ryu "I got some new games I wanna show you!"
        him "We could also paint some shit in my room."
        show ryuji hap
        with Dissolve(0.5)
        fuy "I don't have anything else to do so..."
        show fuyu smile
        with Dissolve(0.5)
        fuy "Why not?"
        jump KonpekiHouse
#Spacer

label HarukiandRei:
    if HarukiChat:
        har "Oh. Hi... Fuyuhiko."
        rei "Hello, Shiro."
        har "I was... {i}Ahem.{/i} Just getting this guy to talk about that great fire in the sky."
        show fuyu what
        with Dissolve(0.5)
        fuy "The Sun?"
        show rei cautious
        with Dissolve(0.5)
        rei "No!"
        rei "Lantern. He means Lantern."
        fuy "Lantern?"
        show haruki smug
        with Dissolve(0.5)
        har "That god his parents forced our boy into worshipping."
        har "I mean seriously. You're so obsessed, it's kinda pathetic."
        show rei shatter
        with Dissolve(0.5)
        rei "Dammit Haruki, They didn't force me into ANYTHING!"
        show haruki frown
        show fuyu down
        with Dissolve(0.5)
        $ renpy.pause(1.0)
        har "Hey..."
        show fuyu really
        with Dissolve(0.5)
        fuy "Shut up, Haruki."
        show rei cautious
        with Dissolve(0.5)
        rei "Look. You want proof of Lantern's glory? Come to my house tonight Haruki."
        fuy "I don't think that's a good idea Rei."
        nar "Haruki grumbled, he had something we wanted to say but he held himself back."
        rei "Well, how about you come over, Shiro?"
        show haruki whatever
        with Dissolve(0.5)
        har "Really? So you're just gonna invite him over. Just like that? What are you planning on doing? Huh, Rei?"
        rei "Nothing! We're friends!"
        har "Nothing!? Because it seems to me like you're planning a little sacrifice!"
        fuy "Haruki!"
        show haruki angry
        with Dissolve(0.5)
        har "Oh fuck you too Fuyuhiko!"
        show haruki shut
        with Dissolve(0.5)
        har "I'm done with this, I'll see you all next time..."
        hide haruki
        with Dissolve(0.5)
        show rei at left
        with moveinright
        show fuyu at right
        with moveinleft
        rei "I can't believe him."
        show rei distracted
        with Dissolve(0.5)
        rei "So Shiro, are you coming over?"
        fuy "Sure."
        rei "Good. We'll leave once club is over."
        jump ReiHouse
    elif ReiChat:
        har "Hey Fuyu~"
        rei "Shiro."
        har "I was just getting this guy to talk about that great fire in the sky."
        show fuyu what
        with Dissolve(0.5)
        fuy "The Sun?"
        rei "Lantern. He means Lantern."
        fuy "Lantern?"
        har "That god his parents forced our boy into worshipping."
        har "I mean seriously. You're so obsessed, it's kinda pathetic."
        $ renpy.pause(2.0)
        rei "Shiro. Can I talk to you, in private?"
        fuy "Oh, uh, sure."
        har "Hey, where are you going? I was just teasing him."
        rei "Sure you were, Supai."
        scene hallway afternoon
        hide haruki
        show rei cautious at left
        show fuyu what at right
        with Dissolve(0.5)
        rei "About last night."
        nar "Fuyuhiko groans, remembering their conversation, and what preceeded it."
        show fuyu really
        with Dissolve(0.5)
        fuy "Really, Rei? You don't have to do this, I'm fine."
        rei "I know you aren't Shiro, I saw what happened."
        rei "I just, want to know what's going on."
        show fuyu down
        with Dissolve(0.5)
        nar "Fuyuhiko doesn't respond, instead opting to sit with the other boy in scilence."
        rei "If you don't tell me, Lantern will."
        fuy "You can't do that."
        rei "I can, Shiro."
        fuy "Prove it."
        rei "I- I can't not here."
        rei "Come to my house, after club, I'll show you then, okay?"
        hide rei
        with Dissolve(0.5)
        nar "Rei quickly went back into the classroom alone, but it didn't take long for someone else to emerge from the doorway."
        show haruki frown at left
        with moveinleft
        har "What was that about? I didn't mean to hurt him. Honest."
        har "I just, went a little far."
        fuy "This isn't about you Haruki."
        har "What?"
        fuy "It's between me and him, he invited me over to his."
        har "Really? Are you gonna go?"
        show haruki smug
        with Dissolve(0.5)
        har "There might be another boy would love you at his house~"
        menu:
            "I'm going to Rei's.":
                har "Well then."
                har "Suit yourself, Fuyu."
                hide haruki
                with Dissolve(0.5)
                nar "Fuyu sat in the hallway for the rest of the club time, thinking about what the hell was going to transpire at Rei's house."
                nar "Until the boy appeared to show him."
                jump ReiHouse
            "Oh?":
                har "How about coming to that other boy's house?"
                show fuyu neut
                with Dissolve(0.5)
                fuyu "Okay then, I don't see why not."
                jump HarukiHouse
    else:
        har "Hey Fuyu~"
        rei "Hello, Shiro."
        har "I was just getting this guy to talk about that great fire in the sky."
        show fuyu what
        with Dissolve(0.5)
        fuy "The Sun?"
        show rei cautious
        with Dissolve(0.5)
        rei "No!"
        rei "Lantern. He means Lantern."
        fuy "Lantern?"
        har "That god his parents forced our boy into worshipping."
        har "I mean seriously. You're so obsessed, it's kinda pathetic."
        show rei shatter
        with Dissolve(0.5)
        rei "Dammit Haruki, They didn't force me into ANYTHING!"
        show haruki frown
        show fuyu down
        with Dissolve(0.5)
        $ renpy.pause(2.0)
        har "Rei..."
        har "I- I was just teasing."
        rei "Can you hear yourself!?"
        rei "I can't believe you. You can't even believe me, even for a second!"
        show rei disappoint
        with Dissolve(0.5)
        rei "What about you Shiro, come to my house after club, I'll show you Lantern's flame."
        show haruki whatever
        with Dissolve(0.5)
        har "Don't do that, don't drag him into this."
        har "If you're going that then, Fuyu, you should come to mine. I haven't gotten a chance to really talk to you lately."
        nar "This whole conversation, Fuyuhiko's barely processed what happened. And now a choice to make?"
        nar "How about we help our Silver Boy."
        nar "Who's offer should he accept?"
        menu:
            "Haruki's":
                rei "Oh."
                show haruki smug
                with Dissolve(0.5)
                har "Good choice, Fuyu."
                hide rei
                with Dissolve(0.5)
                show fuyu at left
                with moveinleft
                nar "The rest of the time in club passed awkwardly, Rei eventually drifting to the Konpeki siblings."
                nar "After that, you left with Haruki to his house."
                jump HarukiHouse
            "Rei's":
                har "Fine."
                hide haruki
                with Dissolve(0.5)
                show fuyu at right
                with moveinright
                nar "Haruki left the club after that, the rest of you followed not soon after."
                jump ReiHouse
#Spacer

label Nobody:
    if WorkChat:
        nar "Fuyuhiko is far too tired to socialize, he's still thinking about that email he recieved yesterday."
        nar "Accomadations are one thing, when they actually help him do his damn job."
        nar "But this? He's not a toddler, he's more than capable of handling himself without hurting someone."
        show fuyu snap
        with Dissolve(0.5)
        nar "More than capable of working without a babysitter watching his every move."
        nar "And all this but they can't put braille labels on fucking anything!"
        fuy "Ugh!"
        nar "His clubmates eye Fuyuhiko, more concerned than anything."
        show fuyu neut
        with Dissolve(0.5)
        fuy "I'm going home, I-I need to be alone."
        nar "A few of his friends hesistate before saying nothing, but Fuyuhiko doesn't wait for their approval."
        nar "Fuyuhiko grabs his bag and heads back to his apartment."
        jump HomeAlone
    else:
        nar "Fuyuhiko is far too tired to socialize, he sits alone in a far corner of the room."
        show haruki shut
        show hime uncomfy
        show rei disappoint
        show ryuji so
        with Dissolve(0.5)
        nar "His clubmates appear every now again, trying to make conversation."
        show fuyu really
        with Dissolve(0.5)
        nar "Fuyuhiko gives them the mininmum response beyond \"Fuck off.\""
        hide haruki
        hide hime
        hide rei
        hide ryuji
        with Dissolve(0.5)
        nar "It's clear Fuyuhiko is struggling with something but he won't talk about it."
        menu:
            "Look at it.":
                $ WorkChat = True
                hide fuyu
                show the email at truecenter
                with Dissolve(0.5)
                nar "The email."
                hide the email
                show fuyu really
                with Dissolve(0.5)
                nar "They treat him like a child."
                nar "So incapable, so stupid."
                nar "It's not that Fuyuhiko doesn't need help sometimes, no."
                nar "It's their idea of helping him."
                nar "They won't give him the tools to do his job properly himself, braile labels, text readers."
                nar "So they stick him with a babysitter, someone who has the mercy to pretend he's helping."
                nar "It's like he's an infant."
                fuy "I'm sick of it."
                nar "Eventually Fuyuhiko gets tired of pretending he's participating in club."
                nar "He goes home."
                jump HomeAlone
            "Don't.":
                nar "He can't afford to talk about it."
                nar "He can't afford to think about it."
                nar "He can't afford to look at it."
                nar "Eventually, he goes home."
                jump HomeAlone
#Spacer

label KonpekiHouse:
    #Regardless of route, Fuyuhiko is ultimately invited by both siblings for art stuff and video games respectively
    #Should offer another choice between the two and then do the thing
    #Then Haruki calls Hime and tells them to meet up in club room tomorrow even though they don't have club
    hide fuyu
    hide hime
    hide ryuji
    scene road day
    with Dissolve(0.5)
    nar "The drive to the Konpeki place isn't long. Leave it to Himiko to know all the possible shortcuts."
    scene konpeki day
    nar "And soon enough, they're home."
    show ryuji excited at farleft
    with Dissolve(0.5)
    ryu "Come on Winter!"
    show fuyu smile at center
    with Dissolve(0.5)
    fuy "I'm coming! I'm coming."
    show hime yo at far right
    him "Slow down!"
    show ryuji hap
    show hime cool
    show fuyu neut
    with Dissolve(0.5)
    nar "Fuyuhiko brings out his cane and the Konpeki siblings show him around the house."
    nar "But soon enough it comes down to another competition between the siblings for Fuyuhiko's attention."
    nar "Maybe he should have a little less agency this time."
    ryu "Come on dude! We have gotta try out The Remaining of Them!"
    him "Hang out with who you want man, but I did get some cool new spray paint cans, wanna see how they sound?"
    menu:
        "The Remaining of Them":
            #This references the Last of Us Part 2 and the insane blind accessiblity options it has
            #If you want, you could research them and include them in the conversation
            #Or just have Ryuji and Fuyuhiko talk about whatever
            fuy "Let's try the Remaining of Them."
            show ryuji excited
            with Dissolve(0.5)
            #If you could get this to go off-screen that would be cool
            ryu "Let's gooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo!"
            him "Well I'll see you boys later, I've still got some spray paint calling my name."
            show ryuji hap
            with Dissolve(0.5)
            hide hime with moveinleft
            $renpy.pause(1.0)
            show ryuji at left with moveinleft
            show fuyu at right with moveinleft
            nar "Ryuji gets busy setting up the game while Fuyuhiko waits on the couch."
            ryu "Do you play many games on your own Winter?"
            fuy "No, why?"
            ryu "Well, I've helped you play a ton of games, but the Remaining of Them is awesome and has a ton of great accessibility features."
            ryu "You could probably play it on your own!"
            ryu "If you wanted to borrow it."
            show fuyu smile with Dissolve(0.5)
            fuy "That's really sweet Ryuji."
            show fuyu neut with Dissolve(0.5)
            fuy "But I don't have a console."
            show ryuji err with Dissolve(0.5)
            ryu "Oh. yeah..."
            $renpy.pause(0.5)
            show ryuji hap with Dissolve(0.5)
            ryu "Well we can still play now!"
            nar "The two play for a few hours. Ryuji tries his best not to intervene too often, happy to watch his friend play."
            show hime cool at farleft with moveinleft
            show ryuji at farright with moveinleft
            nar "Until Hime interrupts them."
            him "Hey guys, Haruki just called."
            show fuyu really with Dissolve(0.5)
            ryu "Haruki?"
            show fuyu at center with moveinright
            fuy "God, what does he want now?"
            him "He said we should meet up at the clubroom tomorrow."
            ryu "But we don't have club on Tuesdays?"
            show hime uncomfy with Dissolve(0.5)
            him "He said he wants to talk, he sounded really freaked out."
            ryu "What do you think Winter?"
            menu:
                "Meet up with Haruki tomorrow.":
                    $ HarukiMeeting = True
                    fuy "I guess we should meet up with him tomorrow."
                    show hime cool with Dissolve(0.5)
                    him "Okay then."
                    ryu "I'll see you afterschool then!"
                    nar "Fuyuhiko shifts around in his seat uncomfortably, then hands his controller back to Ryuji."
                    fuy "Hey Hime, it's getting kinda late. Could you give me a ride home?"
                    him "Sure."
                    jump Day3
                "Fuck him.":
                    fuy "Honestly? Fuck him."
                    show ryuji err
                    ryu "Oh."
                    fuy "You two can meet up with him if you want."
                    fuy "I'm not coming."
                    show ryuji so with Dissolve(0.5)
                    ryu "Guess we're not going then."
                    him "I'll still go. I want to see what this is about."
                    him "This sounds serious."
                    fuy "Suit yourself."
                    ryu "Hey Winter, it's getting kinda late."
                    ryu "You wanna go home?"
                    fuy "Yeah, sure."
                    jump Day3
        "Spray Paint":
            #Himiko likes to paint, Fuyuhiko likes to sit and listen
            #It's more about the meaning behind the rebellion y'know
            #Probably have them talk about their jobs? Or maybe Haruki.
            fuy "I've gotta hear this new spray paint."
            show ryuji so with Dissolve(0.5)
            ryu "If you say so..."
            hide ryuji with moveinright
            show fuyu at left with moveinright
            show hime at right with moveinright
            him "Don't worry about him, he'll be over it within the hour."
            nar "Hime leads Fuyuhiko to her easel, judging by the crunching underfoot, it seems she's taken proper precautions to protect the house."
            him "Welcome to the proverbial Art Corner."
            nar "Himiko shakes up a can and begins to paint with a satisfying hiss."
            nar "Hime has always shown mastery over spray paint, Winter can tell by the controlled highs and lows of the hissing's volume."
            nar "It's nice listening, though granted, nothing can match the satisfaction of painting a wall that actually deserved it."
            nar "But despite the canvas she's painting now having done nothing wrong, Hime's painting feels angry almost."
            fuy "Wanna talk?"
            if HimeChat:
                show hime uncomfy with Dissolve(0.5)
                him "Well you kinda already know what happened."
                nar "Fuyuhiko nods, her manager, the tagging, she told him last night."
                fuy "But didn't you already tag the place."
                show hime cool with Dissolve(0.5)
                him "Yeah, well, it wasn't enough."
                nar "The hissing grows louder, more intense for a moment."
                nar "A part of Fuyuhiko enjoys it, the sound of defiance, of the rage, of revolution."
                nar "A part of Fuyuhiko just feels bad for his friend."
                nar "Then Hime's phone starts to ring."
                him "Shit."
                $renpy.pause(1.0)
                him "It's Haruki."
                show fuyu really with Dissolve(0.5)
                nar "Fuyuhiko motions her to take the call, hesitantly."
                him "Yeah?"
                nar "..." 
                him "Uh-huh" 
                nar "..."
                him "No, he's with me." 
                nar "..." 
                him "Fuyuhiko too, yeah." 
                nar "..." 
                him "Okay, talk to you later."
                nar "Hime ends the call and looks at Fuyuhiko with a sigh."
                him "Let's go find Ryuji."
                scene konpeki day
                show hime cool at farleft
                show ryuji at farright
                show fuyu at center
                nar "Ryuji is laying down on the couch, he looks up when Hime and Fuyuhiko enter."
                him "Hey dude, Haruki just called."
                him "He said we should meet up at the clubroom tomorrow."
                ryu "But we don't have club on Tuesdays?"
                show hime uncomfy with Dissolve(0.5)
                him "He said he wants to talk, he sounded really freaked out."
                ryu "What do you think Winter?"
                menu:
                "Meet up with Haruki tomorrow.":
                    $ HarukiMeeting = True
                    fuy "I guess we should meet up with him tomorrow."
                    show hime cool with Dissolve(0.5)
                    him "Okay then."
                    ryu "I'll see you afterschool then!"
                    nar "Fuyuhiko shifts on his feet uncomfortably."
                    fuy "Hey Hime, it's getting kinda late. Could you give me a ride home?"
                    him "Sure."
                    jump Day3
                "Fuck him.":
                    fuy "Honestly? Fuck him."
                    show ryuji err
                    ryu "Oh."
                    fuy "You two can meet up with him if you want."
                    fuy "I'm not coming."
                    show ryuji so with Dissolve(0.5)
                    ryu "Guess we're not going then."
                    him "I'll still go. I want to see what this is about."
                    him "This sounds serious."
                    fuy "Suit yourself."
                    him "Hey Winter, it's getting kinda late."
                    him "You wanna go home?"
                    fuy "Yeah, sure."
                    jump Day3
            else:
                $ HimeChat = True
                him "It's fucking Dave. My manager."
                show hime uncomfy with Dissolve(0.5)
                him "He threatened my job yesterday Fuyuhiko. Because I wouldn't go out with him."
                him "God, I hate men."
                show hime cool with Dissolve(0.5)
                him "No offense."
                nar "Fuyuhiko shrugs, what could he say?."
                show fuyu really with Dissolve(0.5) 
                fuy "That's awful Hime..."
                show hime uncomfy with Dissolve(0.5)
                him "I know right!?"
                show hime cool with Dissolve(0.5)
                him "I'll be alright though, I just wanted to get this out of my system."
                show fuyu neut with Dissolve(0.5)
                him "You seem like you wanna talk too, Fuyuhiko."
                fuy "It's nothing, I'm fine."
                nar "Hime shrugs, Fuyuhiko can tell as the paint can stops hissing for a moment to accomodate it."
                him "If you say so just know-"
                $renpy.pause(1.0)
                him "Haruki's calling."
                show fuyu really with Dissolve(0.5)
                nar "Fuyuhiko motions her to take the call, hesitantly."
                him "Yeah?"
                nar "..." 
                him "Uh-huh" 
                nar "..."
                him "No, he's with me." 
                nar "..." 
                him "Fuyuhiko too, yeah." 
                nar "..." 
                him "Okay, talk to you later."
                nar "Hime ends the call and looks at Fuyuhiko with a sigh."
                him "Let's go find Ryuji."
                scene konpeki day
                show hime cool at farleft
                show ryuji at farright
                show fuyu at center
                nar "Ryuji is laying down on the couch, he looks up when Hime and Fuyuhiko enter."
                him "Hey dude, Haruki just called."
                him "He said we should meet up at the clubroom tomorrow."
                ryu "But we don't have club on Tuesdays?"
                show hime uncomfy with Dissolve(0.5)
                him "He said he wants to talk, he sounded really freaked out."
                ryu "What do you think Winter?"
                menu:
                "Meet up with Haruki tomorrow.":
                    $ HarukiMeeting = True
                    fuy "I guess we should meet up with him tomorrow."
                    show hime cool with Dissolve(0.5)
                    him "Okay then."
                    ryu "I'll see you afterschool then!"
                    nar "Fuyuhiko shifts on his feet uncomfortably."
                    fuy "Hey Hime, it's getting kinda late. Could you give me a ride home?"
                    him "Sure."
                    jump Day3
                "Fuck him.":
                    fuy "Honestly? Fuck him."
                    show ryuji err
                    ryu "Oh."
                    fuy "You two can meet up with him if you want."
                    fuy "I'm not coming."
                    show ryuji so with Dissolve(0.5)
                    ryu "Guess we're not going then."
                    him "I'll still go. I want to see what this is about."
                    him "This sounds serious."
                    fuy "Suit yourself."
                    him "Hey Winter, it's getting kinda late."
                    him "You wanna go home?"
                    fuy "Yeah, sure."
                    jump Day3
#Spacer 

label HarukiHouse:
    nar "Placeholder"
#Spacer

label ReiHouse:
    #Rei means to show Fuyuhiko the glory of Lantern
    #But Haruki suspects something is up, he's watching
    #And Rei /will/ get possessed after all
    scene road night
    show rei cautious at right
    show fuyu neut at left
    with Dissolve(0.5)
    nar "Rei is quiet the whole drive to his house."
    nar "There's a weird sort of air around him, nervous and detirmination bundled up together."
    nar "Fuyuhiko doesn't say anything though."
    scene rei night
    nar "Not until they're there."
#Spacer

label HomeAlone:
    scene 
    if WorkChat:
        scene apartment afternoon
        show fuyu really
        with Dissolve(0.5)
        nar "Fuyuhiko throws his bag onto his couch, and starts to pace around his room."
        fuy "What gives them the right!"
        show fuyu snap
        with Dissolve(0.5)
        fuy "WHAT GIVES THEM THE DAMN RIGHT!"
        show fuyu really
        with Dissolve(0.5)
        fuy "I can't stop thinking about it."
        fuy "The babying, the control, the lack of fucking faith."
        fuy "I am valuable! I am!"
        fuy "I could do my job if you just gave me the actual damn tools to do it! Ugh!"
        hide fuyu
        with moveinright
        nar "Fuyuhiko goes into the bathroom. He throws water into his face until he feels a little calmer."
        show fuyu
        with moveinright
        fuy "I need to lie down..."
        nar "And soon enough, he begins to drift off into sleep..."
    else:
        scene apartment day
        show fuyu down
        with Dissolve(0.5)
        nar "Fuyuhiko is exhausted when he arrives home."
        nar "He's already exhausted."
        nar "It's not even late yet, it's even 6 o'clock."
        nar "How unfair is that..."
        scene apartment afternoon
        with Dissolve(0.5)
        nar "He lays down on his couch, twiddling his thumbs on his phone."
        nar "He watches and listens and consumes anything he can get his hands on."
        nar "Anything other than thinking about what's bothering him."
        nar "Eventually he falls asleep."
        jump Day3
#Spacer





#Day3
label Day3:
    nar "Placeholder."
#Spacer