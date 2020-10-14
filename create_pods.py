import json
import random


# Read characters into list
with open("non-dlc-characters.txt", "r") as character_file:
    draftable_characters = [i.rstrip() for i in character_file.readlines()]

# Remove Mike's veto's
# https://tenor.com/bmcQR.gif
draftable_characters.remove("Bowser")
draftable_characters.remove("Incineroar")

# Generate pods dict
pods = {
    "Mike":[],
    "Phil":[],
    "Kyle":[],
    "Sam":[],
    "Brian":[],
    "Marlene":[],
    "Nick":[],
    "Nik":[]
}

# Combine the seeds of all for one... master seed
random.seed(
      69            # Brian
    + 69            # Kyle
    + 70            # Sam
    + 420           # Mike
    + 23            # Marlene
    + 146601812     # Nick
    + 544           # Phil
    + 347           # Jan (wildcard)
    + int(0x533d)   # Nik
)

# Populate pods
for i in range(0,5):
    for name in pods.keys():
        draft_choice = random.choice(draftable_characters)
        pods[name].append(draft_choice)
        draftable_characters.remove(draft_choice)

print("Pods:\n", json.dumps(pods, indent=4))
print("Remaining Draftable Characters:")
for character in draftable_characters:
    print(character)
