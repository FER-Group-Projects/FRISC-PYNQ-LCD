# FRISC-PYNQ-lab2

[@Marko Lazarić](https://github.com/mlazaric), [@Tin Blažević](https://github.com/TinBlazevic)

Zadatak: Zadatak 8 - Ispisivanje slova i znamenki

Oprema:
- LCD display
- žice
- protoboard

Zadatak je napraviti potprogram za ispisivanje slova i znamenki na LCD zaslon. Potprogram
preko stoga prima više parametara:
1. Pozicija X
2. Pozicija Y
3. Orijentacija (0 ili 1)
4. Boja znaka
5. Boja pozadine znaka
6. Kod znaka (može biti ASCII ili po izboru)

Napomene:
1. Svaki znak je potrebno definirati u memoriji
2. Svi znakovi su osnovne veličine od 8x8 piksela
3. Za opis jednog znaka potrebno je 8 bajtova (8x8 bitova - piksela) od kojih svaki bit
određuje ispunjava li se određeni piksel bojom znaka ili pozadine
4. U datoteci s primjerima postoji program koji koristi LCD, rutinu koja inicijalizira LCD se
može preuzeti kompletno od tog rješenja

# Rješenje:
U memoriji se nalaze praznina, znakovi engleske abecede, znamenke i boje.  
Osnovna veličina je 8x8 piksela.  
Iz primjera je preuzeta rutina za inicijalizaciju lcd-a i potprogram za crtanje pravokutnika.  

# Korisničko sučelje: 
  1 Pretpregled znaka za ispis  
  2 Trenutni redak   
  3 Trenutni stupac  
  4 Trenutni faktor skaliranja  
  5 Zastavica za način rada  
  6 Zastavica za omogućen ispis  
  7 Zastavica za spremanje orijentacije  

# Upute za korištenje:
Pritisnuti sva 4 gumba odjednom u bilo kojem načinu rada za reset.

Položaj switcheva definira načine rada (SW1 - lijevi bit, SW0 - desni bit)

00 - UI zastavica Z (znakovi)
    btn1 - prethodni znak u memoriji 
    btn2 - sljedeći znak u memoriji
    btn3 - omogućavanje upisa on/off (UI zastavica P)
    btn4 - omogući upis i upiši znak
    
01 - UI zastavica B (boje)
    btn1 - prethodna boja pozadine
    btn2 - sljedeća boja pozadine
    btn3 - prethodna boja znaka
    btn4 - sljedeća boja znaka
    
10 - UI zastavica N (navigacija)
    btn1 - redak--
    btn2 - redak++
    btn3 - stupac--
    btn4 - stupac++
    
11 - UI zastavica S (skaliranje)
    btn1 - faktor skaliranja--
    btn2 - faktor skaliranja++
    btn3 - promijeni orijentaciju x
    btn4 - promijeni orijentaciju y
	
    btn1 i btn2 ili btn3 i btn4 - spremanje orijentacije on/off (UI zastavica O)
    
![Upute za korištenje](/Slike/upute/4.jpg?raw=true "")


# Upute za spajanje:

![Upute za spajanje1](/Slike/upute/1.jpg?raw=true "")
![Upute za spajanje2](/Slike/upute/2.jpg?raw=true "")
![Upute za spajanje3](/Slike/upute/3.jpg?raw=true "")


# Primjeri:

![Primjer1](/Slike/primjeri/8.jpg?raw=true "")
![Primjer2](/Slike/primjeri/9.jpg?raw=true "")
