import pywhatkit

try:
	#pywhatkit.sendwhatsmsg("+524441062564", "Hello world", 18,10)
	pywhatkit.sendwhatmsg_instantly("+524445821580", "Prueba de python", 10, True,5)
	#pywhatkit.sendwhatmsg_to_group_instantly("HIsAlnmzmA4A0s9ea21mKJ", "Lleve su Promo 2x1", 10, True,3)
	print("Mensaje enviado")
except:
	print("Error")