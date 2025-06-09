class Player:

  def __init__(self,name,team):
    self.name = name
    self.xp = 1500
    self.team = team

  def introduce(self):
    print(f"안녕하세요, 제 이름은 {self.name}이고, 팀은 {self.team}입니다. 현재 경험치는 {self.xp}입니다.")


class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []
  def show_players(self):
    for player in self.players:
      player.introduce()

  def add_player(self,name):
    new_player = Player(name=name, team=self.team_name)
    self.players.append(new_player)
  def remove_player(self, name):
    for player in self.players:
      if player.name == name:
        self.players.remove(player)
        print(f"Player {name} has been removed from team {self.team_name}.")
        break
    else:
      print(f"Player {name} not found in team {self.team_name}.")
  def get_total_xp(self):
    total_xp = 0
    for player in self.players:
      total_xp += player.xp
    return print(f"Total XP for team {self.team_name}: {total_xp}")

nico = Player(name="nico", team="TEAM X")

lyne = Player(name="lyne", team="TEAM BLUE")



team_x = Team(team_name="TEAM X")

team_x.add_player("nico")
team_blue = Team(team_name="TEAM BLUE")
team_x.add_player("lyne")
team_x.get_total_xp()