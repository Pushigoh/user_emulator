import subprocess
def click( xAxis, yAxis, flip = false ):
	#Flip simulates a backwards click
	if flip:
		xAxis = -xAxis
		yAxis = -yAxis
	subprocess.call(["xdotool", "mousemove", xAxis, yAxis])
	subprocess.call(["xdotool", "click", "1"]) #1 is left click
def saveClick (  ): 
