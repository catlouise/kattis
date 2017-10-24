import sys
pieces = sys.stdin.readline().split()
addrm = [0,0,0,0,0,0]

#king
addrm[0] = str(1 - int(pieces[0]))
#queen
addrm[1] = str(1 - int(pieces[1]))  
#rooks
addrm[2] = str(2 - int(pieces[2]))
#bishops
addrm[3] = str(2 - int(pieces[3]))
#knights
addrm[4] = str(2 - int(pieces[4]))
#pawns
addrm[5] = str(8 - int(pieces[5]))

print(' '.join(addrm))  
