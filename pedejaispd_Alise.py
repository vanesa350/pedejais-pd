# Bāzes klase (vecāku klase visiem skolotājiem)
class Skolotajs:
    def __init__(self, uzvards, stundu_skaits, tips):
        # Skolotāja uzvārds
        self.uzvards = uzvards
        # Kopējais stundu skaits
        self.stundu_skaits = stundu_skaits
        # Skolotāja tips (1 – sākumskola, 3 – vidusskola)
        self.tips = tips


# Sākumskolas skolotāja klase (mantota no Skolotajs)
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, klase, stundu_skaits):
        # Izsauc bāzes klases konstruktoru
        super().__init__(uzvards, stundu_skaits, 1)
        # Klase, kurā māca (piemēram, 1.a, 2.b utt.)
        self.klase = klase

    # Metode informācijas izvadīšanai
    def izvadit(self):
        print(f"Sākumskolas (tips – {self.tips}) skolotājs {self.uzvards} māca {self.stundu_skaits} stundas {self.klase} klasē.")


# Vidusskolas skolotāja klase (mantota no Skolotajs)
class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, p1, st1, p2, st2):
        # Kopējais stundu skaits ir abu priekšmetu summa
        super().__init__(uzvards, st1 + st2, 3)

        # Pirmais priekšmets
        self.p1 = p1
        # Otrais priekšmets
        self.p2 = p2
        # Stundu skaits pirmajam priekšmetam
        self.st1 = st1
        # Stundu skaits otrajam priekšmetam
        self.st2 = st2

    # Metode, kas aprēķina kopējo stundu skaitu
    def kopa_stundas(self):
        return self.st1 + self.st2

    # Metode informācijas izvadīšanai
    def izvadit(self):
        print(f"Vidusskolas (tips – {self.tips}) skolotājs {self.uzvards} māca šādus priekšmetus: {self.p1} un {self.p2}, kopā {self.kopa_stundas()} stundas.")


# ===== IEVADES DAĻA =====

# Lietotājs ievada sākumskolas skolotāja datus
uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
klase = input("Ievadiet skolotāja klasi: ")
stundas = int(input("Ievadiet skolotāja stundu skaitu: "))

# Izveido sākumskolas skolotāja objektu
s = SakumskolasSkolotajs(uzvards, klase, stundas)


# Lietotājs ievada vidusskolas skolotāja datus
uzvards2 = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
p1 = input("Ievadiet pirmo pasniegto priekšmetu: ")
st1 = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
p2 = input("Ievadiet otro pasniegto priekšmetu: ")
st2 = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))

# Izveido vidusskolas skolotāja objektu
v = VidusskolasSkolotajs(uzvards2, p1, st1, p2, st2)


# ===== IZVADS =====

# Tukša rinda ērtākai lasīšanai
print()

# Izvada sākumskolas skolotāja informāciju
s.izvadit()

# Izvada vidusskolas skolotāja informāciju
v.izvadit()