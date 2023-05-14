# Base64

## Përshkrim i shkurtër i Base64
Base64 është një grup i skemave të ngjashme të enkodimit binar në tekst që prezantojnë të dhëna binare në një format ASCII string duke përkthyer atë në riprezantimin radix-64.
Termi Base64 rrjedh nga një enkodim special të përmbajtjes MIME.
Skemat e enkodimit Base64 përdoren zakonisht kur ka nevojë për enkodimin e të dhënave binare që duhen të ruhen dhe të transferohen në media që janë të dizajnuara për tu marrë me ASCII. Kjo është për tu siguruar se të dhënat mbesin të njëjta pa modifikim gjatë transportit. 

## Ekzekutimi i programit të implementuar për Base64
Programi për Base64 është implementuar në gjuhën programuese Python në kuadër të lëndës Siguria e të Dhënave dhe përmban pjesët për enkodim dhe dekodim të mesazhit.
Ekzekutimi i këtij programi bëhet përmes command line.  

Për enkodim të mesazhit përdoret komanda si më poshtë:

`python bookCipher.py -m e -i base64file.txt -o base64fileencoded.txt`

, ndërsa për dekodim të mesazhit përdoret komanda si më poshtë:

`python bookCipher.py -m d -i base64fileencoded.txt -o base64filedecoded.txt`

, ku:

-m përcakton modin (encode / decode ose e / d);

-i përcakton fajllin e mesazhit që do të enkriptohet apo dekriptohet;

-o përcakton fajllin ku do të ruhet rezultati pas ekzekutimit.


## Libraritë e nevojshme

Për ta ekzekutuar programin duhet të keni të instaluar paraprakisht ndonjë nga environments siç janë PyCharm apo IDLE Python dhe librarinë argparse.


## Anëtarët e grupit

- Alba Thaqi

- Albatin Totaj

- Ajshe Selmani

- Bleron Mexhuani



