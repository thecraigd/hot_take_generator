import random

list1 = ["FKA Twigs", "Carly Rae Jepsen", "Grimes", "The Streets", "Danny Brown", "DaBaby", "Mannequin Pussy", "Idles"]
list2 = ["The Beatles", "Led Zeppelin", "Lynyrd Skynrd", "Taylor Swift", "Carly Rae Jepsen", "Coolio", "Death Grips"]
list3 = ["Metallica", "Mansun", "Marilyn Manson", "The Smashing Pumpkins", "Alanis Morissete", "Transvision Vamp", "Carly Rae Jepsen", "Sonic Youth"]

item1 = random.choice(list1)
item2 = random.choice(list2)
item3 = random.choice(list3)

print(item1 + " is just " + item2 + " for people who like " + item3 + ".")