nightelf_classes = ['Hunter', 'Druid', 'Warrior', 'Monk', 'Priest', 'Mage', 'Death Knight']

for i in nightelf_classes:
	print(i.upper())


print("My favorite class is " + nightelf_classes[0] + ", but I also enjoy playing " + nightelf_classes[6] + ".")

print("\nWhat's your favorite class?")

wow_class = input("\nEnter a class: ")
 
if wow_class == 'Hunter':
    print("Me too!")
    
elif wow_class == 'Druid':
    print("Druids are so versatile.")

elif wow_class == 'Warrior':
    print("Warriors have the nicest looking gear sets.")
    
elif wow_class == 'Monk':
    print("Monks have the best class hall.")
    
elif wow_class == 'Priest':
    print("Priests are fun in PVP.")

elif wow_class == 'Mage':
    print("Mages are OP.")

elif wow_class == 'Death Knight':
    print("Death Knights are my favorite lore-wise.")

else:
    print("Sorry, that's not one of the available class options")
    
    
