# Define class for items in inventory
class Item:
    def __init__(self,name,weight,quantity,location,notes):
        self.name = name
        self.weight = weight
        self.quantity = quantity
        self.location = location
        self.notes = notes

# List items in inventory
inventory = [
    Item("Acid (vial)",1,2,"Bag of Holding, Basket","Vial is made of glass, has protective holster"),
    Item("Alchemy Jug",12,1,"Bag of Holding",""),
    Item("Amani Verig Pendant",0,1,"Wearing",""),
    Item("Bag of Holding",15,1,"Belt","Looks like a large drawstring pouch"),
    Item("Basket",2,1,"Bag of Holding","Large basket with lid for holding cooking supplies"),
    Item("Bedroll",7,1,"Bag of Holding",""),
    Item("Book of Poetry",2,1,"Bag of Holding",""),
    Item("Clothes, Traveller's",4,1,"Wearing","Belt has a holster for one flask and holsters for 10 darts; other things (pouches, Shanga beads) may be tied to it"),
    Item("Coin Pouch",1,1,"Bag of Holding",""),
    Item("Cook's Utensils",8,1,"Bag of Holding, Basket","Includes a metal pot, knives, forks, a stirring spoon, and a ladle"),
    Item("Dart",0.25,9,"Belt","Darts fit in small holsters on belt"),
    Item("Grappling Hook",4,1,"Bag of Holding","Tied to on end of the hempen rope"),
    Item("Healer's Kit",3,1,"Belt","7 uses left"),
    Item("Heward's Handy Spice Pouch",0,1,"Bag of Holding, Basket",""),
    Item("Honey (jar)",3,1,"Bag of Holding, Basket","Jar is made of ceramic, has protective holster"),
    Item("Mess Kit",1,1,"Bag of Holding, Basket",""),
    Item("Oil (flask)",1,1,"Bag of Holding, Basket","Flask is made of ceramic, has protective holster"),
    Item("Oil (bottle)",3,1,"Bag of Holding, Basket","Bottle is made of ceramic, has protective holster"),
    Item("Poison, Basic (vial)",0,1,"Bag of Holding, Basket","Vial is made of metal"),
    Item("Quarterstaff",4,1,"Carrying",""),
    Item("Rations (1 day)",2,2,"Bag of Holding, Basket",""),
    Item("Rope, Hempen (50 feet)",10,1,"Bag of Holding",""),
    Item("Shanga Beads",0,1,"Wearing",""),
    Item("Tinderbox",1,1,"Bag of Holding, Basket",""),
    Item("Waterskin",5,1,"Bag of Holding",""),
    Item("Wine (bottle)",3,1,"Bag of Holding, Basket","Bottle is made of ceramic, has protective holster"),
    Item("Wooden Rabbit Mask",2,1,"Bag of Holding",""),
    ]

# Function to print info about an item, given name string as input
def itemInfo(itemName_str):
    for iItem in inventory:
        if iItem.name == itemName_str:
            item = iItem
            break
    print item.name
    print '  Weight: '+repr(item.weight)
    print '  Quantity: '+repr(item.quantity)+' lbs'
    print '  Location: '+item.location
    if item.notes != '':
        print '  Notes: '+item.notes

# Generate list of item locations
locations = []
for i in inventory:
    if i.location not in locations:
        locations.append(i.location)
locations = sorted(locations)   # puts in alphabetical order

# Print (and save) inventory, organized by item location
print '\nINVENTORY LIST'
ordered_inv = []
for iLocation in locations:
    print iLocation
    for iItem in inventory:
        if iItem.location == iLocation:
            ordered_inv.append(iItem)
            if iItem.quantity == 1:
                print '  '+iItem.name
            elif iItem.quantity > 1:
                print '  '+iItem.name+' ('+repr(iItem.quantity)+')'

# Calculate weight of carried inventory
print '\nCARRIED WEIGHT'
weight = 0
for iItem in inventory:
    if iItem.location != 'Bag of Holding' and iItem.location != 'Bag of Holding, Basket':
        weight += iItem.weight*iItem.quantity
        if iItem.quantity == 1:
            print '  '+iItem.name+': '+repr(iItem.weight)+' lbs'
        elif iItem.quantity > 1:
            print '  '+iItem.name+' ('+repr(iItem.quantity)+'): '+repr(iItem.weight*iItem.quantity)+' lbs'
print 'TOTAL WEIGHT: '+repr(weight)

# Calculate weight of items inside Bag of Holding, prints warning if too many items
weight_boh = 0
for iItem in inventory:
    if iItem.location == 'Bag of Holding' or iItem.location == 'Bag of Holding, Basket':
        weight_boh += iItem.weight*iItem.quantity
if weight_boh > 500: print 'WARNING - Too many items inside Bag of Holding'

# Calculate weight of items inside Basket, prints warning if too many items
weight_basket = 0
for iItem in inventory:
    if iItem.location == 'Bag of Holding, Basket':
        weight_basket += iItem.weight*iItem.quantity
if weight_basket > 40: print 'WARNING - Too many items inside Basket'
