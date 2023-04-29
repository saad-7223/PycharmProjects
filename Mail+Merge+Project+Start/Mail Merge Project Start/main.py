placeholder = "[name]"
counter = 0
with open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()
    for name in names:
        new_name = name.strip()
        new_letter = letter.replace(placeholder, new_name)
        with open(f"./Output/ReadyToSend/letter{counter}.txt", mode="w") as f:
            f.write(new_letter)
        counter += 1
