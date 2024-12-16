class BalanceException(Exception):
    pass
    
class BankKonto:
    def __init__(self, initialerBetrag, kontoName):
        self.saldo = initialerBetrag
        self.name = kontoName
        print(f"\nKonto '{self.name}' erstellt.\nSaldo = {self.saldo:.2f}€")

    def getBalance(self):
        print(f"\nKonto '{self.name}' Saldo = {self.saldo:.2f}€")

    def anlage(self, betrag):
        self.saldo = self.saldo + betrag
        print("\nAnlage erledigt.")
        self.getBalance()

    def viableTransaction(self, betrag):
        if self.saldo >= betrag:
            return
        else:
            raise BalanceException(
                f"\nSorry, Konto '{self.name}' hat nur ein Saldo von {self.saldo:.2f}€"
            )
        
    def auszahlung(self, betrag):
        try:
            self.viableTransaction(betrag)
            self.saldo = self.saldo - betrag
            print("\nAusahlung erledigt.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nAuszahlung unterbrochen: {error}')

    def überweisung(self, betrag, konto):
        try:
            print('\n**********\n\nÜberweisung beginnt..🚟')
            self.viableTransaction(betrag)
            self.auszahlung(betrag)
            konto.anlage(betrag)
            print('\nÜberweisung erfolgt! 😆\n\n**********')
        except BalanceException as error:
            print(f'\nÜberweisung unterbrochen😣 {error}')

class Zinskonto(BankKonto):
    def anlage(self, betrag):
        self.saldo = self.saldo + (betrag * 1.05)
        print("\nAnlage fertig.")
        self.getBalance()

class SparKonto(Zinskonto):
    def __init__(self, initialerBetrag, kontoName):
        super().__init__(initialerBetrag, kontoName)
        self.gebühr = 5
    def auszahlung(self, betrag):
        try:
            self.viableTransaction(betrag + self.gebühr)
            self.saldo = self.saldo - (betrag + self.gebühr)
            print("\nAuszahlung erfolgt.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nAusahlung unterbrochen: {error}')
