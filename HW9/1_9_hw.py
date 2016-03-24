from libdw import sm
class CM(sm.SM):
  startState = 0
  def getNextValues(self,state,inp):
    if inp == 50 and state == 0 :
      nextstate = 1
      return (nextstate,(50,"--", 0))
    elif inp == 50 and state == 1:
      nextstate = 0
      return (nextstate,(0,"coke", 0))
    elif inp == 100 and state == 0:
      nextstate = 0
      return (nextstate,(0,"coke", 0))
    elif inp == 100 and state == 1:
      nextstate = 0
      return (nextstate,(0,"coke", 50))
    elif inp != 100 or inp != 50:
      return (state,(0,"--", inp))
    else:
      nextstate = 0
      return (nextstate,(0,"--", 0))
c=CM()
c.start()
print c.step(50)
# (50, '--', 0)
print c.step(50)
# (0, 'coke', 0)
print c.step(100)
# (0, 'coke', 0)
print c.step(10)
# (0, '--', 10)
print c.step(50)
# (50, '--', 0)
print c.step(100)
# (0, 'coke', 50)
print c.step(10)
