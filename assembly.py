f = open ('/tmp/assemble','r')
l = f.readlines()
i=0
while(i<len(l)):
 s = l[i].rstrip()
 print s
 i=i+1


