#given a list of time for different movie shows.
#find the minimum number of theatres required to be able to show all the movies
#hashing, dictionaries, skip list
x = []
l = []
n = int(input("no. of movies: "))
for i in range(n):
    a = list(map(int, input("movie start and end time").split()))
    x += [a]
x.sort()
j = 0
c = 1
l.append(x[0])
th = [l]
k = 0
print(th)
for i in range(n):
    if th[j][k][0]>x[i][0] or th[j][k][1]>x[i][1]:
        j += 1
        th[j][k] += [x]
    else:
        c += 1
        k += 1
        th[j][k] += [x]
print(c)
        

