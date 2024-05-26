#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Intermediate/D24_Files/Mail Merge Project/Input/Names/invited_names.txt") as names:
    names = names.readlines()
    names_strip = []
    for n in names:
        n_strip = n.strip()
        names_strip.append(n_strip)

with open("Intermediate/D24_Files/Mail Merge Project/Input/Letters/starting_letter.txt") as initial_letter:
    letter_data = initial_letter.read()

for n in names_strip:
    new_letter = letter_data.replace("[name]", n)
    with open(f"Intermediate/D24_Files/Mail Merge Project/Output/ReadyToSend/letter_for_{n}.txt", mode="w") as op_file:
        op_file.write(new_letter)