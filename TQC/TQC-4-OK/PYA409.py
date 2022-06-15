# TODO

vote_count=1
nami=0
chopper=0
null=0
while vote_count <=5:
  vote=eval(input())
  if vote==1:
    nami+=1
  elif vote==2:
    chopper+=1
  else:
    null+=1
  print("Total votes of No.1: Nami =  %d\nTotal votes of No.2: Chopper =  %d\nTotal null votes =  %d" %(nami,chopper,null))
  vote_count+=1

if nami>chopper:print("=> No.1 Nami won the election.")
elif nami<chopper:print("=> No.2 Chopper won the election.")
elif nami==chopper:print("=> No one won the election.")
"""
Total votes of No.1: Nami = _
Total votes of No.2: Chopper = _
Total null votes = _

=> No.1 Nami won the election.
=> No.2 Chopper won the election.
=> No one won the election.
"""
