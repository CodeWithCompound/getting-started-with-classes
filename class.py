# FOR GITHUB READERS
# was explaining this to my girlfriend and decided to keep the comments in for explanation.

#our class where we say each animal has a kind and color
class Animal:
    def __init__(self, kind: str, color: str):
        self.kind = kind
        self.color = color

    def __str__(self):
        return f"{self.kind} {self.color}"
    
kitty = Animal("cat", "red")
doggo = Animal("dog", "blue")
# and now we can say we want a yellow dolphin
dol = Animal("dolphin", "yellow")
print(doggo, kitty)
# if we now check below:
print(dol)
#we can also look for only the color
print(doggo.color, kitty.color, dol.color)
# very easy to understand example here with 
# class animals and we have a kitty and dog

# right, look otherwise you'd need to do something like this
bee_1_health = 100
bee_2_health = 100
bee_3_health = 100
bee_4_health = 100
# and that for each one

#instead we can make a class 
# either insect or bee or whatever

print("\n\n\n\n\n")

#actually let me include a number (index) for each bee!
class Bee:
    def __init__ (self,name: str, health: int):
        self.name = name
        self.health = health
    #dw about this below it is just to make
    #the printing more pretty
    def __str__(self):
        return f"Name: (Bee) {self.name}\nHealth: {self.health}"
    
#right so we now said we have a blueprint
#for bees and each bee is a name and health
#here i will make a little number indicating
#how many bees we have in total 

amount_bees = 20
for i in range(amount_bees):
    print(Bee(i + 1, 100))
