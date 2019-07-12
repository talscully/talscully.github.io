import numpy as np

# Carrying information
carryingBackpack = False
backpack_location = 'Inn'
carryingRopeWOutBackpack = False
carryingCoinsWOutBackpack = False

# Money quantities - [gold, silver, copper]
money = np.array([24,7,10])

# Name columns of equipment array
name = 0
weight = 1
quantity = 2
location = 3
carrying = 4
container_capacity = 5
magic = 6
level = 7
itemOrder = 8
notes = 9

# Inventory array
inventory = np.array([
    ("Treant-Heart Staff",4,1,"Carrying",True,"","",0,0,"<em>Magic weapon (quarterstaff), rare (requires attunement)</em><br><br>This magical quarterstaff has been imbued with the heart of a treant, giving it many powers. As an action, an attuned wielder of the staff can speak one of the Sylvan command words to change the staff's form:<br><ul><li><b>Ai.</b> 3 feet in length. While in this form, it can be used as a magic club with a +2 bonus to attack and damage rolls.</li><li><b>Sanya.</b> 6 feet in length. While in this form, it can be used as a magic quarterstaff with a +1 bonus to attack and damage rolls.</li><li><b>An.</b> 12 feet in length. While in this form, it can be used as a special magic quarterstaff with the reach property. In this form, one-handed attacks with the staff have disadvantage.</li></ul><p>An attuned user can access the staff's innate magical properties. The staff has a maximum number of charges equal to your proficiency bonus. At dawn, it regains a number of charges equal to half your proficiency bonus (rounded up).<br><br><b>Spells.</b> You can use an action to expend 1 or more of the staff's charges to cast one of the following spells from it, using Wisdom as your spellcasting ability: <a target='_blank' href='https://www.dndbeyond.com/spells/animal-friendship'>animal friendship</a> (1 charge), <a target='_blank' href='https://www.dndbeyond.com/spells/awaken'>awaken</a> (5 charges), <a target='_blank' href='https://www.dndbeyond.com/spells/barkskin'>barkskin</a> (2 charges), <a target='_blank' href='https://www.dndbeyond.com/spells/locate-animals-or-plants'>locate animals or plants</a> (2 charges), <a target='_blank' href='https://www.dndbeyond.com/spells/speak-with-animals'>speak with animals</a> (1 charge), <a target='_blank' href='https://www.dndbeyond.com/spells/speak-with-plants'>speak with plants</a> (3 charges), or <a target='_blank' href='https://www.dndbeyond.com/spells/wall-of-thorns'>wall of thorns</a> (6 charges).<br><br><b>Tree Form.</b> You can use an action to plant one end of the staff in fertile earth and expend 1 charge to transform the staff into a healthy tree. The tree is 60 feet tall and has a 5-foot-diameter trunk, and its branches at the top spread out in a 20-foot radius. If there is not enough space for the tree to grow to its full dimensions, then the transformation fails, and the action and charge are both wasted. The tree appears ordinary but radiates a faint aura of transmutation magic if targeted by detect magic. While touching the tree and using another action to speak its command word (sanya), you return the staff to its normal form. Any creature in the tree falls when it reverts to a staff.</p>"),
    ("Backpack",5,1,"Carrying",True,"30","",0,0,"A backpack is a leather pack carried on the back, typically with straps to secure it. A backpack can hold 1 cubic foot/ 30 pounds of gear.<br><br>You can also strap items, such as a bedroll or a coil of rope, to the outside of a backpack."),
    
    ("Boots of Elvenkind",2,1,"Wearing",True,"","",0,0,"While you wear these boots, your steps make no sound, regardless of the surface you are moving across. You also have advantage on Dexterity (Stealth) checks that rely on moving silently."),
    ("Cloak of Elvenkind",4,1,"Wearing",True,"","",0,0,"While you wear this cloak with its hood up, Wisdom (Perception) checks made to see you have disadvantage, and you have advantage on Dexterity (Stealth) checks made to hide, as the cloak's color shifts to camouflage you. Pulling the hood up or down requires an action."),
    ("Clothes, Mtawa robes",4,1,"Wearing",True,"","",0,0,"These are simple traditional robes of the Mtawa. Holsters for two flasks and 10 darts, as well as other things (pouches, Shanga beads) may be tied to the Holster in belt."),
    #("Winter cloak",8,1,"Wearing",True,"","",0,0,"This heavy black cloak keeps the wearer warm in wintery weather.tal"),
    #("Winter hat",0.5,1,"Wearing",True,"","",0,0,"This dark purple hat with a pom-pom on top was crocheted for Kisha by Karen."),
    ("Amani Verig Pendant",0,1,"Wearing",True,"","",0,0,"On a string hangs a smooth stone with a simple symbol carved into it.<br><br><img src='images/amani_varig_pendant.png'/>"),
    ("Shanga Beads",0,1,"Wearing",True,"","",0,0,"Twenty hand-painted wooden counting beads are attached at one end to a hand-woven string. These are used in the daily Nidhamu ritual, and are otherwise tied at the waist."),
    
    ("Dagger (+2)",1,1,"On Belt",True,"","",0,0,"Ranged attack (20ft./60ft.): <b>1d4+4 piercing</b>"),
    ("Darts",0.25,10,"On Belt",True,"","",0,0,"Ranged attack (20ft./60ft.): <b>1d4+4 piercing</b>"),
    ("Wand of Web",0,1,"On Belt",True,"","m",0,0,"Charges left: <b>1</b><br><br>This wand has 7 charges. While holding it, you can use an action to expend 1 of its charges to cast the <a target='_blank' href='https://www.dndbeyond.com/spells/web'>web</a> spell (save DC 15) from it.<br><br>If you expend the wand's last charge, roll a d20. On a 1, the wand crumbles into ashes and is destroyed."),
    ("Healer's Kit",3,1,"On Belt",True,"","",0,0,"This kit is a leather pouch containing bandages, salves, and splints. The kit has ten uses total. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check.<br><br>As part of a long rest, you can use your Cook's Utensils to recharge a Healer's Kit by 1d4+1 charges. You must cook a meal to do this. A number times between periods of downtime equal to Wisdom score - 10 + Proficiency (9), you can do one of the following with a Healer's Kit that you've charged up by cooking:<ul><li>Spend 1 charge of Healer's Kit as a bonus action to stabilize someone.</li><li>Spend 2 charges of Healer's Kit to produce the effects of Cure Wounds as a first level spell, using your Wisdom modifier.</li><li>Spend 3 charges of Healer's Kit to produce the effects of Lesser Restoration.</li></ul><p>These spells don't count as Casting a Spell: it's not magic, just good food. You recharge a use of this feature by spending a week working at the Curry Kitchen or Sally's Soup Kitchen.</p>"),
    ("Heward's Handy Spice Pouch",0,1,"On Belt",True,"","m",0,0,"This belt pouch appears empty and has 10 charges. While holding the pouch, you can use an action to expend 1 of its charges, speak the name of any nonmagical food seasoning (such as salt, pepper, saffron, or cilantro), and remove a pinch of the desired seasoning from the pouch. A pinch is enough to season a single meal. The pouch regains 1d6 + 4 expended charges daily at dawn.<br><br><img src='images/spice_pouch.png'/>"),
    #("Poison, Basic (vial)",0,1,"On Belt",True,"","",0,0,"You can use the poison in this metal vial to coat one slashing or piercing weapon or up to three pieces of ammunition. Applying the poison takes an action. A creature hit by the poisoned weapon or ammunition must make a DC 10 Constitution saving throw or take 1d4 poison damage. Once applied, the poison retains potency for 1 minute before drying."),
    ("Potion of Healing",0.5,2,"On Belt",True,"","m",0,0,"A character who drinks the magical red fluid in this vial regains 2d4 + 2 hit points. Drinking or administering a potion takes an action.<br><br><img src='images/potion_of_healing.png'/>"),
    
    ("Coin Pouch",1 + 0.02*np.sum(money),1,"On Belt",True,"","",0,0,f"This cloth pouch can hold 1/5 cubic foot/6 pounds of coins. Currently it is holding {money[0]} gp, {money[1]} sp, and {money[2]} cp (coin weight of {0.02*np.sum(money)} lb.)."),
    ("Cook's Utensils",8,1,"Backpack",True,"","",0,0,"Cook's utensils include a metal pot, knives, forks, a stirring spoon, and a ladle. Proficiency with Cook's Utensils lets you add your proficiency bonus to any ability checks you make using these tools.<br><br><img src='images/cooks_utensils.png'/>"),
    ("Mess Kit",1,1,"Backpack",True,"","",0,0,"This tin box contains a cup and simple cutlery. The box clamps together, and one side can be used as a cooking pan and the other as a plate or shallow bowl."),
    ("Oil (bottle)",1,1,"Backpack",True,"","",0,0,"This metal tankard holds 1 pint of oil. As an action, you can splash the oil in this flask onto a creature within 5 feet of you. Make a ranged attack against a target creature or object, treating the oil as an improvised weapon. On a hit, the target is covered in oil. If the target takes any fire damage before the oil dries (after 1 minute), the target takes an additional 5 fire damage from the burning oil. You can also pour a flask of oil on the ground to cover a 5-foot-square area, provided that the surface is level. If lit, the oil burns for 2 rounds and deals 5 fire damage to any creature that enters the area or ends its turn in the area. A creature can take this damage only once per turn."),
    ("Honey (jar)",1,1,"Backpack",True,"","",0,0,"A ceramic jar filled with about 8 ounces of delicious honey. The jar has a protective holster."),
    #("Empty Jar",1,1,"Backpack",True,"","",0,0,"A ceramic jar which used to be filled with honey. It can hold 8 ounces. The jar has a protective holster."),
    ("Nuts",0.5,1,"Backpack",True,"","",0,0,"This pouch is filled with a mixture of walnuts, hazelnuts, and chestnuts."),
    ("Dried Fruit",0.5,1,"Backpack",True,"","",0,0,"This pouch is filled with dried cranberries and blueberries."),
    ("Tinderbox",1,1,"Backpack",True,"","",0,0,"This small container holds flint, fire steel, and tinder (usually dry cloth soaked in light oil) used to kindle a fire. Using it to light a torch -- or anything else with abundant, exposed fuel -- takes an action. Lighting any other fire takes 1 minute."),
    ("Torch",1,1,"Backpack",True,"","",0,0,"A torch burns for 1 hour, providing bright light in a 20-foot radius and dim light for an additional 20 feet. If you make a melee attack with a burning torch and hit, it deals 1 fire damage."),
    ("Waterskin",5,1,"Backpack",True,"","",0,0,"A waterskin can hold 4 pints of liquid."),
    
    ("Bedroll",7,1,"On Backpack",True,"","",0,0,"You never know where you're going to sleep, and a bedroll helps you get better sleep in a hayloft or on the cold ground. A bedroll consists of bedding and a blanket thin enough to be rolled up and tied. In an emergency, it can double as a stretcher."),
    ("Rope with a Grappling Hook",5,1,"On Backpack",True,"","",0,0,"Silk rope has 2 hit points and can be burst with a DC 17 Strength check. This rope is 50 feet long and has a grappling hook tied to one end, which can secure the rope to a battlement, window ledge, tree limb, or other protrusion."),
    
    ("Alchemy Jug",12,1,"Wildcat Tower",False,"","m",0,0,"This ceramic jug appears to be able to hold a gallon of liquid and weighs 12 pounds whether full or empty. Sloshing sounds can be heard from within the jug when it is shaken, even if the jug is empty.<br><br>You can use an action and name one liquid from the table below to cause the jug to produce the chosen liquid. Afterward, you can uncork the jug as an action and pour that liquid out, up to 2 gallons per minute. The maximum amount of liquid the jug can produce depends on the liquid you named.<br><br>Once the jug starts producing a liquid, it can't produce a different one, or more of one that has reached its maximum, until the next dawn.<table class='itemNotesTable'><tr><th>Liquid</th><th>Max Amount</th></tr><tr><td>Acid</td><td>8 ounces</td></tr><tr><td>Basic poison</td><td>1/2 ounce</td></tr><tr><td>Beer</td><td>4 gallons</td></tr><tr><td>Honey</td><td>1 gallon</td></tr><tr><td>Maynnaise</td><td>2 gallons</td></tr><tr><td>Oil</td><td>1 quart</td></tr><tr><td>Vinegar</td><td>2 gallons</td></tr><tr><td>Water, fresh</td><td>8 gallons</td></tr><tr><td>Water, salt</td><td>12 gallons</td></tr><tr><td>Wine</td><td>1 gallon</td></tr></table><br><img src='images/alchemy_jug.png'/>"),    
    ("Cook's Utensils (home set)",8,1,"Wildcat Tower",False,"","",0,0,"Cook's utensils include a metal pot, knives, forks, a stirring spoon, and a ladle. Proficiency with Cook's Utensils lets you add your proficiency bonus to any ability checks you make using these tools.<br><br><img src='images/cooks_utensils.png'/>"),
    ("Rice (sack)",4,1,"Wildcat Tower",False,"","",0,0,"This sack holds 4 pounds (10 cups) of wild rice. Each cup of uncooked wild rice expands to about 3.5 cups when cooked.<br><br><img src='images/rice.png'/>"),
    ("Herbalism Kit",3,1,"Wildcat Tower",False,"","",0,0,"This kit contains a variety of instruments such as clippers, mortar and pestle, and pouches and vials used by herbalists to create remedies and potions. Proficiency with this kit lets you add your proficiency bonus to any ability checks you make to identify or apply herbs. Also, proficiency with this kit is required to create antitoxin and any potion of healing."),
    ("Poisoner's Kit",2,1,"Wildcat Tower",False,"","",0,0,"A poisoner's kit includes the vials, chemicals, and other equipment necessary for the creation of poisons. Proficiency with this kit lets you add your proficiency bonus to any ability checks you make to craft or use poisons."),
    ("Journal",5,1,"Wildcat Tower",False,"","",0,0,"This journal contains Kisha's written record of the journey portion of her adept defense, essentially her adventures with the Wildcats since leaving Luostari. Most pages with writing have been filled with small, neat cursive and are written in Common. The inside cover says in Elivsh, Common and Dwarvish:<br><br><img src='images/journal_first_page.png'/>"),
    ("Orange Scale Medal",0,1,"Wildcat Tower",False,"","",0,0,"Awarded by Lucretia, an ancient Roman orange dragon, for saving Bakke and the Empire at large from Cornelia's devastation orbs.<br><br><img src='images/scale_orange.png'/>"),
    ("Yellow Scale Medal",0,1,"Wildcat Tower",False,"","",0,0,"Awarded by the govenor of Bakke for saving Bakke and the Empire at large from Cornelia's devastation orbs.<br><br><img src='images/scale_yellow.png'/>"),
    ])


# ============================================================================

def is_in_container(item, container):
    """
    IN: item is row of inventory array, container is a string
    OUT: returns true if item is in container, checks two levels
    """
    # Get list of objects with this container as location
    objs_in_container = inventory[inventory[:,location] == container]
    objs_in_container = objs_in_container[:,name].tolist()

    # Check if item is directly inside of container
    if item[name] in objs_in_container:
        return True

    # Check if item is in another item inside of container
    elif item[location] in objs_in_container:
        return True

    # Otherwise return false
    else:
        return False


def item_index(item, array):
    """
    IN: name of item (string), inventory array
    OUT: items index in inventory array
    """
    item_names = array[:,name]
    return np.argwhere(item_names==item)[0,0]


# ============================================================================
# Adjust table info for carrying backpack w/ or w/out rope and coin pouch

# If not carrying backpack, set carrying to false for appropriate items
if not carryingBackpack:
    for iItem in inventory:
        # nothing carried that is in backpack
        if is_in_container(iItem, 'Backpack'):
            iItem[carrying] = False
        # nothing carried strapped to backpack
        elif iItem[location] == 'On Backpack':
            iItem[carrying] = False
            iItem[location] = backpack_location + ', on Backpack'
        # backpack not carried
        elif iItem[name] == 'Backpack':
            iItem[carrying] = False
    # Set new location for backpack
    backpack_index = item_index('Backpack', inventory)
    inventory[backpack_index,location] = backpack_location

    # If 'wearing' rope while not carrying backpack
    if carryingRopeWOutBackpack:
        # find rope in inventory
        rope_index = item_index('Rope with a Grappling Hook', inventory)
        # set carrying to true, set location to Wearing
        inventory[rope_index][carrying] = True
        inventory[rope_index][location] = 'Wearing'

    # If carrying coins while not carrying backpack
    if carryingCoinsWOutBackpack:
        # find rope in inventory
        rope_index = item_index('Coin Pouch', inventory)
        # set carrying to true, set location to Wearing
        inventory[rope_index][carrying] = True
        inventory[rope_index][location] = 'On Belt'

# Generate list of carried equipment and other holdings
equipment = inventory[inventory[:,carrying] == 'True']
otherHoldings = inventory[inventory[:,carrying] == 'False']

# ============================================================================
# Sort carried equipment

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
itemOrder_list = np.array([int(i) for i in equipment[:,itemOrder]])   # makes list of strings into list of ints
equipment_sort = equipment[itemOrder_list.argsort()]


# ============================================================================
# Sort other holdings

# List of unique locations
locations_oh = np.unique(otherHoldings[:,location])

# Loop through, organize items in order based on nested containers
# loop through locations
for iLoc in locations_oh:
    # if location is not itself an object, print it
    if iLoc not in otherHoldings[:,name]:
        # go through location's items
        for iItem in otherHoldings[otherHoldings[:,location] == iLoc]:
            # if location's item is not another location, print it
            if iItem[name] not in locations_oh:
                otherHoldings[otherHoldings[:,name]==iItem[name],level] = 1
                count += 1
                otherHoldings[otherHoldings[:,name]==iItem[name],itemOrder] = count
            # if location's item IS another location (loc2), print it with its items...
            else:
                loc2 = iItem[name]
                otherHoldings[otherHoldings[:,name]==iItem[name],level] = 1
                count += 1
                otherHoldings[otherHoldings[:,name]==iItem[name],itemOrder] = count
                # loop through loc2's items
                for iItem2 in otherHoldings[otherHoldings[:,location]==loc2]:
                    # if loc2's item is not another location, print it
                    if iItem2[name] not in locations_oh:
                        otherHoldings[otherHoldings[:,name]==iItem2[name],level] = 2
                        count += 1
                        otherHoldings[otherHoldings[:,name]==iItem2[name],itemOrder] = count
                    # if loc2's item IS another location (loc3), print it with its items
                    else:
                        loc3 = iItem2[name]
                        otherHoldings[otherHoldings[:,name]==iItem2[name],level] = 2
                        count += 1
                        otherHoldings[otherHoldings[:,name]==iItem2[name],itemOrder] = count
                        # loop through loc3's items and print all
                        for iItem3 in otherHoldings[otherHoldings[:,location]==loc3]:
                            otherHoldings[otherHoldings[:,name]==iItem3[name],level] = 3
                            count += 1
                            otherHoldings[otherHoldings[:,name]==iItem3[name],itemOrder] = count


# Sort items in order set in above series of loops
itemOrder_list = np.array([int(i) for i in otherHoldings[:,itemOrder]])   # makes list of strings into list of ints
otherHoldings_sort = otherHoldings[itemOrder_list.argsort()]


# ============================================================================
# WRITE HTML FILE

# Write standard (non-container) item to HTML table string
def writeItem(item):
    # Add class if magic item
    str = '\t<table><tr class="level'+item[level]+'" id="item'+item[itemOrder]+'" onclick='+"'"+'$("#item'+item[itemOrder]+'_notes").slideToggle();'+"'"+'>'
    
    # Weight of item
    item_weight = float(item[weight]) * float(item[quantity])
    item_weight_str = '%.1f' % item_weight
    str = str + '<td class="itemName">'+item[name]+'</td><td class="itemWeight">'+item_weight_str+' lb.</td><td class="itemQuantity">'+item[quantity]+'</td><td class="itemLocation">'+item[location]+'</td></tr></table>\n'
    
    # div for item notes
    str = str + '\t\t<div class="itemNotes" id="item'+item[itemOrder]+'_notes"><p>'+item[notes]+'</p></div>'
    return str


# Write container item to HTML table string
def writeContainer(item_container, container_num):
    # Calculate contained weight
    contained_weight = 0
    for iItem in equipment:
        if is_in_container(iItem,item_container[name]):
            iItem_weight = float(iItem[weight]) * float(iItem[quantity])
            contained_weight += iItem_weight

    weight_str = '%.1f' % float(item_container[weight])
    str = '<table><tr class="level'+item_container[level]+'" id="item'+item_container[itemOrder]+'" id="container'+repr(container_num)+'" onclick='+"'"+'$("#container'+repr(container_num)+'_contents").slideToggle();$("#item'+item_container[itemOrder]+'_showDescription").slideToggle();if(("#item'+item_container[itemOrder]+'_notes:visible").length!=0){$("#item'+item_container[itemOrder]+'_notes").slideUp();}'+"'"+'>'
    
    # Add warning symbol if container is over capacity
    if contained_weight > float(item_container[container_capacity]):
        str = str + '<td class="itemName">&#10071; &#9734; '+item_container[name]+' <em>[container]</em></td><td class="itemWeight">'+weight_str+' lb.</td><td class="itemQuantity">'+'--'+'</td><td class="itemLocation">'+item_container[location]+'</td></tr></table>'
    else:
        str = str + '<td class="itemName">&#9734; '+item_container[name]+' <em>[container]</em></td><td class="itemWeight">'+weight_str+' lb.</td><td class="itemQuantity">'+'--'+'</td><td class="itemLocation">'+item_container[location]+'</td></tr></table>'
    
    # div for "Show description"
    str = str + '\t\t<div class="showDescription" id="item'+item_container[itemOrder]+'_showDescription" onclick='+"'"+'$("#item'+item_container[itemOrder]+'_notes").slideToggle();'+"'"+'><p>Toggle container description</p></div>'
    # div for item notes
    str = str + '\t\t<div class="itemNotes" id="item'+item_container[itemOrder]+'_notes">'
    # option to close container description
    contained_weight_str = '%.1f' % contained_weight
    str = str + '<p>Contains '+contained_weight_str+' lb. of items (max: '+item_container[container_capacity]+' lb.)</p>'
    str = str + '<p>'+item_container[notes]+'</p></div>'
    return str


# ----------------------------------------
# head of HTML file
html = open('index.html','w')
html.write('<!DOCTYPE html>\n<html>\n<head>\n\t<title>Kisha'+"'"+'s Equipment</title>\n\n\t<link rel="stylesheet" type="text/css" href="style.css">\n\n\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n\t<script src="script.js"></script>\n</head>\n<body>\n\n')

# Add portrait of Kisha
html.write('<img id="kisha" src="images/kisha.png"/>\n')

# Total weight carried and money
total_weight_carried = 0
for iItem in equipment_sort:
    if not is_in_container(iItem, 'Bag of Holding'):
        total_weight_carried += float(iItem[weight]) * float(iItem[quantity])
html.write('<div id="money_area"><div>\n')
html.write('<p id="weightCarried">Weight carried: {0:.1f}</p>\n'.format(total_weight_carried))
if total_weight_carried < (15*8): html.write('<p id="encumbrance">Unencumbered</p>\n\n')
html.write('<p id="money"><b>Gold:</b> '+repr(money[0])+', <b>Silver:</b> '+repr(money[1])+', <b>Copper:</b> '+repr(money[2])+'</p>\n')
html.write('</div></div>\n\n')


# ----------------------------------------
# HTML table of carried equipment
html.write('<div id="equipment"><div><table><tr><th class="Name">Item</th><th class="Weight">Weight</th><th class="Quantity">Quantity</th><th class="Location">Location</th></tr></table>\n')

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
html.write('</div></div>\n\n')


# ----------------------------------------
# HTML table of other holdings
html.write('<div id="other_holdings"><div><table><tr><th class="Name">Item</th><th class="Weight">Weight</th><th class="Quantity">Quantity</th><th class="Location">Location</th></tr></table>\n')

for i,iItem in enumerate(otherHoldings_sort):

    # check if item is first level
    if iItem[level] == '1':
        if iItem[name] in locations_oh:
            # add id of container# to tr, write line
            container_num += 1
            str = writeContainer(iItem,container_num)
            html.write('\t'+str+'\n')

            # made div for container level 1 contents
            html.write('\t<div id="container'+repr(container_num)+'_contents">\n')
            count = i+1;
            contained_item = otherHoldings_sort[count]
            while contained_item[level] == '2':

                if contained_item[name] in locations_oh:    # deal with container (level 2) inside container (level 1)
                    # add id of container# to tr
                    container_num += 1
                    str = writeContainer(contained_item,container_num)
                    html.write('\t\t'+str+'\n')

                    # make div for container level 2 contents
                    html.write('\t\t<div id="container'+repr(container_num)+'_contents">\n')
                    count += 1
                    contained_item = otherHoldings_sort[count]

                    while contained_item[level] == '3': # write items contained in container level 2
                        str = writeItem(contained_item)
                        html.write('\t\t'+str+'\n')

                        count += 1
                        contained_item = otherHoldings_sort[count]

                    # close div for container level 2 contents
                    html.write('\t\t</div>\n')

                else:   # write items contained in container level 1
                    str = writeItem(contained_item)
                    html.write('\t'+str+'\n')

                    count += 1
                    contained_item = otherHoldings_sort[count]

            # close dive for container level 1 contents
            html.write('\t</div>\n')

        else:   # write items non-contained and non-container items
            str = writeItem(iItem)
            html.write(str+'\n')
html.write('</div></div>\n\n')


# ----------------------------------------
# finish HTML file
html.write('\n\n</body>\n</html>')
html.close()
