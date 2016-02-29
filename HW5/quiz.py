def sumList(inp):
  sum_list =[]
  for x in inp:
    sum_sublist = 0
    for y in range(len(x)):
      sum_sublist += x[y]
    sum_list+=[sum_sublist]
  return sum_list

print sumList([[100],[1,7],[8,0,-1],[2]])
