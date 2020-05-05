
# Authors: Stephanie Marsh & Josey VanOrsdale
# Due Date: May 4th, 2020
# File name: cyoa.py
# Input: user input
# Output: text based game
# Purpose: Allows user to play a text based game in terminal

# first define node class for plot points
class Node:
   def __init__(self,somedata):
       self.data = somedata
   def __repr__(self):
       return str(self.data)

# chunker's purpose is to break up the text so that it is easier to read on the screen
def chunker():
    print('\n\n\n\n')

 # define the fight mechanic part of the game
def combat():
    import random
    #random is for damage
    import time
    #time is for waiting
    #each sleep's purpose is to pause, so that the user can read the damage amounts/totals
    count = 0
    player_damage = []
    NPC_damage = []
    while count != 5:
        player_damage.append(random.randrange(1,6))
        print("you took " + str(player_damage[-1]) + " damage")
        NPC_damage.append(random.randrange(1,6))
        time.sleep(1)
        print("you dealt " + str(NPC_damage[-1]) + " damage")
        time.sleep(1)
        print("you've dealt a total of " + str(sum(NPC_damage)) + " damage. you've taken a total of " + str(sum(player_damage)) + ' damage')
        count += 1
        time.sleep(2)

    if sum(player_damage) > sum(NPC_damage):
        return "You lose :("
    else:
        return "You win! :)"
        #yes, you win on a tie

# next section [lines 48 - 425] are all of the possible nodes in our game        
root = Node(
       "Welcome to The Choose Your Own Adventure Game! \n"
       "You will be put into various situations based on your choices. \n"
       "To make a choice, choose one of the prompted letter, W or S, and press enter. \n"
       "But, be wary! Your choices _do_ have consequences. \n"
       "Have fun! \n"
       "\n"
       "---------------------------------------------------------\n"
       "During the quarantine you got very bored and decided to go on a walk in the Off-Limits Forest. \n"
       "As you are walking, you are approached by a Wizard. \n"
       "He gets a little within 5 feet away from you, and you are instantly annoyed. \n"
       "\n"
       "Do you: \n"
       "Talk to him anyways [W] or \n"
       "Walk away [S] ?"
)

A = Node(
   "He introduces himself as Professor Grumbledore.  \n"
   "He explains that he is the dean of the local wizarding school, \n"
   "and asks if you are up for a challenge. \n"
   "\n"
   "Do you: \n" 
   "Accept the challenge [W] or \n"
   "Reject the challenge [S]?"
   )
 
AB = Node(
   "Professor Grumbledore is very enthusiastic and gives you a riddle to solve: \n"
   "I speak without a mouth and hear without ears. \n"
   "I have no body, but come alive with wind. \n"
   "What am I? \n"
   "\n"
   "Do you: \n"
   "Answer, 'An echo' [W] or \n"
   "Answer, 'A tree spirit' [S]"
)
 
AC = Node(
   'Grumbledore angrily grumbles at you “You are wasting my time, and frankly, your talent.” \n'
   "He storms off, and you are alone in the forest again. \n"
   "You wake up from what was apparently a dream with a migraine and feeling lonelier than ever. \n"
   'Oh no!? Do you have the Corona?'
)
 
AAB = Node(
   "“Congratulations!” The wizard exclaims jumping up and down. \n"
   "He hands you a magical map, something called a “Mulder Map” \n"
   "and says he will meet you on the other side, at your new school! \n"
   "He then disappears. \n"
   "\n"
   "Do you: \n"
   "Head towards the school [W] or \n"
   "Try to figure out where he went [S]?"
)
 
AAC = Node(
   "Grumbledore angrily grumbles at you, “You are a fool not to be trifled with! \n"
   "Everyone knows tree spirits have mouths! HUMPH! \n"
   "How dare you have wasted my precious time!” * grumble grumble grumble * \n"
   "\n"
   "Do you: \n"
   "Walk away [W] or \n"
   "Challenge Grumbledore again [S]?"
)
 
AAAB = Node(
   "You look at the map, and see you have far to journey. \n"
   "\n"
   "Do you: continue on? \n" 
   "No way! [W] \n"
   "Yes! [S]"
)
 
AAAC = Node(
"You have more questions for Grumbledore, and want to figure out where he went. \n"
"\n"
"Do you: \n"
"Look around your surroundings [W] \n"
"Check the map for clues [S]"
)
 
AAAD = Node(
   "As you wander through the forest, you come across a knight. \n"
   "He introduces himself as Sir Ruis Black.  \n"
   "He takes your presence as a very personal affront \n"
   "[who said you could be this close to him!?], and challenges you to a duel."
)
 
AAAE = Node(
   "Grumbledore stares at you with disbelief 'I told you to leave imbecile!', \n" 
   "but you ask for a thumb war instead. \n"
   "Grumbledore happens to be rather fond of thumb wars, and so he grumbly agrees."
)
 
A4B = Node(
   "You decide that this is far too much to undertake, especially for a grumbling mean old man. \n"
   "Do do not wish to continue on this journey. \n"
   "Instead, you peacefully amble through the forest until you come across a lake, \n"
   "and wake up, coughing, with the taste of saltwater in your mouth."
)
 
A4C = Node(
   "You square your shoulders, and decide that this is worth the effort. \n"
   "[of course it is: it's Hogwarts, errrr, I mean a totally different magic school] \n"
   "You journey far, and are extremely exhausted. \n" 
   "You eventually get to the spot on the map that Grumbledore marked, \n"
   "and you look up to see a huge beautiful castle.  \n"
   "\n"
   "Do you: \n"
   "Explore the grounds [W] or \n"
   "Head inside [S]?"
)
  
A4D = Node(
   "You think to yourself: 'wait this doesn’t make sense. How could a person just disappear? \n"
   "How did I get here, anyway?' \n"
   "You become self aware that you are in a dream, and wake up. \n"
   "Before you are fully awake you hear a groggy voice grumbling and then saying not to overthink things so much."
)
 
A4E = Node(
"You see on the map, he has marked a cabin to the south. \n" 
"It is not quite on the way, but looks promising.  \n"
"\n"
"Do you: \n"
"Follow towards the cabin [W] or \n"
"Decide that you’re better off meeting him at the school [S]?"
)
 
A4F = Node(
   "The knight sheaths his sword and says, “You don’t give up easy! \n"
   "I am impressed with your grit. Very well shall tell you why I am out here. \n"
   "I have been sent by my queen, Queen Mab to Open the Cave of Smaug. \n"
   "But I will never tell you where it is. Leave this forest you fool!” \n"
   "You wander home, a bit sad at the rejection [you tried your best!], \n"
   "but your life is forever changed since you now know magic is real."
)
 
A4G = Node(
   "The knight sheaths his sword and says “Finally, a worthy opponent. Impressive! Very well. \n"
   "I shall tell you why I am out here. I have been sent by my queen, Queen Mab, to Open the Cave of Smaug. \n"
   "If you come with me, I shall reveal the cave to you. \n"
   "\n"
   "Do you: \n"
   "Accept the invitation [W] or \n"
   "Reject the invitation [S] ?"
 
)
 
A4H = Node(
   "Grumbledore grumbles at you for wasting his time, bonks you on the head with his wand. \n"
   "After the wand hits, you wake up suddenly, now with a new huge migraine, \n"
   "and a bump on your head that wasn’t there when you fell asleep ..."
)
 
A4I = Node(
   "Grumbledore grumbles at you, frustrated that he lost to someone clearly lacking in wit. \n"
   "He decides that while the magic school isn’t quite the right fit as of yet, but he sees definite potential. \n"
   "He tells you of a Scroll of Truth, that will teach you the to see things that you couldn’t see before. \n"
   "\n"
   "Do you: \n"
   "Take the map [W] or \n"
   "Reject the map [S]"
)
  
A_A = Node(
   "You decide that you want to get your bearings, and explore the grounds. \n"
   "You see a giant man lovingly caressing a turtle with 2 heads. He sees you, and greets you. \n"
   "“Ello There! Don’t run over here; you’ll mess up the grass!\n"
   "Grumbledore said you’d be arriving any time now. \n"
   "My name’s Nagrid. You’re going to be late for your first lesson if you don’t hurry! Please follow me, come on now!” \n"
   "You go to follow, very excited, and then, as you enter the castle, you wake up. \n"
   "You crawl out of bed, and as you leave your room, you hear a gruffy voice say: 'Oi! Don't forget to make the bed!' \n"
   "You make your bed, and then are overcome with the distinct feeling that you want to reread the Harry Potter Series again. \n"
   "What else are you going to do with the quarantine going on, eh?"
)
 
A_B = Node(
   "You head inside. It is lit with floating candles and as your eyes try to see everything, you notice Grumbledore is at the end of the hall. \n"
   "You go up to him, and he says “Ah, yes, FINALLY you’ve decided to GRACE us with your presence HUMPH! But, *sigh*. \n"
   "Here, take this.” He hands you your own magic wand, and you wave it. \n"
   "The wand vibrates, and streams of spectacular multicolored air begin to dance around the castle. \n"
   "Before you can say a word or do anything, you wake up fully rested and smiling: a childhood dream come again."
)
 
A_C = Node(
   "You decide to try your luck and head for the cabin first. \n"
   "You don’t find Grumbledore there, but you do find a note that says “My, my, aren’t we a clever one. \n"
   "I suppose I should reward your curiosity. If you must know, I disappeared because I just KNEW you were going to ask a lot of questions. \n"
   "Yes, magic is real. Yes, you are technically asleep, but never mind about that. \n"
   "We will meet at the academy while your mind is resting, and you will learn the ancient art of magic. \n"
   "Here is your dream wand, and an invisibility cloak; be warned, it’s dangerous out here. \n"
   "Put it on, and come meet me at the academy! \n"
   "You wake up, unsure if it’s real, and you feel a crumbled piece of paperin your hand that reads 'it most assuredly is.'"
)
 
A_D = Node(
   "You eventually get to the spot on the map that Grumbledore marked and look up to see a huge beautiful castle. \n"
   "As you approach, you feel a hand poke your arm. You look up, startled, and see Grumbledore staring at you. \n"
   "He holds up a small wrapper and asks, 'Would you care for a sherbot lemon candy?' \n"
   "You are utterly bewildered, as out of anything he coul've said in that moment, offering you a sweet didn't make the list. \n"
   "'Oh, look who thinks they're too good for hard candy! HUMPH! Back in my day ... *grumble grumble grumble*' \n"
   "You smile as he continues grumbling on as he is wont to do, and take the candy from his hand, saying thank you. \n"
   "He eventually stops his grumbling, and the two of you head inside the castle, about to begin your first day at a school of witchcraft and wizardry."
)
 
A_E = Node(
   "You travel far with the knight, slaying many foes along the way.\n"
   "After what feels like weeks, you finally reach the cave. It is sealed shut with a boulder. \n"
   "With incredible might, you and the knight push it away, and go into the cave, seeing endless piles of treasure. \n"
   "You turn to the Knight, who has become a dear friend, and ask what to do next. \n"
   "Just as he begins to answer, you wake up in bed. You smile at the excellent adventure you had just been on. \n"
   "As you make the bed, you go to fluff a pillow, and find 10 gold coins underneath it."
)
 
A_F = Node(
   "Sir Ruis Black is deeply offended. After soundlessly shaking his head at you, he leaves you there, alone. \n"
   "You wander aimlessly  through the forest for hours, until you come across a waterfall. \n"
   "While peering over it, you lose your balance, trip, fall, and perish. \n"
   "You wake up, exhausted, feeling sad for a reason you can't quite discern, and feeling rather ill."
)
 
A_G = Node(
   "You take the map, and look it over. You see that it isn’t pointing too far away, just half a mile due north.\n"
   "You head north, and eventually come across the scroll at the bottom of the mountain. \n"
   "You open it, and begin to read it, when you suddenly wake up. \n"
   "You rub your eyes, and very happily realize that you think you know how to fix that bug in your code that’s been eluding you."
)
 
A_H = Node(
   "Grumbledore, instead of grumbling as is his norm, blankly stares at you, deep in thought. \n"
   "After some time, he pulls out his wand and flicks his wrist, casting a spell on you. \n"
   "You are transported in the middle of a pile of manure many miles away. \n"
   "You wake up, and swear, for half a second, you can hear an old man cackle."
)
 

Z = Node(
    "You wander the forest \n"
    "After about an hour you run across a bridge over a fierce river below.\n"
    "Just as you are about to step on the bridge, an adorable troll appears!\n" 
    "'Hi my name is Elfie'.\n"
    "You think to yourself ... hmm a troll named Elfie! How absurd.\n"
    "Do you: \n"
    "Laugh [W] or\n"
    "Take him seriously [S]")

ZY = Node(
    "Elfie stops talking abruptly. \n"
    "He looks at you again and says  'Wow you're a boring one aren't you?' \n"
    "You ignore him and wander to the left, and come across a black cat, doing a watercolor painting of a can of tuna with the tip of its tail. \n"
    "It notices you looking, and stares at you.\n"
    "Do you: \n"
    "Pet the cat [W] or \n"
    "compliment the painting [S]")


ZX = Node(
    "You laugh at Elfie \n" 
    "and Elfie reponds, 'Yes I know my parents were evil, but at least now I am a wealthy bridge owner, the highest honor of my people. Take this Sword of honesty on your journey'\n" 
    "Do you: \n"
    "Continue across the bridge [W] or \n"
    "Turn Right and head towards the mountains [S] ")

ZZW = Node(
    "You hear some alternative  rock music, and look around.\n" 
    "You  see some glitter flying violently through the air.\n"
    "You look more closely, and realize that there are pixies, angrily fighting.\n" 
    "You step on a twig, and they're heads swivel towards you.\n"
    "Do you: \n"
    "Run [W] or \n"
    "Talk to them [S] ")

ZZX = Node(
    "You head towards the mountains and see a swarm of jellyfish floating in the air \n" 
    "Each of them is wearing a full coat of steel plate armor.\n"
    "Hmmm ... \n"
    "Do you: \n"
    "Greet them [W] or \n"
    "Hide [S] ")



ZZY = Node(
    "The fur on the back of the cat rises, and it’s pupils fully dilate. \n"
    "It hisses at you. \n"
    "It says ‘humans are much to grabby, next time buy me dinner first.\n"
    "It grows to the size of a small house, and picks you up with its claws, then tosses you down its throat as a small snack.\n"
    "You wake up, feeling ashamed of yourself for being needlessly rude, with the smell of tuna filling your nostrils.")

ZZZ = Node(
    "The cat purrs, and grows to the size of a horse. \n"
    "It bends down, bidding you to climb onto its back." )


ZZZT = Node(
    "You run as fast as you can from the pixies. \n"
    "However, as fast you are they are faster.\n"
    "They catch up to you, and scream cursing you and saying ‘you have been cowardly and have seen things no human should have!\n"
    "You wake up, head swimming.\n"
    "Wanting to get your mind off of it, you grab your phone,\n" 
    "it floats in the air for a small second and you swear you see some sparkles and then suddenly it drops onto your face.\n" 
    "Uh oh. That isn't a good sign ...")

ZZZU = Node(
    "You talk to the pixies and ask why they are fighting.\n"
    "They do not take kindly to the interruption!\n")

ZZZV = Node(
    "You climb on, and the cat begins to walk around.\n"
    "You are enjoying the nice country air,\n" 
    "when, suddenly, the cat begins to sprint in that erratic way cats are known for.\n" 
    "You hold on for dear life, laughing, and crying, thinking you should have  known better. \n"
    "You wake up with your head spinning, and notice that there is black fur all over your shirt,\n" 
    "which is strange, considering you don't own any pets.")

ZZZW = Node(
    "They turn to your greeting, and eye you closely.\n" 
    "Then, in a mechanical voice, they say in unison: 'You are not a JELLAK, you must be exterminated!'\n" 
    "Before you can even draw your blade, their metal covered bodies begin to shake, and a giant electrical storm flies towards you;\n" 
    "killing you instantly.\n"
    "You wake up with a jolt (ba dum tss)")

ZZZY = Node(
    "You make it out undetected by the floating jellyfish. \n"
    "Eventually, you get tired, and stop paying attention, and run into a tree.\n")

Z4W = Node(
    "The pixies attack\n"
    "Do you: \n"
    "Use the Sword of Honor [W] or \n"
    "Protest the violence [S] ")
Z4W = Node("The pixies attack, and you battle them with the Sword of Honor \n"    )

Z4Y = Node(
    "The Tree bellows: 'OI! Watch it! How dare you! I am a 900 year old tree and will NOT SUFFER FOOLS!'\n"
    "Do you: \n"
    "Apologize sincerely [W] or \n"
    "Apologize with a joke to break the mood [S] ")

Z_W = Node(
    "Congratulations you won the battle! \n" 
    "Not many people can say they have defeated pixies in battle.\n" 
    "They accept your victory, and say they have a gift to give you. \n" 
    "You wake up from your dream, feeling satisfied.\n"
    "You get up, and notice a box of chocolates on your desk that wasn't there before.")

Z_X = Node(
    "You were bitterly defeated by the horde of angry pixies.\n" 
    "You die in battle, and wake up with the song 'where is my mind' stuck in your head,\n" 
    "and a cough that wasn't there before.")

Z_Y = Node(
    "The tree is placated, and says that since you were humble, it will allow you a glorious sight.\n" 
    "A branch lowers, and you climb on.\n"
    "It then raises you up 100s of feet to see the entire forest from above.\n"
    "It is surreal and utterly beautiful.\n"
    "You wake up, smelling pine, and feeling as though you are finally fully rested")

Z_Z = Node(
    "The tree, despite himself, begins to laugh uncontrollably.\n" 
    "As he is laughing, you realize that the wind is getting stronger and stronger,\n" 
    "and then a small tornado begins.\n" 
    "You are sucked up into it, and perish.\n" 
    "You wake up, and giggle that your pun made that tree barking mad.")


# defined the binary tree class to hold all of our nodes
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key




# next section (lines 461 - 504) is building our binary tree 
#   we is assigning every node to their corresponding location in the tree 
#the end comments mean its the end of that plotline
tree = BinaryTree(root)
tree.insertLeft(A)
tree.getLeftChild().insertLeft(AB)
tree.getLeftChild().insertRight(AC) #end 
tree.getLeftChild().getLeftChild().insertLeft(AAB)
tree.getLeftChild().getLeftChild().insertRight(AAC)
tree.getLeftChild().getLeftChild().getLeftChild().insertLeft(AAAB)
tree.getLeftChild().getLeftChild().getLeftChild().insertRight(AAAC)
tree.getLeftChild().getLeftChild().getRightChild().insertLeft(AAAD)
tree.getLeftChild().getLeftChild().getRightChild().insertRight(AAAE)
tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().insertLeft(A4B) #end
tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().insertRight(A4C) #end
tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().getRightChild().insertLeft(A_A) #end
tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().getRightChild().insertRight(A_B) #end
tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().insertLeft(A4D) #end
tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().insertRight(A4E)
tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().getRightChild().insertLeft(A_C) #end
tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().getRightChild().insertRight(A_D) #end
tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().insertLeft(A4F) #end
tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().insertRight(A4G)
tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().getRightChild().insertLeft(A_E) #end
tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().getRightChild().insertRight(A_F) #end
tree.getLeftChild().getLeftChild().getRightChild().getRightChild().insertLeft(A4H) #end
tree.getLeftChild().getLeftChild().getRightChild().getRightChild().insertRight(A4I)
tree.getLeftChild().getLeftChild().getRightChild().getRightChild().getRightChild().insertLeft(A_G) #end
tree.getLeftChild().getLeftChild().getRightChild().getRightChild().getRightChild().insertRight(A_H)
tree.insertRight(Z)
tree.getRightChild().insertLeft(ZX)
tree.getRightChild().insertRight(ZY)
tree.getRightChild().getLeftChild().insertLeft(ZZW)
tree.getRightChild().getLeftChild().insertRight(ZZX)
tree.getRightChild().getRightChild().insertLeft(ZZY) #end
tree.getRightChild().getRightChild().insertRight(ZZZ)
tree.getRightChild().getLeftChild().getLeftChild().insertLeft(ZZZT) #end
tree.getRightChild().getLeftChild().getLeftChild().insertRight(ZZZU)
tree.getRightChild().getLeftChild().getRightChild().insertLeft(ZZZW) #end
tree.getRightChild().getLeftChild().getRightChild().insertRight(ZZZY)
tree.getRightChild().getRightChild().getRightChild().insertLeft(ZZZV) #end
tree.getRightChild().getLeftChild().getRightChild().getRightChild().insertLeft(Z4Y)
tree.getRightChild().getLeftChild().getRightChild().getRightChild().getLeftChild().insertLeft(Z_Y) #end
tree.getRightChild().getLeftChild().getRightChild().getRightChild().getLeftChild().insertRight(Z_Z) #end
tree.getRightChild().getLeftChild().getLeftChild().getRightChild().insertLeft(Z4W)
tree.getRightChild().getLeftChild().getLeftChild().getRightChild().getLeftChild().insertLeft(Z_W) #end
tree.getRightChild().getLeftChild().getLeftChild().getRightChild().getLeftChild().insertRight(Z_X) #end

#this is where the game is built. we take into account where every choice could lead, and display the correct nodes or combat mechanic as necessary
    #we also use the chunker function here to break up the text and make it easier to read
print(tree.getRootVal())
chunker()
string = (input("Which action will you take: ")).lower()
if string == 'w':
    chunker()
    print(tree.getLeftChild().getRootVal())
    string = (input("Which action will you take: ")).lower()
    chunker()
    if string == 'w':
        print(tree.getLeftChild().getLeftChild().getRootVal())
        string = (input("Which action will you take: ")).lower()
        chunker()
        if string == 'w':
            print(tree.getLeftChild().getLeftChild().getLeftChild().getRootVal())
            string = (input("Which action will you take: ")).lower()
            chunker()
            if string == 'w':
                print(tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().getRootVal())
                string = (input("Which action will you take: ")).lower()
                chunker()
                if string == 'w':
                    print(tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().getLeftChild().getRootVal())
                    #end of that plot
                elif string == 's':
                    print(tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().getRightChild().getRootVal())
                    string = (input("Which action will you take: ")).lower()
                    chunker()
                    if string == 'w':
                        print(tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().getRightChild().getLeftChild().getRootVal())
                        #end of that plot
                    elif string == 's':
                        print(tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().getRightChild().getRightChild().getRootVal())
                    else:
                        print('invalid entry')
                else:
                    print("invalid entry")
            elif string == 's':
                print(tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().getRootVal())
                string = (input("Which action will you take: ")).lower()
                chunker()
                if string == 'w':
                    print(tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().getLeftChild().getRootVal())
                    #end of that plot
                elif string == 's':
                    print(tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().getRightChild().getRootVal())
                    string = (input("Which action will you take: ")).lower()
                    chunker()
                    if string == 'w':
                        print(tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().getRightChild().getLeftChild().getRootVal())
                        #end of that plot
                    elif string == 's':
                        print(tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().getRightChild().getRightChild().getRootVal())
                        #end of that plot
                else:
                    print('invalid entry')
            else:
                print("invalid entry")
            
        elif string == 's':
            print(tree.getLeftChild().getLeftChild().getRightChild().getRootVal())
            string = (input("Which action will you take: ")).lower()
            chunker()
            if string == 'w':
                print(tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().getRootVal())
                string = (input("enter W to fight: ")).lower()
                if string == 'w':
                    fight = combat()
                    print(fight)
                    if fight == "You win! :)":
                        chunker()
                        print(tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().getRightChild().getRootVal())
                        string = (input("Which action will you take: ")).lower()
                        chunker()
                        if string == 'w':
                            print(tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().getRightChild().getLeftChild().getRootVal())
                            #end of that plot
                        elif string == 's':
                            print(tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().getRightChild().getRightChild().getRootVal())
                            #end of that plot
                        else:
                            print('invalid entry')
                    else:
                        chunker()
                        print(tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().getLeftChild().getRootVal())
                        #end of this plot
                else:
                    print("invalid entry")
            elif string == 's':
                print(tree.getLeftChild().getLeftChild().getRightChild().getRightChild().getRootVal())
                string = (input("Enter W to have a thumb war!: ")).lower()
                if string == 'w':
                    fight = combat()
                    print(fight)
                    if fight == "You win! :)":
                        chunker()
                        print(tree.getLeftChild().getLeftChild().getRightChild().getRightChild().getRightChild().getRootVal())
                        string = (input("Which action will you take: ")).lower()
                        chunker()
                        if string == 'w':
                            print(tree.getLeftChild().getLeftChild().getRightChild().getRightChild().getRightChild().getLeftChild().getRootVal())
                            #end of that plot:
                        elif string == 's':
                            print(tree.getLeftChild().getLeftChild().getRightChild().getRightChild().getRightChild().getRightChild().getRootVal())
                            #end of tha plot
                        else:
                            print("invalid entry")
                    else:
                        chunker()
                        print(tree.getLeftChild().getLeftChild().getRightChild().getRightChild().getLeftChild().getRootVal())
                        #end of that plot
                else:
                    print("invalid entry")
        else:
            print("invalid entry.")
    elif string == 's':
        print(tree.getLeftChild().getRightChild().getRootVal())  
        #end of that plot          
    else:
        print("invalid entry")

elif string == 's':
    print(tree.getRightChild().getRootVal())
    chunker()
    string = (input("Which action will you take: ")).lower()
    if string == 's':
        print (tree.getRightChild().getRightChild().getRootVal())
        chunker()
        string = (input("Which action will you take: ")).lower()
        if string == 's':
            print(tree.getRightChild().getRightChild().getRightChild().getRootVal())
            chunker()
            string = (input("enter W to climb aboard: ")).lower()
            if string == 'w':
                print(tree.getRightChild().getRightChild().getRightChild().getLeftChild().getRootVal())
            else:
                print("invalid entry")
        elif string == 'w':
            print(ZZY.getData())
			#break
        else:
            print("invalid entry")
    elif string == 'w':
        print(ZX.getData())
        chunker()
        string = (input("Which action will you take: ")).lower()
        if string == 's':
            print(ZZX.getData())
            chunker()
            string = (input("Which action will you take: ")).lower()
            if string == 's':
                print(tree.getRightChild().getLeftChild().getRightChild().getRightChild().getRootVal())
                chunker()
                string = (input("enter W to continue: ")).lower()
                if string == 'w':
                    print(tree.getRightChild().getLeftChild().getRightChild().getRightChild().getLeftChild().getRootVal())
                    chunker()
                    string = (input("Which action will you take: ")).lower()
                    if string == 's':
                        print(tree.getRightChild().getLeftChild().getRightChild().getRightChild().getLeftChild().getRightChild().getRootVal())
						#break
                    elif string == 'w':
                        print(tree.getRightChild().getLeftChild().getRightChild().getRightChild().getLeftChild().getLeftChild().getRootVal())
                        #break
                    else:
                        print("invalid entry")
                else:
                    print("invalid entry")
            elif string == 'w':
                print(tree.getRightChild().getLeftChild().getRightChild().getLeftChild().getRootVal())
				#break
            else:    
                print("invalid entry")
        elif string == 'w':
            print(tree.getRightChild().getLeftChild().getLeftChild().getRootVal())
            chunker()
            string = (input("Which action will you take: ")).lower()
            if string == 's':
                print(tree.getRightChild().getLeftChild().getLeftChild().getRightChild().getRootVal())
                chunker()
                string = (input("enter W to continue: ")).lower()
                if string == 'w':
                    print(tree.getRightChild().getLeftChild().getLeftChild().getRightChild().getLeftChild().getRootVal())
                    string = (input("enter W to fight: ")).lower()
                    fight = combat()
                    print(fight)
                    chunker()
                    if fight == "You win! :)":
                        print(tree.getRightChild().getLeftChild().getLeftChild().getRightChild().getLeftChild().getLeftChild().getRootVal())
						#break
                    else:
                        print(tree.getRightChild().getLeftChild().getLeftChild().getRightChild().getLeftChild().getRightChild().getRootVal())
						#break
                else:
                    print("invalid entry")
            elif string == 'w':
                print(tree.getRightChild().getLeftChild().getLeftChild().getLeftChild().getRootVal())
				#break
            else:
                print("invalid entry")
        else:
            print("invalid entry")
    else:
        print("invalid entry")

else:
    print('invalid entry.')
print("\nGame Over \nThanks for playing!")