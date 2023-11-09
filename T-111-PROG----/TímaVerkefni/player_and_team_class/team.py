class Team:
    def __init__(self, name) -> None:
        self.name = name
        self.players = []
        
        
    def __str__(self) -> str:
        ret = f"{self.name}:"

        for player in sorted(self.players, key=lambda p: p.goals, reverse=True):
            ret += f"\n\t{player}"

        return ret
    

    def add_player(self, player):
        self.players.append(player)

    def most_goals_player(self):
        return max(self.players, key=lambda p : p.goals)

    def __add__(self, other):
        new_team = Team(f"{self.name}+{other.name}")

        for player in self.players + other.players:
            new_team.add_player(player)

        return new_team
    