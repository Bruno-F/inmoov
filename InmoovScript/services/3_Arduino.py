# ##############################################################################
# 								ARDUINO SERVICE FILE
# ##############################################################################


# ##############################################################################
# ARDUINO RELATED FUNCTIONS
# ##############################################################################


	
	
#function to check arduino & mrlcomm
def CheckArduinos(Card,Port,slave=0):
	#A RX/TX connection don't return 'arduino is connected', only mrlcomm version
	if slave!=0:
		Card.connect(slave,Port)
		sleep(1)
	else:
		Card.connect(Port)
	
	if not Card.isConnected() and slave==0:
		errorSpokenFunc('ArduinoNotConnected',Port)
		return False
	if Card.isConnected() or slave!=0:
		print "Mrlcomm version : ",Card.getBoardInfo().version," ( requiered ",MRLCOMM_VERSION," )"
		if Card.getBoardInfo().version!=MRLCOMM_VERSION:
			errorSpokenFunc('BadMrlcommVersion',Port)
		else:
			print "Arduino ",Port," OK"
			return True


	
	



    

