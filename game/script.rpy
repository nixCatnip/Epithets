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
    $ HarukiMeeting = False
    $ NoMeeting = False
    $ DeniedMeeting = False
    $ RyujiGoing = True
    #Spacer
    play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0 volume 0.5
    nar "Ah, San Francisco, the salty air of the sea mixed with the salty attitudes of young adults experiencing true independence for the first time in their lives."
    nar "Five of these young adults attend the local prestigious university, hailing from across the sea, here to expand their hearts and minds."
    nar "Ah, here comes one now, arriving home after a long day of work. Perhaps the saltiest of them all, Fuyuhiko Shiro."
    scene apartment night
    show fuyu really
    with Dissolve(0.5)
    fuy "I can't believe that woman!"
    fuy "She always thinks she knows what's best for me. She's not my fucking mom!"
    nar "He stomps across his small apartment and flips open a laptop, furiously scrolling through social media."
    nar "Perhaps we should have him recall a few of his companions to take his mind off of things."
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
    play sound "audio/phone.mp3" volume 0.5
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
    play sound "audio/phone.mp3" volume 0.5
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
    tfuy "MY NAME IS FUYUHIKO." with hpunch
    show fuyu really
    with Dissolve(0.5)
    tfuy "It's not \"Fuyu\"."
    tfuy "It's not \"sweetheart\" or \"doll\"."
    tfuy "It's Fuyuhiko."
    $ renpy.pause(2.0)
    thar "Fuyu..."
    tfuy "I'm done talking with you."
    play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0 volume 0.5
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
    play sound "audio/phone.mp3" volume 0.5
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
    play sound "audio/phone.mp3" volume 0.5
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
    play sound "audio/phone.mp3" volume 0.5
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
    play sound "audio/phone.mp3" volume 0.5
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
    stop music
    fuy "I'M NOT A FUCKING KID ANYMORE DAD!" with hpunch
    $ renpy.pause(2.0)
    show fuyu what
    with Dissolve(0.5)
    fuy "I-"
    play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0 volume 0.5
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
        stop music
        rei "Dammit Haruki, They didn't force me into ANYTHING!" 
        with hpunch
        show haruki frown
        show fuyu down
        with Dissolve(0.5)
        $ renpy.pause(1.0)
        play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0 volume 0.5
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
        menu:
            "Intervene":
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
            "Standby":
                rei "I don't need to take this."
                rei "Sorry, Shiro, I'm going home."
                rei "You can come over some other time."
                hide rei
                with moveoutleft
                show haruki smug at right with moveinleft(0.5)
                show fuyu at left with moveinright(0.5)
                har "Well. Since you're recently free..."
                show fuyu really
                with Dissolve(0.5)
                fuy "Really?"
                har "You got anything better to do?"
                fuy "... No."
                har "Then come to mine!"
                fuy "... "
                extend "... "
                extend "Fine."
                jump HarukiHouse
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
        nar "Fuyuhiko doesn't respond, instead opting to sit with the other boy in silence."
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
                fuy "Okay then, I don't see why not."
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
        stop music
        rei "Dammit Haruki, They didn't force me into ANYTHING!" 
        with hpunch
        show haruki frown
        show fuyu down
        with Dissolve(0.5)
        $ renpy.pause(2.0)
        play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0 volume 0.5
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
    with Dissolve(0.5)
    nar "And soon enough, they're home."
    show ryuji excited at farleft
    with Dissolve(0.5)
    ryu "Come on Winter!"
    show fuyu smile at center
    with Dissolve(0.5)
    fuy "I'm coming! I'm coming."
    show hime yo at farright
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
            hide hime with moveoutright
            $renpy.pause(1.0)
            show ryuji at left 
            with moveinleft
            show fuyu at right 
            with moveinleft
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
            show hime cool at farleft 
            with moveinleft
            show ryuji at farright 
            with moveinleft
            nar "Until Hime interrupts them."
            him "Hey guys, Haruki just called."
            show fuyu really with Dissolve(0.5)
            ryu "Haruki?"
            show fuyu at center 
            with moveinright
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
                    show hime cool 
                    with Dissolve(0.5)
                    him "Okay then."
                    ryu "I'll see you afterschool then!"
                    nar "Fuyuhiko shifts around in his seat uncomfortably, then hands his controller back to Ryuji."
                    fuy "Hey Hime, it's getting kinda late. Could you give me a ride home?"
                    him "Sure."
                    jump Day3
                "Fuck him.":
                    $ DeniedMeeting = False
                    $ RyujiGoing = False
                    fuy "Honestly? Fuck him."
                    show ryuji err
                    ryu "Oh."
                    fuy "You two can meet up with him if you want."
                    fuy "I'm not coming."
                    show ryuji so 
                    with Dissolve(0.5)
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
            show ryuji so 
            with Dissolve(0.5)
            ryu "If you say so..."
            hide ryuji 
            with moveoutleft
            show fuyu at left 
            with moveinright
            show hime at right 
            with moveinright
            him "Don't worry about him, he'll be over it within the hour."
            nar "Hime leads Fuyuhiko to her easel, judging by the crunching underfoot, it seems she's taken proper precautions to protect the house."
            him "Welcome to the proverbial Art Corner."
            play sound "audio/spraycan.mp3" volume 0.5
            nar "Himiko shakes up a can and begins to paint with a satisfying hiss."
            nar "Hime has always shown mastery over spray paint, Winter can tell by the controlled highs and lows of the hissing's volume."
            nar "It's nice listening, though granted, nothing can match the satisfaction of painting a wall that actually deserved it."
            nar "But despite the canvas she's painting now having done nothing wrong, Hime's painting feels angry almost."
            fuy "Wanna talk?"
            if HimeChat:
                show hime uncomfy
                with Dissolve(0.5)
                him "Well you kinda already know what happened."
                nar "Fuyuhiko nods, her manager, the tagging, she told him last night."
                fuy "But didn't you already tag the place."
                show hime cool 
                with Dissolve(0.5)
                him "Yeah, well, it wasn't enough."
                nar "The hissing grows louder, more intense for a moment."
                nar "A part of Fuyuhiko enjoys it, the sound of defiance, of the rage, of revolution."
                nar "A part of Fuyuhiko just feels bad for his friend."
                nar "Then Hime's phone starts to ring."
                him "Shit."
                play sound "audio/phone.mp3" volume 0.5
                $renpy.pause(2.0)
                him "It's Haruki."
                show fuyu really 
                with Dissolve(0.5)
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
                with Dissolve(0.5)
                nar "Ryuji is laying down on the couch, he looks up when Hime and Fuyuhiko enter."
                him "Hey dude, Haruki just called."
                him "He said we should meet up at the clubroom tomorrow."
                ryu "But we don't have club on Tuesdays?"
                show hime uncomfy 
                with Dissolve(0.5)
                him "He said he wants to talk, he sounded really freaked out."
                ryu "What do you think Winter?"
                menu:
                    "Meet up with Haruki tomorrow.":
                        $ HarukiMeeting = True
                        fuy "I guess we should meet up with him tomorrow."
                        show hime cool 
                        with Dissolve(0.5)
                        him "Okay then."
                        ryu "I'll see you afterschool then!"
                        nar "Fuyuhiko shifts on his feet uncomfortably."
                        fuy "Hey Hime, it's getting kinda late. Could you give me a ride home?"
                        him "Sure."
                        jump Day3
                    "Fuck him.":
                        $ MeetingDenied = True
                        $ RyujiGoing = False
                        fuy "Honestly? Fuck him."
                        show ryuji err
                        ryu "Oh."
                        fuy "You two can meet up with him if you want."
                        fuy "I'm not coming."
                        show ryuji so 
                        with Dissolve(0.5)
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
                show hime uncomfy 
                with Dissolve(0.5)
                him "He threatened my job yesterday Fuyuhiko. Because I wouldn't go out with him."
                him "God, I hate men."
                show hime cool 
                with Dissolve(0.5)
                him "No offense."
                nar "Fuyuhiko shrugs, what could he say?."
                show fuyu really 
                with Dissolve(0.5) 
                fuy "That's awful Hime..."
                show hime uncomfy 
                with Dissolve(0.5)
                him "I know right!?"
                show hime cool 
                with Dissolve(0.5)
                him "I'll be alright though, I just wanted to get this out of my system."
                show fuyu neut 
                with Dissolve(0.5)
                him "You seem like you wanna talk too, Fuyuhiko."
                fuy "It's nothing, I'm fine."
                nar "Hime shrugs, Fuyuhiko can tell as the paint can stops hissing for a moment to accomodate it."
                him "If you say so just know-"
                $renpy.pause(1.0)
                him "Haruki's calling."
                show fuyu really 
                with Dissolve(0.5)
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
                show ryuji hap at farright
                show fuyu really at center
                with Dissolve(0.5)
                nar "Ryuji is laying down on the couch, he looks up when Hime and Fuyuhiko enter."
                him "Hey dude, Haruki just called."
                him "He said we should meet up at the clubroom tomorrow."
                ryu "But we don't have club on Tuesdays?"
                show hime uncomfy 
                with Dissolve(0.5)
                him "He said he wants to talk, he sounded really freaked out."
                ryu "What do you think Winter?"
                menu:
                    "Meet up with Haruki tomorrow.":
                        $ HarukiMeeting = True
                        fuy "I guess we should meet up with him tomorrow."
                        show hime cool 
                        with Dissolve(0.5)
                        him "Okay then."
                        ryu "I'll see you afterschool then!"
                        nar "Fuyuhiko shifts on his feet uncomfortably."
                        fuy "Hey Hime, it's getting kinda late. Could you give me a ride home?"
                        him "Sure."
                        jump Day3
                    "Fuck him.":
                        $ DeniedMeeting = True
                        fuy "Honestly? Fuck him."
                        show ryuji err
                        ryu "Oh."
                        fuy "You two can meet up with him if you want."
                        fuy "I'm not coming."
                        show ryuji so 
                        with Dissolve(0.5)
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
    $ NoMeeting = False
    scene road day
    show fuyu really at left
    show haruki smug at right
    with Dissolve(0.5)
    nar "Fuyuhiko almost immediately regrets his decision the second he's in the car alone with Haruki."
    if HarukiChat:
        #Focus on Fuyuhiko (eventually) apologizing for blowing up at Haruki
        #He was just under a lot of stress okay?
        #But like, you can still cut it bit with the flirting
        nar "Haruki is annoying as ever, though he seems to be holding something back."
        nar "Then Fuyuhiko realizes what's wrong, Haruki hasn't called him Fuyu all day."
        nar "He doesn't long to think about it before they arrive at his apartment though."
        scene supai day
        show fuyu really at left
        show haruki smug at right
        with Dissolve(0.5)
        har "Welcome to my humble abode."
        $ renpy.pause(1.0)
        show haruki frown 
        with Dissolve(0.5)
        har "I, uh, didn't think I would get this far."
        har "I don't really know what to do."
        har "Wanna like, throw darts or something?"
        $ renpy.pause(0.5)
        fuy "I'm blind, Haruki."
        har "Oh yeah..."
        show haruki smug 
        with Dissolve(0.5)
        har "How about I just wear a blindfold! It'll be even."
        fuy "If you want us both to poke your eyes out, then sure."
        show haruki frown 
        with Dissolve(0.5)
        har "How about... No... Um, reading something...? Probably not."
        stop music fadeout 1.0
        fuy "Look if you don't wanna hang out with me, I can just go home."
        show haruki shut 
        with Dissolve(0.5)
        har "No! I uh... I just need a minute."
        fuy "I'm going home."
        har "Come on Fuyuhiko, I-"
        fuy "No, if it's such a problem for you to accomdate me then I think I should just go home."
        har "I-I'm trying here, I-"
        fuy "You shouldn't have to! Hime and Fall, they-"
        har "You never hang out with me Fuyuhiko!"
        har "I barely know the things you like! I'm not familiar with your limits."
        har "You don't tell when I do something that bothers you until you're at an exploding point!"
        har "You won't let me!"
        $ renpy.pause(1.0)
        show fuyu neut 
        with Dissolve(0.5)
        fuy "..."
        har "Look if you wanna go home, just let me drive you, alright?"
        fuy "No, I-"
        play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0 volume 0.5
        fuy "Let's just watch a movie, okay?"
        show haruki smug 
        with Dissolve(0.5)
        har "Oh, um, okay. What kind?"
        show fuyu smile 
        with Dissolve(0.5)
        fuy "Something gorey, so that you're the only one who has to see it."
        har "Hah. Okay then, come on."
        $ HarukiFriend = True
        scene black 
        with Dissolve(1.0)
        nar "Eventually, Haruki does end up driving Fuyuhiko home."
        jump Day3
    else:
        #Fuyuhiko might blow up yet
        #But have Haruki push him a bit farther
        #And try to resolve it at least a bit within the day
        har "So, Fuyu~"
        har "How're ya feeling?"
        fuy "Worse now that you're talking."
        har "Oh how you wound me so!"
        har "But I wonder, my dear, if you're okay? You seem far too uncomfortable."
        show haruki frown 
        with Dissolve(0.5)
        har "Do I need to take you home?"
        nar "Fuyuhiko shifts in his seat, wanting to give the impression that he's considering it."
        fuy "No."
        show haruki smug 
        with Dissolve(0.5) 
        har "Okay then, Fuyu."
        scene supai day
        show fuyu really at left
        show haruki smug at right
        with Dissolve(0.5)
        har "Welcome to my humble abode."
        $ renpy.pause(1.0)
        show haruki frown 
        with Dissolve(0.5)
        har "I, uh, didn't think I would get this far."
        har "I don't really know what to do."
        har "Wanna like, throw darts or something?"
        $ renpy.pause(0.5)
        fuy "I'm blind, Haruki."
        har "Oh yeah..."
        show haruki smug 
        with Dissolve(0.5)
        har "How about I just wear a blindfold! It'll be even."
        fuy "If you want us both to poke your eyes out, then sure."
        show haruki frown 
        with Dissolve(0.5)
        har "How about... No... Um, reading something...? Probably not."
        fuy "Look if you don't wanna hang out with me, I can just go home."
        show haruki shut 
        with Dissolve(0.5)
        har "No! I uh... I just need a minute."
        fuy "I'm going home."
        har "Come on Fuyu, I-"
        fuy "No, if it's such a problem for you to accomdate me then I think I should just go home."
        har "I-I'm trying here, I-"
        fuy "You shouldn't have to! Hime and Fall, they-"
        har "You never hang out with me Fuyuhiko!"
        har "I barely know the things you like! I'm not familiar with your limits."
        har "You won't let me!"
        $ renpy.pause(1.0)
        show fuyu neut 
        with Dissolve(0.5)
        fuy "..."
        har "Look if you wanna go home, just let me drive you, alright?"
        fuy "No, I-"
        fuy "Let's just watch a movie, okay?"
        show haruki smug 
        with Dissolve(0.5)
        har "Oh, um, okay. What kind?"
        show fuyu smile 
        with Dissolve(0.5)
        fuy "Something gorey, so that you're the only one who has to see it."
        har "Hah. Okay then, come on."
        $ HarukiFriend = True
        scene black 
        with Dissolve(1)
        nar "Eventually, Haruki does end up driving Fuyuhiko home."
        jump Day3
#Spacer

label ReiHouse:
    $ ReiHouse = True
    stop music fadeout 1.0
    play music "audio/KinetikLee-MidnightMirrors.mp3" fadein 1.0 fadeout 1.0 volume 0.5
    #Rei means to show Fuyuhiko the glory of Lantern
    #But Haruki suspects something is up, he's watching
    #And Rei /will/ get possessed after all
    scene road day
    with Dissolve(0.5)
    #consider changing to night for mood, even if it doesn't make total sense chronologically
    show rei cautious at right
    show fuyu neut at left
    with Dissolve(0.5)
    nar "Rei is quiet the whole drive to his house."
    nar "There's a weird sort of air around him, nervous and detirmination bundled up together."
    nar "Fuyuhiko doesn't say anything though."
    scene amanshi day
    show rei cautious at right
    show fuyu neut at left
    with Dissolve(0.5)
    #^^, need asset
    nar "Not until they're there."
    rei "This is it."
    rei "I just need a minute."
    rei "To get ready..."
    hide rei 
    with moveoutright
    nar "With Rei gone, Fuyuhiko sighs and takes out his cane."
    nar "He walks around the house, mentally mapping where the furniture is in order to try and avoid tripping later on."
    nar "But there's one thing he can't place."
    nar "A small rectangular box, too hard to be a footrest, but too small to be a coffee table."
    nar "It seems centerally placed, so it doesn't seem to be a nightstand either."
    show rei cautious at right 
    with moveinright
    nar "Fuyuhiko jumps up when Rei re-enters."
    rei "Okay then, let's get started. I just need you to witness this."
    hide fuyu
    with Dissolve(0.5)
    show rei at center 
    with moveinright
    nar "Rei guides Fuyuhiko to sit at the strange box, as he sits down on the other side. He takes a deep breath before he begins a chant."
    rei "{i}Inter nos in nobis.{/i}"
    rei "{i}Per flammam et lucem.{/i}"
    show rei posesso 
    with Dissolve(0.5)
    rei "{i}Te ipsum rev-!{/i}"
    #The finished chant is "Te ipsum revelare!", "Among us, among us. By flame and light. Reveal thyself!"
    stop music
    har "Stop it!"
    show rei paradox 
    with Dissolve(0.5)
    rei "What?"
    show haruki shut at farright 
    with moveinright
    show fuyu really at farleft 
    with moveinleft
    har "I said stop it."
    show rei shatter 
    with Dissolve(0.5)
    rei "{i}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARRRGH!!!{/i}" with hpunch
    rei "How do you ruin EVERYTHING!?"
    rei "How did you even GET here!?"
    rei "Did you follow me to my fucking house, Haruki!?"
    show haruki smug 
    with Dissolve(0.5)
    har "Well, yeah, but-"
    rei "Get the fuck out!"
    har "What about-"
    rei "OUT!"
    hide rei 
    with Dissolve(0.5)
    hide haruki 
    with Dissolve(0.5)
    nar "Rei shoves Haruki out his front door and slams it in his face."
    show rei distracted at right 
    with Dissolve(0.5)
    show fuyu at left 
    with moveinleft
    play music "audio/Urban-Flight.mp3" fadein 1.0 fadeout 1.0 volume 0.5
    rei "I can't believe him..."
    rei "This night is over. Let me drive you home Shiro..."
    jump Day3
#Spacer

label HomeAlone:
    $ HomeAlone = True
    if WorkChat:
        scene apartment afternoon
        show fuyu really
        with Dissolve(0.5)
        nar "Fuyuhiko throws his bag onto his couch, and starts to pace around his room."
        fuy "What gives them the right!"
        show fuyu snap
        with Dissolve(0.5)
        stop music
        fuy "WHAT GIVES THEM THE DAMN RIGHT!" 
        with hpunch
        show fuyu really
        with Dissolve(0.5)
        fuy "I can't stop thinking about it."
        fuy "The babying, the control, the lack of fucking faith."
        fuy "I am valuable! I am!"
        fuy "I could do my job if you just gave me the actual damn tools to do it! Ugh!"
        hide fuyu
        with moveoutright
        nar "Fuyuhiko goes into the bathroom. He throws water into his face until he feels a little calmer."
        show fuyu
        with moveinright
        play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0 volume 0.5
        fuy "I need to lie down..."
        nar "And soon enough, he begins to drift off into sleep..."
        jump Day3
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
    nar "End of Day 2."
    nar "Start of Day 3."
    scene apartment day
    with Dissolve(0.5)
    nar "Fuyuhiko felt awful the next morning."
    if HarukiMeeting:
        nar "The meeting he agreed to go to earlier wasn't helping any."
    if ReiHouse or HomeAlone:
        play sound "audio/phone.mp3" volume 0.5
        nar "Especially not with his phone going off."
        nar "Especially not with with a text from him."
        show fuyu really at farleft
        with moveinright
        show haruki smug at farright
        with Dissolve(0.5)
        if ReiHouse:
            thar "I need to talk to you about last night."
        else:
            thar "I need to talk to you."
        $ renpy.pause(1.5)
        show haruki shut
        with Dissolve(0.5)
        if HarukiChat:
            thar "C'mon Fuyuhiko, it's important."
        else:
            thar "C'mon Fuyu it's important."
        $ renpy.pause (1.0)
        thar "Fine just, come to club tonight okay?"
        thar "I really need to talk with you and the others."
        menu:
            "Fine.":
                tfuy "Fine."
                show haruki smug
                with Dissolve(0.5)
                thar "Great."
                $ HarukiMeeting = True
                show fuyu down at center
                with moveinleft
                hide haruki frown
                with Dissolve(0.5)
            "Don't Respond.":
                $ DeniedMeeting = True
                nar "Fuyuhiko just mutes his phone."
                nar "He can't deal with this right now. He can't deal with {i}him{/i} right now."
                nar "He needs to get ready."
                show fuyu down at center
                with moveinleft
                hide haruki frown
                with Dissolve(0.5)
    nar "The boy manages to get himself to brush his teeth, shower, put on his clothes. All the horrible necessities."
    scene hallway day
    with Dissolve(0.5)
    nar "He drags himself to class."
    if HarukiMeeting:
        jump HarukiMeeting
    nar "Then decides to talk with... someone. What a rarity."
    nar "He should text..."
    menu:
        "Hime":
            if NoMeeting:
                jump HimeCheck
            else:
                nar "Fuyuhiko goes to text Hime when he suddenly recieves a call from Ryuji."
                play sound "audio/phone.mp3" volume 0.5
                jump KonpekiMeeting
        "Ryuji":
            if NoMeeting:
                jump RyujiCheck
            else:
                nar "Fuyuhiko goes to text Ryuji when he suddenly recieves a call from him."
                play sound "audio/phone.mp3" volume 0.5
                jump KonpekiMeeting
        "Haruki":
            if NoMeeting:
                jump HarukiCheck
            else:
                nar "Fuyuhiko goes to text Haruki, but he rememebers..."
                nar "If he texts Haruki right now, he's going to try to pressure him to meet with him."
                nar "Not wanting that he decides to just stay home."
                jump AloneForever
        "Rei":
            if NoMeeting:
                jump ReiCheck
            else:
                jump ReiMeeting
        "Nobody":
            jump AloneForever
#Spacer

#Checks are NoMeeting, Meetings are MeetingDenied (or HarukiMeeting)
label HimeCheck:
    show fuyu neut at farleft
    with moveinright
    tfuy "Hey Hime."
    show ryuji ugh at farright
    with Dissolve(0.5)
    thim "Hey Fuyuhiko."
    show ryuji uncomfy
    with Dissolve(0.5)
    thim "My boss is being a dick again."
    show ryuji ugh
    with Dissolve(0.5)
    extend "More than normal."
    show fuyu really
    with Dissolve(0.5)
    tfuy "What did he do now?"
    thim "Nothing in particular, it's that kind of shitty."
    thim "It's just giving me work, getting on me more often, threatening to write me up for the littlest things."
    show fuyu down
    with Dissolve(0.5)
    tfuy "That sucks."
    thim "Yeah..."
    show hime cool
    with Dissolve(0.5)
    extend "But hey, don't you usually have work when I do on Tuesdays? How's your job?"
    play sound "audio/phone.mp3" volume 0.5
    nar "Fuyuhiko's alarm goes off."
    tfuy "Shit."
    show hime yo
    with Dissolve(0.5)
    thim "Awesome, see you later Fuyuhiko."
    tfuy "You too Hime."
    jump WorkTime
#Spacer

label RyujiCheck:
    show fuyu neut at farleft
    with moveinright
    tfuy "Hey Ryuji."
    show ryuji hap at farright
    with Dissolve(0.5)
    tryu "hey winter!"
    tryu "do you wanna come over?"
    show fuyu what
    with Dissolve(0.5)
    tfuy "What?"
    tryu "oh! i just thought you wanted to study"
    tryu "we have a math exam coming up, y'know"
    tfuy "What!"
    tryu "don't tell me you didn't remember!"
    tryu "just think, i'm being more responsible than you right now!"
    tryu "speaking of, don't you usually have work around now?"
    play sound "audio/phone.mp3" volume 0.5
    nar "Fuyuhiko's alarm goes off."
    tfuy "I do..."
    tryu "well, ttyl! we should study together!"
    jump WorkTime
#Spacer

label HarukiCheck:
    show fuyu neut at farleft
    with moveinright
    tfuy "Hey Haruki."
    show haruki smug at farright
    thar "Hey Fuyu!"
    show fuyu really
    with Dissolve(0.5)
    tfuy "Don't. Start."
    thar "Okay, okay."
    thar "Hey I was meaning to talk to you about something, alright?"
    show fuyu neut
    with Dissolve(0.5)
    tfuy "Alright."
    show haruki frown
    with Dissolve(0.5)
    thar "I'm sorry for a being a shitty host, last night."
    tfuy "Oh."
    show fuyu down
    with Dissolve(0.5)
    extend "No, I'm sorry for being a shitty guest."
    show haruki smug
    with Dissolve(0.5)
    thar "I think we both could take each other into account more often, huh."
    show fuyu neut
    with Dissolve(0.5)
    tfuy "Yeah, I think we could."
    play sound "audio/phone.mp3" volume 0.5
    nar "Fuyuhiko's alarm goes off, it's time for his shift."
    tfuy "I need to go. I'll see you later Haruki."
    jump WorkTime
#Spacer

label ReiCheck:
    show fuyu neut at farleft
    with moveinright
    tfuy "Hey Rei."
    show rei posesso at farright
    $renpy.pause(0.1)
    show rei happy
    trei "Hello Fuyuhiko. Would you like to come over?"
    show fuyu what
    with Dissolve(0.5)
    tfuy "No, I have my shift soon."
    if ReiHouse:
        tfuy "Besides it didn't that well last time."
    trei "Come after your shift."
    trei "Or anytime really, you're always welcome."
    trei "But preferably after your shift."
    tfuy "Okay, fine."
    trei "Good."
    hide rei
    with Dissovle(0.5)
    show fuyu what at center
    with moveinleft
    fuy "That was weird, Rei never calls me-"
    play sound "audio/phone.mp3" volume 0.5
    nar "Fuyuhiko's alarm goes off."
    fuy "Shit."
    jump WorkTime
#Spacer

label AloneForever:
    show fuyu really
    nar "Fuyuhiko lies alone in his bed, dreading the moment he has to go to work."
    nar "The moment he had to face being treated as useless, again."
    nar "He tosses himself around-"
    fuy "It's so awful!"
    fuy "I can do everything right, and they still treat me like I can't take care of myself!"
    fuy "Like I can't do my fucking job! Like I'm a fucking child!"
    fuy "It's humiliating..."
    fuy "I'm an adult! I don't need a damn babysitter watching my every move, I just need a damn screenreader!"
    extend "I-"
    extend "Ugh!" with hpunch
    fuy "This is awful..."
    play sound "audio/phone.mp3" volume 0.5
    nar "Fuyuhiko's alarm goes off."
    nar "He breathes a long sigh, and snaps up."
    nar "It's time to work."
    jump WorkTime
#Spacer

label KonpekiMeeting:
    show fuyu neut at farleft
    with moveinright
    show ryuji hap at farright
    with Dissolve(0.5)
    tryu "Hey Winter!"
    if KonpekiHouse:
        tfuy "I thought you were going to Haruki's meeting."
        tryu "Oh, Hime is!"
        show hime cool at right
        with Dissolve(0.5)
        thim "Hey Fuyuhiko!"
        hide hime
        with Dissolve(0.5)
        tryu "But she's getting ready to leave, which is why I called you!"
        tryu "Have you studied for our math test at all?"
        show fuyu what
        with Dissolve(0.5)
        tfuy "Our what?"
        tryu "You really don't remember!?"
        tryu "In our math class, we have a test coming up, the professor was really adamant about it."
        tfuy "I..."
        extend "No."
        show ryuji excited
        with Dissolve(0.5)
        tryu "Then we need to study!"
        show fuyu neut
        with Dissolve(0.5)
        play sound "audio/phone.mp3" volume 0.5
        nar "Fuyuhiko's alarm goes off."
        tfuy "Sorry Ryuji, but I need to go."
        show ryuji so
        with Dissolve(0.5)
        tryu "Awww."
        tfuy "Bye."
        hide ryuji
        with Dissovle(0.5)
        show fuyu at center
        with moveinleft
        nar "Fuyuhiko quickly ends the call."
        nar "He has a job to get to, unfortunately."
        jump WorkTime
    else:
        tryu "Haruki said to tell you about this meeting at-"
        tfuy "I already know."
        tryu "Oh- Well are you gonna go?"
        tfuy "No."
        tryu "Aw really? Me and Hime are getting ready to go right now!"
        tfuy "I'm not putting up with him any longer than I have to."
        show ryuji so
        with Dissolve(0.5)
        tryu "If you say so..."
        show ryuji hap
        with Dissolve(0.5)
        tryu "Just, uh, try to study for our math test while I'm gone!"
        show fuyu what
        with Dissolve(0.5)
        tfuy "Wait, what-"
        play sound "audio/phone.mp3" volume 0.5
        nar "Fuyuhiko's alarm goes off."
        tfuy "Ugh, I have to go."
        tfuy "Bye, Ryuji."
        tryu "Oh, okay, bye Winter!"
        hide ryuji
        with Dissovle(0.5)
        show fuyu at center
        with moveinleft
        nar "Fuyuhiko quickly ends the call."
        nar "He has a job to get to, unfortunately."
        jump WorkTime
#Spacer

label ReiMeeting:
    show fuyu neut at farleft
    with moveinright
    tfuy "Hey Rei."
    show rei disappoint at farright
    with Dissolve(0.5)
    trei "Hello Shiro."
    if ReiHouse:
        trei "Hey, I'm sorry about last night."
        trei "That was a mess but there's bigger problems now."
    trei "I just recieved a vision from Lantern."
    show fuyu what
    with Dissolve(0.5)
    tfuy "A vision?"
    trei "Yes, that Haruki is hosting a club meeting behind my back, with the others."
    trei "Do you know about this?"
    menu:
        "Yes. {i}(Support Him){/i}":
            tfuy "Yeah, Haruki asked me to go."
            show rei cautious
            show fuyu neut
            with Dissolve(0.5)
            trei "I suspected as much."
            trei "I'm planning to confront him."
            show rei disappoint
            trei "Would you come with me?"
            nar "Fuyuhiko breathes a heavy sigh, all this to end up showing up to this stupid meeting anyway."
            tfuy "Sure."
            jump CrashMeeting
        "No. {i}(Distract Him){/i}":
            show fuyu frown
            with Dissolve(0.5)
            nar "This is bad, whatever Haruki is doing, it's going to hurt everyone if Rei blows up because of it."
            nar "He needs a distraction, quick."
            if ReiChat:
                tfuy "Remember when you said you ask Lantern what happened to me earlier this week?"
            tfuy "Use your powers to look into my secrets, now."
            show rei cautious
            with Dissolve(0.5)
            trei "What?"
            tfuy "Just do it, Rei. Prove to me that you can."
            trei "I don't understand."
            extend "But, okay."
            play sound "audio/phone.mp3" volume 0.5
            trei "We need to video call."
            nar "Fuyuhiko sighs and accepts the call."
            trei "Okay, just, try to remain calm while I do this okay?"
            tfuy "Yeah, of course."
            scene black
            with Dissolve(0.5)
            stop music fadeout 10.0
            nar "Fuyuhiko takes a deep breath as Rei starts to chant something."
            hide rei
            with Dissolve(0.5)
            show fuyu at center
            with moveinleft
            nar "He can't understand it though, and it's almost... distant."
            nar "Then something begins to stir inside him, this awful all-consuming dread."
            nar "He feels lik he's choking, he's almost convinced he is when he sees it."
            fuy "Blanc..."
            nar "His cat."
            extend "In front of him."
            extend "Dead."
            extend "You caused this."
            extend "You did this."
            extend "Why?" with hpunch
            extend "You MONSTER!!" with hpunch
            #SFX?
            nar "Fuyuhiko screams."
            show rei paradox
            $ renpy.pause(0.1)
            show rei cautious at farright
            scene classroom evening
            nar "His senses fade back in quickly after that."
            nar "But he's in a different place, and there are hands on him?"
            nar "He tries to shove them off, to get away-"
            rei "Fuyu, stop!"
            show rei disappoint
            with Dissolve(0.5)
            rei "You're fine now..."
            nar "Rei is... actually here."
            rei "Look you're probably pretty out of it."
            rei "Let's just go to my house, okay?"
            nar "Fuyuhiko nods weakly as Rei helps him up from the corner he finds himself sitting in."
            nar "But he can't stop thinking about what he saw."
            jump ReiRitual
#Spacer

label HarukiMeeting:
    scene classroom evening
    with Dissolve(0.5)
    nar "Then to the club room."
    show haruki shut at farleft
    show hime ugh at center
    show ryuji so at farright
    show fuyu really at right
    with Dissolve(0.5)
    har "I'm telling you I know what I saw!"
    har "Rei was at this altar and green fire started sprouting all around him."
    har "He was summoning some weird demon thing with his powers!"
    if ReiHouse:
        har "You were {i}there{/i} Fuyuhiko!"
    him "Haruki, I just think that we should wait a little longer until we do anything."
    extend "Maybe until someone else-"
    har "Are you calling me crazy!?"
    ryu "She didn't say that!"
    har "Why don't you believe me, I-!"
    #Door Crash SFX
    nar "The clubroom door swings open." with hpunch
    hide hime
    show rei shatter at center
    with Dissolve(0.5)
    nar "And Rei shows up."
    show rei at left
    with moveinright
    show hime uncomfy at center
    with Dissolve(0.5)
    nar "And he goes right for Haruki."
    rei "What are you doing!?"
    har "Rei! Buddy! Heyyyy..."
    rei "Calling a meeting behind my back, after {i}breaking in to my HOUSE!?{/i}"
    rei "What is wrong with you!?"
    nar "Fuyuhiko's phone alarm starts to sound, only to be quickly silenced."
    nar "It's too late though, Rei's attention turns."
    rei "And you three! Why did you agree to meet him!?"
    ryu "We didn't know you wouldn't be here!"
    rei "Ugh! That's it! I'm done with all of you!"
    rei "I can't believe this."
    hide rei
    with moveoutright
    har "Well... That ju-"
    show hime fuck
    with Dissolve(0.5)
    him "Don't."
    him "I'm going home, you want a ride Fuyuhiko?"
    nar "Fuyuhiko checks his phone, reading out the time."
    fuy "I'm good."
    him "Okay then."
    nar "Hime grabs Ryuji's arm and pratically drags him out of the clubroom."
    hide hime
    hide ryuji
    with moveoutright
    har "Fuyuhiko-"
    fuy "I have to go."
    show haruki frown
    with Dissolve(0.5)
    har "But-"
    fuy "Bye, Haruki."
    jump WorkTimeLate
#Spacer

label CrashMeeting:
    nar "Fuyuhiko meets Rei in the hallways. He never had a a chance to leave the school anyway."
    nar "They stand outside the clubroom doors for a second, but when Rei nods..."
    scene classroom evening
    show fuyu really at farright
    show rei shatter at right
    show haruki shut at farleft
    show hime uncomfy at left
    with Dissolve(0.5)
    if RyujiGoing:
        show ryuji err at center
        with Dissolve(0.5)
    nar "You both go in."
    nar "And Rei goes right for Haruki."
    rei "What are you doing!?"
    har "Rei! Buddy! Heyyyy..."
    rei "Calling a meeting behind my back, after {i}breaking in to my HOUSE!?{/i}"
    rei "What is wrong with you!?"
    nar "Fuyuhiko's phone alarm starts to sound, only to be quickly silenced."
    nar "It's too late though, Rei's attention turns, he prompts Fuyuhiko to speak."
    fuy "Rei's right! Why did you call the rest of us but not him Haruki!?"
    har "Look, I just- I... I..."
    rei "I can't believe you."
    rei "I'm going home."
    hide rei
    with moveoutright
    nar "Fuyuhiko goes to follow, and he checks his phone, prompting it to read the time."
    nar "Oh shit. He has to go. Now."
    jump WorkTimeLate
#Spacer

label WorkTime:
    #Fuyuhiko is at his job, he think it kinda sucks, no actual accomodations just help from his coworkers
    #(Where they're basically just doing his job for him). Near the end of his shift Ryuji and Hime show up.
    #Fuyuhiko is grumpy about it. Rei corners after his shift (ReiMeeting cannot have occured), path to
    #Day4 or ReiRitual
#Spacer

label WorkTimeLate:
    scene road day
    nar "Fuyuhiko was late to work."
    nar "Luckily the coffee shop isn't far from work, it's a pretty short walk."
    nar "But he's still late, god, and he's heard people get chewed out for less."
    scene coffee shop
    show fuyu frown at center
    with Dissolve(0.5)
    nar "But when Fuyuhiko finally gets there, no one seems to notice?"
    show fuyu really
    with Dissolve(0.5)
    show fuyu at farleft
    with moveinleft
    fuy "Which is cool because fuck this job but like..."
    show fuyu at farright
    with moveinright
    fuy "Doesn't exactly make me feel any less worthless."
    show fuyu at center
    with moveinleft
    fuy "Everything about this makes me feel useless."
    fuy "The micromanagement, the underestimation, the explaining my damn disability {i}all{/i} the time."
    fuy "It's awful."
    scene black
    with Dissolve(0.5)
    fuy "I'm just glad when my shift is over."
    jump Day4
#Spacer

label ReiRitual:
    #Lantern's power and control only grows. Rei gets hard-possessed and attacks Fuyuhiko, he escapes though.
    #Wary transition to Day4
#Spacer



label Day4:
    #Placeholder
#Spacer