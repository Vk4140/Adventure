import json
import sys


"""abbreviations = {
  "i": "inventory",
  "g": "get",
  "go": "go",
  "gn": "go north"
}
def process_input(input_string):
# Split the input string into words
  words = input_string.split()

# If the first word is an abbreviation, replace it with the full command name
  if words[0] in abbreviations:
    words[0] = abbreviations[words[0]]

# Return the modified input string as a tuple of (command, arguments)
  return (words[0], words[1:])"""

def getRoomDetails(map, i=0):
    print("> " + map[i]["name"])
    print(map[i]["desc"])
    exits = map[i]["exits"].keys()
    if "items" in map[i].keys():
        items = map[i]["items"]
        if len(items) != 0:
            print("Items:", end=" ")
            for i in range(len(items) - 1):
                print(items[i], end=", ")
            print(items[len(items) - 1])
    print("Exits: ", end='')
    for i in exits:
        print(i, end=" ")

    print()

file = open("loop.map.json")
#file = open("C:\\Users\\vamsi\\OneDrive\\Desktop\\cs515\\Project_1\\loop.map.json")
s = file.read()
map = json.loads(s)
length = len(map)

i = 0
getRoomDetails(map)
inventory = []
a = input("What would you like to do?").lower()


while a != 'quit':
    a = a.split()
    if a[0] == 'go' and len(a) <= 2:
        if len(a) == 1:
            print("Sorry, you need to 'go' somewhere.")
        
        elif a[1] in map[i]["exits"].keys():
            i = map[i]["exits"][a[1]]
            print("You go", a[1] + ".")
            getRoomDetails(map, i)
        else:
            print("There's no way to go " + a[1] + ".")
    elif a[0].lower() == "help":
                print("You can run the following commands:")
                print("  inventory\t")
                print("  drop\t")
                print("  boss open\t")
                print("  help\t")
                print("  quit\t")
                print("  go ...\t")
                print("  get ...\t")
                print("  look\t")
    #elif a[0].lower():
        #command, arguments = process_input(a[0])            
    elif a[0] == "look" and len(a) <= 1:
        getRoomDetails(map, i)
    elif a[0] == "inventory"  and len(a) <= 1:
        if len(inventory) == 0:
            print()
            print("You're not carrying anything.")
        else:
            print("Inventory: ")
            for item in inventory:
                print(item)
    elif a[0] == "get" and len(a) <= 2:
        items = map[i]["items"]
        if len(a) == 1:
            print("Sorry, you need to 'get' something.")
        
        elif a[1] not in items:
            print()
            print("There's no " + a[1] + " anywhere.")
        else:
            inventory.append(a[1])
            map[i]["items"].remove(a[1])
            print("You pick up the " + a[1] + ".")
    else:
        print('wrong input')
    a = input("What would you like to do?").lower()
print("Goodbye!")