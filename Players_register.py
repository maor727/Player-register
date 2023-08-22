from Players_class import Players

register_name = input("What is your name?").capitalize()
register_country = input("Where are you from?").capitalize()
register_rank = str(input("What rank are you?"))

player1 = Players(register_name, register_country, register_rank)

print(f'Name: {player1.name}\nCountry: {player1.country}\nRank: {player1.rank}')