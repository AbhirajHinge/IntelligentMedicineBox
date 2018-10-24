from event_queue import EventQueue
from prescription_manager import PrescriptionManager
from timer import Timer
from time import sleep
#from notifier import Notifier
def main():
	event_queue=EventQueue(['presc_man','timeslot','print'])
	prescription_manager=PrescriptionManager(event_queue)
	timer=Timer(event_queue)
	print ("Initialisation Done")
	#notifier=Notifier()
	while(True):
	    event_queue.update()
	    sleep(1)
	del event_queue
	del prescription_manager
	del timer
	print ("Deletion Done")

main()
