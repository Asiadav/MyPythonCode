import random as r

adj = ['my','you are','adorable','beautiful','clean','drab','elegant','fancy','glamorous','handsome','long','magnificent','old-fashioned','plain','quaint','sparkling','ugliest','unsightly','wide-eyed','agreeable','brave','calm','delightful','eager','faithful','gentle','happy','soul','kind','lively','nice','obedient','proud','relieved','silly','thankful','victorious','witty','zealous', 'chilly','real','sweet']

verb = ['love','text','call','hug','miss','be','cry','adore']

noun = ['bug', 'me', 'you', 'mine', 'lungs', 'cheeks', 'hands','tables', 'people','legs', 'mate', 'friend', 'bird',  'plates', 'candy', 'jewelry', 'flowers','baby', 'love','heart','boy','girl','starvation']

oneLine = ['#love', 'You & me', 'XOXO','sure','one & only','crazy 4 U','sweat poo','love 2000 hogs yea','love U']


w = r.randrange(0,len(oneLine))
x = r.randrange(0,len(adj))
y = r.randrange(0,len(noun))
z = r.randrange(0,len(verb))

maybe = r.randrange(1,5)


if maybe > 2:
    thing = adj[x]+ ' ' + noun[y]
elif maybe == 2:
    thing = oneLine[w]
else:
    thing = verb[z] + ' ' + noun[y]


print(thing)