import json
import random 
import tkinter as tk 

prefixes = json.loads(open("prefixes.json").read())
suffixes = json.loads(open("suffixes.json").read())
conjugations = json.loads(open("conjugations.json").read()) # eg Xx_ and _xX, prefix and suffix will get ignored if there is a conjugation selected
midWords = json.loads(open("midwords.json").read())

#print([prefixes,suffixes,conjugations,midWords]) # ok

# just come up with stuff to add now
# kkk
# roux why
# why what
# why did oyiu jotypr kkk  :£=3]] uwu

# 0 = use prefix/suffix, 1 = use conjugations
#istg you put some useless stuff in the code but it looks way better like that
# the bool function
# wtf did i add that isnt necessary
# uselss this ratio
# nah its good imo
# looks a bit better too liek u said

# readable as some may say
# true..

# ratio
# Dicks are so cute omg(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ when you hold one in your hand and it starts twitching its like its nuzzling you(/ω＼) or when they perk up and look at you like" owo nya? :3” hehe ~ penis-kun is happy to see me!!（＾ワ＾） and the most adorable thing ever is when sperm-sama comes out but theyre rlly shy so u have to work hard!!(๑•̀ㅁ•́๑)✧ but when penis-kun and sperm-sama meet and theyre blushing and all like "uwaaa~!" (ﾉ´ヮ´)ﾉ: ･ﾟhehehe~penis-kun is so adorable (●´Д｀●)・
# ok im not giving ratings this time (like 82882/10 etc) instead im going to address come criticism!! yay!!! but instead of various points im just going to address a problem. and thats the amount of ppl who either dislike/blame/ put pressure on mememan. now before you be like oohh thats MY opinion i can say what i want like im not saying you cant hate mememan or anything im just focusing on the bad side lmao. now why does mememan get so much hate? oh, he does his job!!!, oh hes too strict, oh he watches the chat all the time!!, oh hes a stalker yea this is just total bs. first of all mememan doesnt have a life /h- i mean hes an admin. what do you expect? and before you pull up with the ooooooh admins arent supposed to be active and watch the chat all the time i just want to say that hes a fucking admin like what is he supposed to do? hang around in #reports like brain used to do? (not being rude) its annoying hearing ppl say oooh mememan butts in all the time when we're talking/rping! well i mean most of the ppl here tend to say some really weird stuff (like malk and the isaac p word thing) like what youre just gonna do some weird shit and expect no one to do anything like what? and some ppl say ooooh mememan is strict with rules oh no!!! i just wanna have fun?!!!1 well before you act all annoyed over that i just want to say that mememan does not make the rules here. its abu and fourtle. like man you blaming an admin for warning you over small shit like i dont know just because hes an admin doesnt mean hes the fucking owner and shit. so in conclusion if you hate mememan its fine. i can agree he can be a little annoying sometimes. but damn no need to be a dumbass and put shit like oooooh mememan bad in your name and idc if its a joke its still fucking stupid
# https://media.discordapp.net/attachments/873733700762865674/887000815263449128/image0.png?width=322&height=270
window = tk.Tk()


def generate() -> None:
    usernameTextBox.delete(0,100)
    if bool(random.randint(0,1)) == False:
        #print('pre/suf')
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        midWord = random.choice(midWords)

        usernameTextBox.insert(0,f"{prefix}{midWord}{suffix}") 
    else:
        #print('conjugation')
        conjugation = random.choice(conjugations)
        prefix = conjugation[0]
        suffix = conjugation[1]
        midWord = random.choice(midWords)

        usernameTextBox.insert(0,f"{prefix}{midWord}{suffix}")


usernameTextBox = tk.Entry(width=50)
generateButton = tk.Button(text="generate",command=generate)

usernameTextBox.pack()
generateButton.pack()


window.mainloop()