GPP=g++
FLAGS=-c -pipe -O3 -g -funsafe-math-optimizations # -Wall -W
CC=$(GPP) $(FLAGS)
LK=$(GPP)
INC=
pn=sampleBinDumper

all:	$(pn)


$(pn):
	$(LK) $(INC) $(pn).cpp -o $(pn)

###############

clean:
	[ -f $(pn) ] && rm $(pn)
