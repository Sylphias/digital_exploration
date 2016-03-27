from libdw import sm
class CommentsSM(sm.SM):
    startState = 'not a comment'  # fix this

    def getNextValues(self, state, inp):
        if state == 'not a comment':
          if inp == "#":
            return ('is a comment','#')
          else:
            return ('not a comment', None)
        elif state == 'is a comment':
          if inp == "\n":
            return ('not a comment',None)
          else:
            return('is a comment',inp)

        pass

# str = 'def f(x): # comment\n   return 1'
# m = CommentsSM()
# print m.transduce(str)
# [None, None, None, None, None, None, None, None, None, None, 
# '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', 
# None, None, None, None, None, None, None, None, None, None, None, None]
class FirstWordSM(sm.SM):
    startState = 'searching for word'  # fix this

    def getNextValues(self, state, inp):
      if state == 'is first word':
        if inp == " ":
          return ('not first word',None)
        else:
          return ('is first word',inp)
      elif state == 'not first word':
        if inp == "\n":
          return ('searching for word',None)
        else:
          return('not first word',None)
      elif state == 'searching for word':
        if inp.isalnum() or inp == '#':
          return ('is first word', inp)
        else:
          return ('searching for word', None)
        pass
str = 'def f(x): # comment\n   return 1'
m = FirstWordSM()
print m.transduce(str)