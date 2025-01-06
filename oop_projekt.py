from Bankkonto import *

## Konto Eröffnung
imbus = BankKonto(1000, "imbus")
Köln = BankKonto(2000, "Köln")

# expect balance to be 1000 and 2000 
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


# Unit tests 
def test_auszahlung_fail(capsys):
    imbus = BankKonto(1000, "imbus")
    imbus.auszahlung(10000)
    captured = capsys.readouterr()
    assert "Auszahlung unterbrochen" in captured.out 

def test_auszahlung_succeed():
    imbus = BankKonto(1000, "imbus")
    imbus.auszahlung(500)
    assert False

def test_transfer_succeed():
    imbus = BankKonto(1000, "imbus")
    Köln = BankKonto(2000, "Köln")
    imbus.überweisung(100, Köln)

    #TODO: assert success case. 
def test_transfer_fail():
    imbus = BankKonto(1000, "imbus")
    Köln = BankKonto(2000, "Köln")
    imbus.überweisung(10000, Köln)

    ## expect transfer to fail. assert failure message captured in output.
    # assert "Überweisung unterbrochen" in captured.out

def test_get_balance():
    Jim = Zinskonto(1000, "Jim")
    Jim.getBalance()
    #TODO: expect balance of 1000 printed. 



