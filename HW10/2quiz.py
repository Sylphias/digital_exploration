from libdw import sm

class RunOfOddNumbers(sm.SM):
   startState =  0
   def getNextValues(self, state, inp):
      if state == 0:
        if inp %2 != 0: return (1, 1)
        else: return (state,0)
      elif state >=1:
        if inp%2 != 0: return (state+1,state+1)
        else: return (0, 0)

m = RunOfOddNumbers()
print [2,1,8,4,3,7,6,5,8,7,5,9,7]
print m.transduce([2,1,8,4,3,7,6,5,8,7,5,9,7])