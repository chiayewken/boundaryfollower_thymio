from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from boxworld import thymio_world
from time import sleep
class MySMClass(sm.SM):
	start_state='finding'
	def get_next_values(self, state, inp):
		if inp.button_backward:
			return 'halt', io.Action(0,0)
		ground = inp.prox_ground.delta
		left = ground[0]
		right = ground[1]
		print(left,right)
	#####################################
		if state == 'finding':
			if left < 400 and right < 400:
				print('found, turning left')
				return 'found', io.Action(fv=0, rv=0.5)
			else:
				print('finding, straight')
				return 'finding', io.Action(fv=0.1, rv=0)
		elif state == 'found':
			if left >= 400 and right < 400:
				print('edge, straight')
				return 'edge', io.Action(fv=0.1,rv=0) 
			elif left < 400 and right < 400:
				print('found, turning left')
				return 'found',io.Action(fv=0,rv=0.5)
		elif state == 'edge':
			if left < 400 and right < 400:
				print('edge, turning left')
				return 'edge',io.Action(fv=0,rv=0.5)
			elif left >= 400 and right >= 400:
				print('edge, turning right')
				return 'edge',io.Action(fv=0,rv=-0.5)
			else:
				print('edge, straight')
				return 'edge',io.Action(fv=0.1,rv=0) 
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
