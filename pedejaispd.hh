# Bāzes klase
class Skolotajs:
    def __init__(self, uzvards, stundu_skaits, tips):
        self.uzvards = uzvards
        self.stundu_skaits = stundu_skaits
        self.tips = tips


# Sākumskolas skolotājs
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, klase, stundu_skaits):
        super().__init__(uzvards, stundu_skaits, 1)
        self.klase = klase

    def izvadit(self):
        print(f"Sākumskolas (tips – {self.tips}) skolotājs {self.uzvards} māca {self.stundu_skaits} stundas {self.klase} klasē.")


# Vidusskolas skolotājs
class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, p1, st1, p2, st2):
        super().__init__(uzvards, st1 + st2, 3)

        self.p1 = p1
        self.p2 = p2
        self.st1 = st1
        self.st2 = st2

    def kopa_stundas(self):
        return self.st1 + self.st2

    def izvadit(self):
        print(f"Vidusskolas (tips – {self.tips}) skolotājs {self.uzvards} māca šādus priekšmetus: {self.p1} un {self.p2}, kopā {self.kopa_stundas()} stundas.")


# ===== IEVADES DAĻA =====

# Sākumskola (pareizā secība)
uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
klase = input("Ievadiet skolotāja klasi: ")
stundas = int(input("Ievadiet skolotāja stundu skaitu: "))

s = SakumskolasSkolotajs(uzvards, klase, stundas)


# Vidusskola (precīzi pēc tava saraksta)
uzvards2 = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
p1 = input("Ievadiet pirmo pasniegto priekšmetu: ")
st1 = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
p2 = input("Ievadiet otro pasniegto priekšmetu: ")
st2 = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))

v = VidusskolasSkolotajs(uzvards2, p1, st1, p2, st2)


# ===== IZVADS =====
print()
s.izvadit()
v.izvadit()