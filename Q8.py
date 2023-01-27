class py_solution:
 def threeSum(self, lst):
     pos, neg, soln = [], [], []
     lst.sort()
     for _ in lst:
         if _ > 0:
             pos.append(_)
         else:
             neg.append(_)
     for i in neg:
         for j in pos:
             for k in range(len(pos)):
                 if i + j + pos[k] == 0:
                     z = (i, j, pos[k])
                     soln.append(z)

     for c in pos:
         for v in neg:
             for b in range(len(neg)):
                 if c + v + neg[b] == 0:
                     x = (c, v, neg[b])
                     soln.append(x)
     print(soln)
print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
