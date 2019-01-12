import numpy as np


# Name columns of equipment array
name = 0
weight = 1
quantity = 2
location = 3
container_capacity = 4
level = 5
itemOrder = 6
notes = 7

# Money quantities - [gold, silver, copper]
money = np.array([191,8,3])

# Equipment array
equipment = np.array([
    ("Acid (vial)",1,2,"Basket","",0,0,"This glass vial is held in a protective holster and contains acid. As an action, you can splash the contents of this vial onto a creature within 5 feet of you or throw the vial up to 20 feet, shattering it on impact. In either case, make a ranged attack against a creature or object, treating the acid as an improvised weapon. On a hit, the target takes 2d6 acid damage."),
    ("Alchemy Jug",12,1,"Bag of Holding","",0,0,"This ceramic jug appears to be able to hold a gallon of liquid and weighs 12 pounds whether full or empty. Sloshing sounds can be heard from within the jug when it is shaken, even if the jug is empty.<br><br>You can use an action and name one liquid from the table below to cause the jug to produce the chosen liquid. Afterward, you can uncork the jug as an action and pour that liquid out, up to 2 gallons per minute. The maximum amount of liquid the jug can produce depends on the liquid you named.<br><br>Once the jug starts producing a liquid, it can't produce a different one, or more of one that has reached its maximum, until the next dawn.<table class='itemNotesTable'><tr><th>Liquid</th><th>Max Amount</th></tr><tr><td>Acid</td><td>8 ounces</td></tr><tr><td>Basic poison</td><td>1/2 ounce</td></tr><tr><td>Beer</td><td>4 gallons</td></tr><tr><td>Honey</td><td>1 gallon</td></tr><tr><td>Maynnaise</td><td>2 gallons</td></tr><tr><td>Oil</td><td>1 quart</td></tr><tr><td>Vinegar</td><td>2 gallons</td></tr><tr><td>Water, fresh</td><td>8 gallons</td></tr><tr><td>Water, salt</td><td>12 gallons</td></tr><tr><td>Wine</td><td>1 gallon</td></tr></table><br><img src='images/alchemy_jug.png'/>"),
    ("Amani Verig Pendant",0,1,"Wearing","",0,0,"On a string hangs a smooth stone with a simple symbol carved into it.<br><br><img src='images/amani_varig_pendant.png'/>"),
    ("Bag of Holding",15,1,"Belt","500",0,0,"This bag looks like a standard drawstring pouch but has an interior space considerably larger than its outside dimensions, roughly 2 feet in diameter at the mouth and 4 feet deep. The bag can hold up to 500 pounds, not exceeding a volume of 64 cubic feet. The bag weighs 15 pounds, regardless of its contents. Retrieving an item from the bag requires an action.<br><br>If the bag is overloaded, pierced, or torn, it ruptures and is destroyed, and its contents are scattered in the Astral Plane. If the bag is turned inside out, its contents spill forth, unharmed, but the bag must be put right before it can be used again. Breathing creatures inside the bag can survive up to a number of minutes equal to 10 divided by the number of creatures (minimum 1 minute), after which time they begin to suffocate.<br><br>Placing a bag of holding inside an extradimensional space created by a handy haversack, portable hole, or similar item instantly destroys both items and opens a gate to the Astral Plane. The gate originates where the one item was placed inside the other. Any creature within 10 feet of the gate is sucked through it to a random location on the Astral Plane. The gate then closes. The gate is one-way only and can't be reopened.<br><br><img src='images/bag_of_holding.png'/>"),
    ("Basket",2,1,"Bag of Holding","40",0,0,"This is large basket has a sturdy lid and can hold up to 2 cubic feet/40 pounds of gear. Currently, it primarily holds cooking supplies."),
    ("Bedroll",7,1,"Bag of Holding","",0,0,"You never know where you're going to sleep, and a bedroll helps you get better sleep in a hayloft or on the cold ground. A bedroll consists of bedding and a blanket thin enough to be rolled up and tied. In an emergency, it can double as a stretcher."),
    ("Book of Poetry",2,1,"Bag of Holding","",0,0,"This book is filled with traditional Elvish poetry for children."),
    ("Bottled Breath",0.5,1,"Bag of Holding","",0,0,"This bottle contains a breath of elemental air. When you inhale it, you either exhale it or hold it.<br><br>If you exhale the breath, you gain the effect of the gust of wind spell. If you hold the breath, you don't need to breathe for 1 hour, though you can end this benefit early (for example, to speak). Ending it early doesn't give you the benefit of exhaling the breath."),
    ("Clothes, Traveller's",4,1,"Wearing","",0,0,"Belt has a holster for one flask and holsters for 10 darts; other things (pouches, Shanga beads) may be tied to it"),
    ("Coin Pouch",1,1,"Bag of Holding","6",0,0,"This cloth pouch can hold 1/5 cubic foot/ 6 pounds of gear."),
    ("Cook's Utensils",8,1,"Basket","",0,0,"Cook's utensils include a metal pot, knives, forks, a stirring spoon, and a ladle. Proficiency with Cook's Utensils lets you add your proficiency bonus to any ability checks you make using these tools."),
    ("Coins, Gold Pieces",.02,money[0],"Coin Pouch","",0,0,""),
    ("Coins, Silver Pieces",.02,money[1],"Coin Pouch","",0,0,""),
    ("Coins, Copper Pieces",.02,money[2],"Coin Pouch","",0,0,""),
    ("Dart",0.25,9,"Belt","",0,0,"Ranged attack: <b>1d4+4 piercing (20 ft/60 ft)</b><br><br>Proficiency with a dart allows you to add your proficiency bonus to the attack roll for any attack you make with it. Ten darts fit in small holsters in my belt."),
    ("Grappling Hook",4,1,"Bag of Holding","",0,0,"This grappling hook, which is tied to the end of the hempen rope, can secure the rope to a battlement, window ledge, tree limb, or other protrusion."),
    ("Healer's Kit",3,1,"Belt","",0,0,"Uses left: 5<br><br>This kit is a leather pouch containing bandages, salves, and splints. The kit has ten uses total. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check."),
    ("Healer's Kit (spare)",3,1,"Bag of Holding","",0,0,"Uses left: 10<br><br>This kit is a leather pouch containing bandages, salves, and splints. The kit has ten uses total. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check."),
    ("Herbalism Kit",3,1,"Bag of Holding","",0,0,"This kit contains a variety of instruments such as clippers, mortar and pestle, and pouches and vials used by herbalists to create remedies and potions. Proficiency with this kit lets you add your proficiency bonus to any ability checks you make to identify or apply herbs. Also, proficiency with this kit is required to create antitoxin and any potion of healing."),
    ("Heward's Handy Spice Pouch",0,1,"Basket","",0,0,"This belt pouch appears empty and has 10 charges. While holding the pouch, you can use an action to expend 1 of its charges, speak the name of any nonmagical food seasoning (such as salt, pepper, saffron, or cilantro), and remove a pinch of the desired seasoning from the pouch. A pinch is enough to season a single meal. The pouch regains 1d6 + 4 expended charges daily at dawn.<br><br><img src='images/spice_pouch.png'/>q"),
    ("Honey (jar)",3,1,"Basket","",0,0,"A ceramic jar filled with one pint of delicious honey. The jar has a protective holster."),
    ("Mess Kit",1,1,"Basket","",0,0,"This tin box contains a cup and simple cutlery. The box clamps together, and one side can be used as a cooking pan and the other as a plate or shallow bowl."),
    ("Oil (flask)",1,1,"Basket","",0,0,"This ceramic flask holds 1 pint of oil and has a removable protective holster. As an action, you can splash the oil in this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. Make a ranged attack against a target creature or object, treating the oil as an improvised weapon. On a hit, the target is covered in oil. If the target takes any fire damage before the oil dries (after 1 minute), the target takes an additional 5 fire damage from the burning oil. You can also pour a flask of oil on the ground to cover a 5-foot-square area, provided that the surface is level. If lit, the oil burns for 2 rounds and deals 5 fire damage to any creature that enters the area or ends its turn in the area. A creature can take this damage only once per turn."),
    ("Oil (bottle)",3,1,"Basket","",0,0,"This ceramic bottle holds up to 1 1/2 pints of cooking oil."),
    ("Paper Birds",0,2,"Bag of Holding","",0,0,"After you write a message of fifty words or fewer on this magic sheet of parchment and speak a creature's name, the parchment magically folds into a Tiny paper bird and flies to the recipient whose name you uttered. The recipient must be on the same plane of existence as you, otherwise the bird turns into ash as it takes flight.<br><br>The bird is an object that has 1 hit point, an Armor Class of 13, a flying speed of 60 feet, a Dexterity of 16 (+3), and a score of 1 (-5) in all other abilities, and it is immune to poison and psychic damage.<br><br>It travels to within 5 feet of its intended recipient by the most direct route, whereupon it turns into a nonmagical and inanimate sheet of parchment that can be unfolded only by the intended recipient. If the bird's hit points or speed is reduced to 0 or if it is otherwise immobilized, it turns into ash.<br><br>These paper birds came in small, wooden tube containing 8 sheets of the parchment. They were labeled "+'"'+"Magic Marge's Marvelous Mynas."+'"<br><br><img src="images/paper_birds.png"/>'),
    ("Poison, Basic (vial)",0,1,"Basket","",0,0,"You can use the poison in this metal vial to coat one slashing or piercing weapon or up to three pieces of ammunition. Applying the poison takes an action. A creature hit by the poisoned weapon or ammunition must make a DC 10 Constitution saving throw or take 1d4 poison damage. Once applied, the poison retains potency for 1 minute before drying."),
    ("Potion of Animal Friendship",0.5,1,"Bag of Holding","",0,0,"When you drink this potion, you can cast the <a href='https://www.dndbeyond.com/spells/animal-friendship'>animal friendship</a> spell (save DC 13) for 1 hour at will. Agitating this muddy liquid brings little bits into view: a fish scale, a hummingbird tongue, a cat claw, or a squirrel hair."),
    ("Potion of Greater Healing",0.5,1,"Belt","",0,0,"You regain 4d4 + 4 hit points when you drink this potion. The potion's red liquid glimmers when agitated.<br><br><img src='images/potion_of_healing_greater.png'/>"),
    ("Potion of Healing",0.5,1,"Belt","",0,0,"A character who drinks the magical red fluid in this vial regains 2d4 + 2 hit points. Drinking or administering a potion takes an action.<br><br><img src='images/potion_of_healing.png'/>"),
    ("Quarterstaff",4,1,"Carrying","",0,0,"Melee attack: <b>1d6+4 (1d8+4) bludgeoning</b><br><br>This long wooden staff makes a good weapon and a good walking stick."),
    ("Rations (1 day)",2,2,"Basket","",0,0,"Rations consist of dry foods suitable for extended travel, including jerky, dried fruit, hardtack, and nuts."),
    ("Rope, Hempen (50 feet)",0,1,"Bag of Holding","",0,0,"Hempen rope has 2 hit points and can be burst with a DC 17 Strength check. This rope has a grappling hook tied to one end."),
    ("Shanga Beads",0,1,"Belt","",0,0,"Twenty hand-painted wooden counting beads are attached at one end to a hand-woven string. These are used in the daily Nidhamu ritual, and are otherwise tied at the waist."),
    ("Tinderbox",1,1,"Basket","",0,0,"This small container holds flint, fire steel, and tinder (usually dry cloth soaked in light oil) used to kindle a fire. Using it to light a torch -- or anything else with abundant, exposed fuel -- takes an action. Lighting any other fire takes 1 minute."),
    ("Waterskin",5,1,"Bag of Holding","",0,0,"A waterskin can hold 4 pints of liquid."),
    ("Wine (bottle)",3,1,"Basket","",0,0,"This ceramic bottle holds 1.5 pints of wine. The bottle has a protective holster."),
    ("Wooden Rabbit Mask",2,1,"Bag of Holding","",0,0,"This large face mask is shaped like a rabbit's head and made of thin, somewhat flexible wood.<br><br><img src='images/wooden_rabbit_mask.png'/>"),
    ])


# List of unique locations
locations = np.unique(equipment[:,location])


# Loop through, organize items in order based on nested containers
count = 0
# loop through locations
for iLoc in locations:
    # if location is not itself an object, print it
    if iLoc not in equipment[:,name]:
        # go through location's items
        for iItem in equipment[equipment[:,location] == iLoc]:
            # if location's item is not another location, print it
            if iItem[name] not in locations:
                equipment[equipment[:,name]==iItem[name],level] = 1
                count += 1
                equipment[equipment[:,name]==iItem[name],itemOrder] = count
            # if location's item IS another location (loc2), print it with its items...
            else:
                loc2 = iItem[name]
                equipment[equipment[:,name]==iItem[name],level] = 1
                count += 1
                equipment[equipment[:,name]==iItem[name],itemOrder] = count
                # loop through loc2's items
                for iItem2 in equipment[equipment[:,location]==loc2]:
                    # if loc2's item is not another location, print it
                    if iItem2[name] not in locations:
                        equipment[equipment[:,name]==iItem2[name],level] = 2
                        count += 1
                        equipment[equipment[:,name]==iItem2[name],itemOrder] = count
                    # if loc2's item IS another location (loc3), print it with its items
                    else:
                        loc3 = iItem2[name]
                        equipment[equipment[:,name]==iItem2[name],level] = 2
                        count += 1
                        equipment[equipment[:,name]==iItem2[name],itemOrder] = count
                        # loop through loc3's items and print all
                        for iItem3 in equipment[equipment[:,location]==loc3]:
                            equipment[equipment[:,name]==iItem3[name],level] = 3
                            count += 1
                            equipment[equipment[:,name]==iItem3[name],itemOrder] = count


# Sort items in order set in above series of loops
itemOrder_list = np.array(map(int, equipment[:,itemOrder]))   # makes list of strings into list of ints
equipment_sort = equipment[itemOrder_list.argsort()]

# ==============================================================================
# WRITE HTML FILE

# Function checks if an item is in the bag of holding or is in an item which is in the bag of holding
def inBoH(item):
    isInBoH = False
    if item[location] in equipment[:,name]:
        location_item = equipment[equipment[:,name]==item[location]][0]
        isInBoH = "Bag of Holding"==item[location] # check whether item's location is Bag of Holding
        isInBoH = isInBoH or "Bag of Holding"==location_item[location] # check whether item's location's location is Bag of Holding
    return isInBoH

# Function checks if an item is in a container or is in an item which is in the container
def inContainer(item,container_item):
    isInContainer = False
    if item[location] in equipment[:,name]:
        location_item = equipment[equipment[:,name]==item[location]][0]
        isInContainer = container_item[name]==item[location] # check whether item's location is container
        isInContainer = isInContainer or container_item[name]==location_item[location] # check whether item's location's location is container
    return isInContainer

# Write standard (non-container) item to HTML table string
def writeItem(item):
    str = '\t<table><tr class="level'+item[level]+'" id="item'+item[itemOrder]+'" onclick='+"'"+'$("#item'+item[itemOrder]+'_notes").slideToggle();'+"'"+'>'
    item_weight = float(item[weight]) * float(item[quantity])
    item_weight_str = '%.1f' % item_weight
    str = str + '<td class="itemName">'+item[name]+'</td><td class="itemWeight">'+item_weight_str+' lb.</td><td class="itemQuantity">'+item[quantity]+'</td><td class="itemLocation">'+item[location]+'</td></tr></table>\n'
    # div for item notes
    str = str + '\t\t<div class="itemNotes" id="item'+item[itemOrder]+'_notes"><p>'+item[notes]+'</p></div>'
    return str

# Write container item to HTML table string
def writeContainer(item_container, container_num):
    weight_str = '%.1f' % float(item_container[weight])
    str = '<table><tr class="level'+item_container[level]+'" id="item'+item_container[itemOrder]+'" id="container'+repr(container_num)+'" onclick='+"'"+'$("#container'+repr(container_num)+'_contents").slideToggle();$("#item'+item_container[itemOrder]+'_notes").slideToggle();'+"'"+'>'
    str = str + '<td class="itemName">'+item_container[name]+' <em>[container]</em></td><td class="itemWeight">'+weight_str+' lb.</td><td class="itemQuantity">'+'--'+'</td><td class="itemLocation">'+item_container[location]+'</td></tr></table>'

    # Calculate contained weight
    contained_weight = 0
    for iItem in equipment:
        if inContainer(iItem,item_container):
            iItem_weight = float(iItem[weight]) * float(iItem[quantity])
            contained_weight += iItem_weight

    # div for item notes
    str = str + '\t\t<div class="itemNotes" id="item'+item_container[itemOrder]+'_notes">'
    # option to close container description
    str = str + '<p class="close_description_button" onclick='+"'"+'$("#item'+item_container[itemOrder]+'_notes").slideToggle();'+"'"+'>[Close description]</p>'
    contained_weight_str = '%.1f' % contained_weight
    str = str + '<p>Contains '+contained_weight_str+' lb. of items (max: '+item_container[container_capacity]+' lb.)</p>'
    str = str + '<p>'+item_container[notes]+'</p></div>'
    return str


# head of HTML file
html = open('index.html','w')
html.write('<!DOCTYPE html>\n<html>\n<head>\n\t<title>Kisha'+"'"+'s Equipment</title>\n\n\t<link rel="stylesheet" type="text/css" href="style.css">\n\n\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n\t<script src="script.js"></script>\n</head>\n<body>\n\n')

# Total weight carried and money
total_weight_carried = 0
for iItem in equipment_sort:
    if not inBoH(iItem):
        total_weight_carried += float(iItem[weight]) * float(iItem[quantity])
# Add weight of coins, if not in Bag of Holding
coin_pouch = equipment[equipment[:,name]=="Coin Pouch"][0]
if not inBoH(coin_pouch): total_weight_carried += 0.02 * sum(money)
html.write('<p id="weightCarried">Weight carried: '+repr(total_weight_carried)+'</p>\n')
if total_weight_carried < (15*8): html.write('<p id="encumbrance">Unencumbered</p>\n\n')
html.write('<p id="money"><b>Gold:</b> '+repr(money[0])+', <b>Silver:</b> '+repr(money[1])+', <b>Copper:</b> '+repr(money[2])+'</p>\n\n')

# HTML table of inventory
html.write('<table><tr><th class="Name">Item</th><th class="Weight">Weight</th><th class="Quantity">Quantity</th><th class="Location">Location</th></tr></table>\n')

container_num = 0;  # counting number of containers
for i,iItem in enumerate(equipment_sort):

    # check if item is first level
    if iItem[level] == '1':
        if iItem[name] in locations:
            # add id of container# to tr, write line
            container_num += 1
            str = writeContainer(iItem,container_num)
            html.write('\t'+str+'\n')

            # made div for container level 1 contents
            html.write('\t<div id="container'+repr(container_num)+'_contents">\n')
            count = i+1;
            contained_item = equipment_sort[count]
            while contained_item[level] == '2':

                if contained_item[name] in locations:    # deal with container (level 2) inside container (level 1)
                    # add id of container# to tr
                    container_num += 1
                    str = writeContainer(contained_item,container_num)
                    html.write('\t\t'+str+'\n')

                    # make div for container level 2 contents
                    html.write('\t\t<div id="container'+repr(container_num)+'_contents">\n')
                    count += 1
                    contained_item = equipment_sort[count]

                    while contained_item[level] == '3': # write items contained in container level 2
                        str = writeItem(contained_item)
                        html.write('\t\t'+str+'\n')

                        count += 1
                        contained_item = equipment_sort[count]

                    # close div for container level 2 contents
                    html.write('\t\t</div>\n')

                else:   # write items contained in container level 1
                    str = writeItem(contained_item)
                    html.write('\t'+str+'\n')

                    count += 1
                    contained_item = equipment_sort[count]

            # close dive for container level 1 contents
            html.write('\t</div>\n')

        else:   # write items non-contained and non-container items
            str = writeItem(iItem)
            html.write(str+'\n')



# finish HTML file
html.write('\n</body>\n</html>')
html.close()
