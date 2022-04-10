    # Çözene 1M dolar ödül var denilen Collatz Sorununu deneyen bir program.
    # Copyright (C) 2022 libsoykan-dev

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
def collatz_sorunu(sayi): # Collatz sorunu fonksiyonunu tanımla

   sequence = [sayi] # Döngü kümesini tanımla
   
   while(sayi != 1): # Döngü 1 ile bitene kadar
   
       if((sayi % 2) == 0): # Sayı çift ise
       
           sayi = sayi // 2 # x / 2
           
       else:
       
           sayi = (sayi * 3) + 1 # 3x + 1
           
       sequence.append(sayi) # Sayıyı döngü kümesine ekle
       
   return sequence[-1] # Döngü kümesinin son elemanını çıktı olarak ver
   

def sonsuz(): # 1'den sonsuza aralığını tanımla

    index = 1
    
    while True:
    
        yield index
        
        index += 1

for a in sonsuz():

    if collatz_sorunu(a) == 1: # Döngü 1 ile biterse
        
        #print(sequence) # Eğer döngü kümesi de yazdırılsın isterseniz bu satırın yorumunu kaldırın
        
    	print(str(a) + " 1 ile bitti") # Yazdır
    	
    else:
    
    	print(str(a) + " 1 ile bitmedi!!!") # 1 ile bitmeyen bir döngü bulursa -ki bu imkansız- yazdır
    	
    	exit() # 1 ile biten döngü bulursa çık
