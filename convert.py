import csv
# The name of the player is in the second column (index 1).
NAME_INDEX = 1
# The PER of the player is in the 10th column (index 9).
PER_INDEX = 9
COUNT = 15

with open('game_stats.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')

    # Initialize the counter and empty lists.
    character_count = 0
    names = []
    pers = []
    urls = []

    for row in csv_reader:
        if character_count == 0:
            character_count+=1
        elif character_count <= COUNT:
            names.append(row[NAME_INDEX])

            # The image file of the player is their name with no spaces or period and all lowercase.
            urls.append("https://sjanlassets.blob.core.windows.net/assets/" + row[NAME_INDEX].replace(" ","").replace(".","").lower()+".png")
            # The PER of the player is in the 10th row (at index 9).
            pers.append(row[PER_INDEX])

             # Increment the counter so we only get one set of data for each player.
            character_count += 1
        else:
            break
# w overwrites the file if there is anything
f = open("players.json", "w")

# opening bracket of JSON objet to the file
f.write("[\n")

# Iterate over all of the players.
for index in range(0,COUNT):
    # Write the opening bracket of the first player object to the file.
    f.write("\t{\n")

    # Write the name, PER, and image url, with their labels, to the file.
    f.write("\t\t\"name\": \""+names[index]+"\",\n")
    f.write("\t\t\"per\": \""+pers[index]+"\",\n")
    f.write("\t\t\"imgUrl\": \""+urls[index]+"\"\n")
    f.write("\t},\n")

# Write the opening bracket of the Yosemite Sam object to the file.
f.write("\t{\n")

# Write his name, PER (0), and image url, with the data labels, to the file.
f.write("\t\t\"name\": \"Yosemite Sam\",\n")
f.write("\t\t\"per\": \"0\",\n")
f.write("\t\t\"imgUrl\": \"https://sjanlassets.blob.core.windows.net/assets/yosemitesam.png\"\n")

# Since he is the last of the Tune Squad, don't include a comma after closing his object.
f.write("\t}\n")

# Write the closing bracket to the JSON object to the file.
f.write("]")

# Close the file.
f.close()