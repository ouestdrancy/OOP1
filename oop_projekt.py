from Bankkonto import *

imbus = BankKonto(1000, "imbus")
Köln = BankKonto(2000, "Köln")

imbus.getBalance()
Köln.getBalance()

Köln.anlage(500)

imbus.auszahlung(10000)
imbus.auszahlung(10)

imbus.überweisung(100, Köln)

Jim = Zinskonto(1000, "Jim")
Jim.getBalance()
Jim.anlage(100)
Jim.überweisung(100, imbus)
Blitz = SparKonto(1000, "Blitz")
Blitz.getBalance()
Blitz.anlage(100)
Blitz.überweisung(1000, Köln)