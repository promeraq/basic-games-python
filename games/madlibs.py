# 1. Ask user if wanna play
# 2. Read text file. Each line is a "madlib phrase".
# 3. Ask user for inputs
# 4. Replace ADJECTIVE, NOUN, ADVERB, or VERB from phrase with inputs
# 5. Print answer and save in another file
# 6. Ask if wanna play again¡

play = True

while play == True:
    answer = input("Do you want to play madlibs? (Y/N)")
    if answer == "N":
        play = False
        break

    file_name = "madlibs_phrases.txt"
    with open(file_name) as ml_file:    
        # We store each line of the file in a LIST called "lines" with the .readlines() method.
        lines = ml_file.readlines()
    
    for line in lines:
        print("Let's play!\n")
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        verb = input("Enter a verb: ")

        line = line.replace('ADJECTIVE', adjective)
        line = line.replace('NOUN', noun)
        line = line.replace('VERB', verb)

        new_file = "madlibs_answers.txt"
        with open(new_file, 'a') as file:
            file.write(line)

        print(line, '\n')
        keep_on = input("Do you wanna keep on playing madlibs? (Y/N)")
        if keep_on == "N":
            play = False
            break