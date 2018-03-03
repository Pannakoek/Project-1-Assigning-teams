# assigning teams
# import the module that makes it able to read csv
import csv


def read_file():
    # create to list to divide the experienced player from the not experienced
    players_with_experience = []
    players_with_no_experience = []

    # open the file and put them in the right list
    with open("soccer_players.csv", newline='') as file:
        cvs_reader = csv.DictReader(file, delimiter=',')
        rows = list(cvs_reader)
        for row in rows:
            if row['Soccer Experience'] == 'YES':
                players_with_experience.append(row)
            else:
                players_with_no_experience.append(row)

    # return the variable to use later in the file
    return players_with_experience, players_with_no_experience


def create_teams():
    # unpack the variable of the previous function
    experienced_players, not_experienced_players = read_file()

    # create list for the specific teams and a counter
    count = 0
    sharks_team = []
    dragons_team = []
    raptors_team = []

    # divide the experienced players in a even teams
    for player in experienced_players:
        if count in range(0, 9, 3):
            sharks_team.append(player)
            count += 1
        elif count in range(1, 9, 3):
            dragons_team.append(player)
            count += 1
        elif count in range(2, 9, 3):
            raptors_team.append(player)
            count += 1

    count = 0

    # do the same for the not experienced players
    for player in not_experienced_players:
        if count in range(0, 9, 3):
            sharks_team.append(player)
            count += 1
        elif count in range(1, 9, 3):
            dragons_team.append(player)
            count += 1
        elif count in range(2, 9, 3):
            raptors_team.append(player)
            count += 1

    # create the file with the created teams
    with open("teams.txt", "w") as team_file:
        team_file.write("Sharks\n")
        # print every child that is in the shark team
        for team in sharks_team:
            team_file.write(f"{team['Name']}, {team['Soccer Experience']}, {team['Guardian Name(s)']} \n")

        team_file.write("\n")

        team_file.write("Dragons\n")
        # print every child that is in the dragon team
        for team in dragons_team:
            team_file.write(f"{team['Name']}, {team['Soccer Experience']}, {team['Guardian Name(s)']} \n")

        team_file.write("\n")

        team_file.write("Raptors\n")
        # print every child that is in the raptor team
        for team in raptors_team:
            team_file.write(f"{team['Name']}, {team['Soccer Experience']}, {team['Guardian Name(s)']} \n")

    # close the file
    team_file.close()

    # pack the teams with the for using in write_letter()
    return sharks_team, dragons_team, raptors_team


def write_letter():
    # unpack the team players for the specific teams
    sharks_team, dragons_team, raptors_team = create_teams()

    # create a list that has all the players
    all_players = []
    with open("soccer_players.csv", newline='') as file:
        cvs_reader = csv.DictReader(file, delimiter=',')
        rows = cvs_reader
        for row in rows:
            all_players.append(row)

    # get all the names of the players for the sharks
    list_name_sharks = []
    for selected_team in sharks_team:
        list_name_sharks.append(selected_team['Name'])

    # get all the names of the players for the dragons
    list_name_dragons = []
    for selected_team in dragons_team:
        list_name_dragons.append(selected_team['Name'])

    # get all the names of the players for the raptors
    list_name_raptors = []
    for selected_team in raptors_team:
        list_name_raptors.append(selected_team['Name'])

    # create a letter for every players guardian(s)
    for player_info in all_players:
        # create the file name with a _ instate of a space
        file_name = "_".join(player_info['Name'].split())
        # check what there team is
        if player_info['Name'] in list_name_sharks:
            the_team_they_play_for = "Sharks"
        elif player_info['Name'] in list_name_dragons:
            the_team_they_play_for = "Dragons"
        elif player_info['Name'] in list_name_raptors:
            the_team_they_play_for = "Raptors"

        # create for each player a letter with the players name.txt
        with open(f"{file_name}.txt", 'w') as player_letter:
            player_letter.write(f"Dear {player_info['Guardian Name(s)']},\n\n")
            player_letter.write(f"{player_info['Name']} is selected to play for {the_team_they_play_for}.\n\n")
            player_letter.write(f"The first training will take place on March 31, 2018 at 1:00 PM. \n")
            player_letter.write(f"I hope you have informed me enough about this. \n"
                                f"If you have any questions, please let me know.\n\n")
            player_letter.write(f"Sincerely,")


# first load all the imports and than run the file
if __name__ == "__main__":
    read_file()
    create_teams()
    write_letter()
else:
    print("RIP no grade for me")
