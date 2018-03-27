from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from boxworld import thymio_world
from time import sleep
class MySMClass(sm.SM):
	start_state='start'
	def get_next_values(self, state, inp):
		if inp.button_backward:
			return 'halt', io.Action(0,0)
		ground = inp.prox_ground.delta
		left = ground[0]
		right = ground[1]
		print(left,right)
	#####################################
		if state == 'start':
			if left < 400 and right < 400:
				sleep(0.5)
				return 'found', io.Action(fv=0.1, rv=0)
			else:
				return 'start', io.Action(fv=0.1, rv=0)
		if state == 'found':
			if left >= 400 and right < 400:
				return 'wb', io.Action(fv=0,rv=0) 
			else:
				return 'found',io.Action(fv=0,rv=0.5)
		else:
			return 'start',io.Action(fv=0.1,rv=0)
	#########################################
	def done(self,state):
		if state=='halt':
			return True
		else:
			return False
MySM=MySMClass()
m=ThymioSMReal(MySM)
try:
	m.start()
except KeyboardInterrupt:
	m.stop()
