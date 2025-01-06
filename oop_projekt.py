from Bankkonto import *

# Kontoeröffnung
imbus = BankKonto(1000, "imbus")
Köln = BankKonto(2000, "Köln")

# balance sollte zwischen 1000 und 2000 sein
imbus.getBalance()
Köln.getBalance()

# Geldanlage
Köln.anlage(500)

# Auszahlung. Saldo geht runter
imbus.auszahlung(10000)
imbus.auszahlung(10)

# Überweisung von imbus an Köln
imbus.überweisung(100, Köln)

# Neue Kontoeröffnungen und Bankaktivitäten
Jim = Zinskonto(1000, "Jim")
Jim.überweisung(100, imbus)
Blitz = SparKonto(1000, "Blitz")
Blitz.getBalance()
Blitz.anlage(100)
Blitz.überweisung(1000, Köln)


