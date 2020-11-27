#!/bin/env python3
import csv
import random
def replaceWords():
    replacement_dictionary = {
        "failed":['broken my system','fucked up linux','borked my machine'],
        "battles":['Linux system','Fight about Inits','Emacs vs Vim'],
        "medals":['glories','stars','pull requests'],
        "test":['unit tests','testing scripts','test cases'],
        "fail":['failed at compiling','break','berakdown'],
        "machine":['linux system machine','linux based machine','linux based'],
        "airplane":['linux kernel','linux sysfs','linux procfs'],
        "you":['user','programmer','hacker'],
        "your":['user\'s','programmer\'s','hacker\'s'],
        "reading":['inspecting','read operation','read action'],
        "writing":['Saving to disk','Saving to ram','accessing from ram'],
        "door":['back door','vulnerability','bug'],
        "passion":['love for linux','hacking','coding'],
        "devoid":['without','nullified','messed'],
        "nothing":['null','void','/dev/null'],
        "impossible!":['tiny kernel','bloat free','null zero'],
        "possible":['bloated','heavy','could happen'],
        "that":['system','server','machine'],
        "if":['conditional','switch case','possibility'],
        "person":['expert','deccent user','hacker'],
        "someone":['X','/dev/xyz device','some user'],
        "children":['Process child\'s','process','thread'],
        "everything":['world repository','system repostory','git world repo'],
        "learned":['pro','stallman','original hackers'],
        "disappointed":['systemd','init','X server'],
        "always":['Infinite times','Forever','Never Ending'],
        "life":['linux','linux system','kernel'],
        "dream":['hack','mess with it','fuck it'],
        "work":['hack','code','rice'],
        "roads":['source code','compilers','roads'],
        "traveled":['played with','hacked on','traveled'],
        "decision":['distro to choose','kernel','bsd'],
        "capitalism":['kernel','linux','FOSS development'],
        "happens":['breaks','creates','crashes'],
        "plant":['choose a distro','read code','plant'],
        "unexamined":['life without','life without ','Arch based'],
        "success":['rice','source code','code readability'],
        "Winning":['Kernel Hack','Using Linux','FOSS development'],
        "win":['successful compilaton',"gentoo","LFS"],
        "child":['n00b','newbie','begginer'],
        "ocean":['source code','binary file',"ocean of code"],
        "cross":['read','hack','play with'],
        "day":['code','binary','assembly'],
        "forget":['distro hop','use systemd','sysvinit'],
        "born":['given for free','you have stolen','linux user'],
        "revenge":['virus','bug','hack'],
        "motivation":['desire to gentoo','using arch linux','loving FOSS'],
        "nothing":['coding','playing','hacking'],
        "criticism":['bug','hack','malware'],
        "confidently":['with bugs','life with coke','coffee']
    }
    tags = ['Distro Hopper','Kernel hacker','FOSS lover','Gentoo user (I burnt my weewee compiling kernel)','Arch (I use arch btw)','LFS hacker (I have no need for package manager)','Gnome Developer (We break freely)','Debian Maintainer (README is for noobs)','Debian Maintainer (We hate systemd)','Systemd lover (I am the best, your opinion is shit)']
    
    
    with open('quotes.csv', 'r') as quotes:
        reader = csv.reader(quotes)
        quote = random.choice(list(reader))
        words = quote[0].split(" ")
        words = [word.lower() for word in words]
        flag = False
        for word in words:
            if word in replacement_dictionary.keys():
                flag = True
                modified_words = [replacement_dictionary[word][random.randint(0,2)] if x == word else x for x in words]
                author = quote[1] + " "
                author += random.choice(tags)
            if not flag:
                author = quote[1]
                modified_words = words
        keyquote = " ".join(modified_words).capitalize()
        keyauthor = author
        string_output = keyquote + "\n --" + keyauthor
        return string_output


