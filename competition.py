def competition(tourneys, results):
  #evaluate each tourney, to select the winner based on the result
  # the winner of a tourney gets 3 points
    # initialize a scores dict
  scores = {}
    # initialize a winning team string 
  winningTeam = ''
  scores[winningTeam] = 0
    # evaluate winner
  for idx in range(len(tourneys)):
    res = results[idx]
    if res == 0:
      winner = tourneys[idx][1]
    elif res == 1:
      winner = tourneys[idx][0]
    # check if winner already in dict
    if winner not in scores:
      # no: add winner and assign points
      scores[winner] = 3
      # yes: #update winner points
    else:
      scores[winner] = scores[winner] + 3
    if scores[winner] > scores[winningTeam]:
      winningTeam = winner
    #update winninig team string with team that has the highest points

# result -> output the winning team based on highest points
  return winningTeam
    
 

if __name__ == '__main__':
  print(competition([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [1, 1, 1]))
