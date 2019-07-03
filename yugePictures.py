import subprocess
from PIL import Image

def sad():
	Image.open("/Users/rambo/Pictures/trumpSad.jpeg").show()
def happy():
	Image.open("/Users/rambo/Pictures/trumpHappy.png").show()
def disgust():
	Image.open('Pictures/trumpDisgusting.jpeg').show()
def angry():
	Image.open('Pictures/trumpAngry.jpeg').show()
def fear():
	Image.open('Pictures/trumpFear.jpeg').show()

if __name__=='__main__':
	sad()
	happy()
	disgust()
	angry()
	fear()
