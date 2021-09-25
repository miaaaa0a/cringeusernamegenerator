import json
import random 
import tkinter as tk 

prefixes = json.loads(open("prefixes.json").read())
suffixes = json.loads(open("suffixes.json").read())
conjugations = json.loads(open("conjugations.json").read()) # eg Xx_ and _xX, prefix and suffix will get ignored if there is a conjugation selected
midWords = json.loads(open("midwords.json").read())
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