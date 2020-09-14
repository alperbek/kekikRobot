# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from konsolTaban._renkler import *
from konsolTaban._evrensel import *
from konsolTaban._degiskenler import *

from roBot import *
from roBot._edevat import *
from os import listdir

#-----------------------------------#
print(f"{yesil}{logo}")         # yeşil renk koduyla logomuzu yazdırdık
print(ust_bilgi)                # Üst Bilgimizi yazdırdık

baslangic()

onemli("Eklentilerim;\n")

eklentiler = ""

for dosya in listdir("./roBot/Eklentiler/"):
    if not dosya.endswith(".py"):
        continue
    eklentiler += f"📂 {dosya.replace('.py','')} | "

bilgi(f"{eklentiler}\n\n")

if __name__ == "__main__":
    kekikRobot.run()
