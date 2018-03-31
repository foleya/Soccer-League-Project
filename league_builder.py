import csv
import random

def get_player_list(playercsv):
	#add player information (rows) from a csv file into a list
	with open(playercsv, newline ='') as playercsv:
		reader = csv.DictReader(playercsv)
		for row in reader:
			players.append(row)

def sort_players_by_experience(players):
	#sort each players into two lists: exp. and inexp.
	for player in players:
		if player['Soccer Experience'].lower() == 'yes':
			exp_players.append(player)
		else:
			inexp_players.append(player)

def build_teams(league):
	
	#shuffle lists of exp. and inexp. players
	random.shuffle(exp_players)
	random.shuffle(inexp_players)
				
	#calculate appropriate number of exp and and inexp players per team
	exp_player_num = len(exp_players)//len(league)
	inexp_player_num = len(inexp_players)//len(league)
	
	#distribute players evenly until none left
	while exp_players:
		for team in league:	
			league[team] += exp_players[0:exp_player_num]
			del exp_players[0:exp_player_num]
	while inexp_players:
		for team in league:
			league[team] += inexp_players[0:inexp_player_num]
			del inexp_players[0:inexp_player_num]

def write_roster(league):
	#for every team, write the team name and every player on that team (with additional info) to teams.txt
	with open('teams.txt', 'w') as teams:	
		for team in league:
			teams.write(team + '\n')
			for player in league[team]:
				info = []
				info.append(player['Name'])
				info.append(player['Soccer Experience'])
				info.append(player['Guardian Name(s)'])
				teams.write(', '.join(info) + '\n')
			teams.write('\n\n')

def write_welcome_emails(league):
	for team in league:
		for player in league[team]:
			
			#generate a filename for their welcome e-mail
			lc_name = player['Name'].lower()
			filename = '_'.join(lc_name.split()) + '.txt'
			
			#write their welcome email to txt file
			with open(filename, 'w') as welcome:
				welcome.write("Dear {},\n\nCongratulations! {} will be playing soccer for the {} this season!! Our first practice will be {}. We're looking forward to seeing you all then!".format(player['Guardian Name(s)'], player['Name'], team, first_practice))

if __name__ == '__main__':
	
	players = []
	exp_players = []
	inexp_players = []
	league = {'Dragons': [], 'Raptors': [], 'Sharks': []}
	first_practice = 'April 1st, 2018 at 2pm'
	
	#get list of players from csv file
	get_player_list('soccer_players.csv')
	
	#sort players into two lists: exp. and inexp.
	sort_players_by_experience(players)
	
	#build teams that draw evenly from exp. and inexp. player lists
	build_teams(league)

	#build team roster as txt file
	write_roster(league)
	
	#write welcome e-mails as txt files
	write_welcome_emails(league)
