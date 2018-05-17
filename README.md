# FRISC-PYNQ-lab2

@Marko Lazarić
@Tin Blažević

Zadatak: Zadatak 8 - Ispisivanje slova i znamenki

Oprema:
- LCD display

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
