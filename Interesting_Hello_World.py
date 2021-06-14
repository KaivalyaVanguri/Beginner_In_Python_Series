weights = [ 
   -73.0,  88.0, -11.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 
     0.0,   0.0,   0.0,  1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 
     0.0,   0.0,   0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 
     0.0,   0.0,   0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 
     0.0,   0.0,   0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 
     0.0,   0.0,   0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 
     0.0,   0.0,   0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  2.0, 
    77.2,   0.0,   0.0, 70.0,  0.0,  0.0, 69.0, 80.0,  0.0, 83.0, 
    13.0,  83.1,   0.0, 76.9,  0.0,  0.0,  0.0,  0.0, 79.9,  0.0, 
     1.0, -88.0,  80.0, 83.0, 77.0, 69.0,  2.0 
] 
pos, transition = 0, [ -1, 1 ] 
epsilon, delta = (.001, 0.2) 
feedback = [] 
while weights[pos]: 
   weight = abs(weights[pos]) 
   transition[0] = int(weight) + ( 
           2 ** 5 - 1 if weights[pos] >= 0 else -1) + ( 
           weight - int(weight) + delta > 1.0) 
   transition[1] = transition[0] if abs( 
   weight - int(weight) - delta) < epsilon else 0 
   feedback.extend(transition) 
   pos = int(weight) 
print(''.join(chr(val) for val in feedback), end='')
