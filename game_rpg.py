from abc import ABC, abstractmethod

# --- LATIHAN 5: ABSTRACTION (Kontrak Utama) ---
class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

# --- LATIHAN 1, 2, & 4: CLASS, INTERAKSI, & ENKAPSULASI ---
class Hero(GameUnit):
    def __init__(self, name, hp, attack_power):
        self.name = name
        # Latihan 4: Enkapsulasi (Atribut Private)
        self.__hp = hp 
        self.attack_power = attack_power

    # Latihan 4: GETTER & SETTER
    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! Maksimal HP 1000.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    # Latihan 1 & 5: Implementasi Info
    def info(self):
        print(f"Hero: {self.name} | HP: {self.get_hp()} | Power: {self.attack_power}")

    # Latihan 2: Interaksi Antar Objek
    def serang(self, lawan):
        print(f"\n{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.get_hp()}")

# --- LATIHAN 3 & 6: INHERITANCE & POLYMORPHISM ---
class Mage(Hero): # Mewarisi Hero
    def __init__(self, name, hp, attack_power, mana):
        # Latihan 3: Fungsi Super()
        super().__init__(name, hp, attack_power)
        self.mana = mana

    # Latihan 6: Polymorphism (Override Method Serang)
    def serang(self, lawan):
        if self.mana >= 20:
            print(f"\n{self.name} [Mage] menembakkan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            super().serang(lawan) # Serangan biasa jika mana habis

# --- MAIN PROGRAM (EKSEKUSI) ---
hero1 = Hero("Zilong", 120, 20)
hero2 = Mage("Eudora", 80, 30, 100)

hero1.info()
hero2.info()

# Latihan 2 & 6: Pertarungan dengan Polimorfisme
hero2.serang(hero1) # Mage menyerang dengan Skill
hero1.serang(hero2) # Hero biasa menyerang balik