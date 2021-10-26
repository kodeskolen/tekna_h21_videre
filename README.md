# Nettkurs: Programmering for lærere

## Hva er dette repositoriet?
Dette repositoriet er ment for deling av kursmateriale for nettkurs i programmering for lærere som arrangeres av [Tekna Realistene](https://www.tekna.no/realistene) og [Kodeskolen](https://simulakodeskolen.no/). Materialer vil legges ut etterhvert som kurset går, kom derfor gjerne tilbake ved en senere anledning for å finne nyere materialer!

## Materiale
### Dag 1
* Hvis du vil laste ned alle notatbøkene for dag 1 kan du gjøre det **[her](https://github.com/kodeskolen/tekna_h21_videre/raw/main/dag1/materiale_dag1.zip)**
* Hvis du arbeider på Google Colab finner du notatbøkene vi arbeider med [her](dag1/google_colab)

### Dag 2
* Hvis du vil laste ned alle notatbøkene for dag 2 kan du gjøre det **[her](https://github.com/kodeskolen/tekna_h21_videre/raw/main/dag2/materiale_dag2.zip)**
* Hvis du arbeider på Google Colab finner du notatbøkene vi arbeider med [her](dag2/google_colab)
* Presentasjonen om Stefan-Boltzmann loven og klimafysikk finer du [her](dag2/Klimafysikk%20og%20Stefan-Boltzmann%20loven.pdf) (som pdf-fil) og [her](dag2/Klimafysikk%20og%20Stefan-Boltzmann%20loven.pptx) (som pptx-fil).
* Presentasjonen om undervisning med notebooks finner du [her](dag2/Notebookundervisning.pdf).

### Bonusmateriale
* En oppgavesamling med faglige relevante oppgaver er [her](bonus/faglig_relevante_oppgaver.pdf) (fasit er [her](bonus/faglig_relevante_oppgaver_fasit.pdf)).
* Kompendie med mer info om populasjon-simuleringer er er [her](bonus/befolkningsvekst_kompendie.pdf) (løsningsforslag for oppgavene i dette kompendiet er [her](bonus/befolkningsvekst_fasit.pdf))
* Kompendie med mer info om Monte Carlo estimering av π er [her](bonus/pi_estimering_kompendie.pdf)

## Kursets innhold:
Kurset vil passe for deg som deltok på vårt forrige kurs eller som har noe programmeringserfaring fra før. Vi ønsker at du skal få mer trening i å programmere, og få ideer til hvordan lage undervisningsopplegg som utforsker og løser problemstillinger innenfor realfagene.
Kurset fokuserer på programmeringseksempler som er relevante for matematikk og realfag. Sammen skal vi blant annet se på hvordan man kan estimere pi ved å dra nytte av sammenhengen mellom dartkast og Monte Carlo-integrasjon. 
## Hva er anbefalte forkunnskaper?
Kurset er en fortsettelse av et introduksjonskurs og antar at du er kjent med grunneleggende programmeringskonsepter (variabler, løkker, betingelser, funksjoner og plotting).
En gjennomgang av disse konseptene finner du i [kompendiene fra introkurset til Python](introkurs/kompendier). Du kan og finne oppgavene fra dette kurset [her](introkurs/oppgaver).

## Hva er `pylab`?
Pylab er en pakke som inneholder kode fra [NumPy](https://numpy.org/) og [Matplotlib](https://matplotlib.org/). Det gjør det enkelt å laste inn fra de følgende pakkene:

 * `numpy`: https://numpy.org/doc/stable/reference/routines.html
 * `numpy.fft`: https://numpy.org/doc/stable/reference/routines.fft.html
 * `numpy.random`: https://numpy.org/doc/stable/reference/random/index.html
 * `numpy.linalg`: https://numpy.org/doc/stable/reference/routines.linalg.html
 * `matplotlib.pyplot`: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

Du kan se alt som er mulig å importere fra pylab ved å kjøre koden

```python
import pylab

for navn in dir(pylab):
    if not navn.startswith("_"):
        print(navn)
```


## Ekstra Ressurser:
Her har vi samlet et knippe resurser som kan være nyttige som ekstra trening eller som inspirasjon for realfagsrelevante programmeringseksempler. 

[Kodeskolen VGS kurs](https://github.com/kodeskolen/vgs)
Materiale for et 5 dagers kurs arrangert av Kodeskolen våren 2019. 

[Introduksjonsbok for vitenskapelig programmering i Python](https://link.springer.com/book/10.1007/978-3-030-50356-7)
En gratis bok om vitenskapelig programmering i Python. Boken er pensum i faget "IN1900 – Introduksjon i programmering for naturvitenskapelige anvendelser", som er et introduksjonsemne i Python programmering ved UiO.

[Oppgavesamling i fysikk](https://github.com/kodeskolen/vgs/blob/master/Oppgavesamlinger/Oppgavesamling%20i%20fysikk.pdf)
Disse oppgavene er laget som et supplement til "IN1900 – Introduksjon i programmering for naturvitenskapelige anvendelser". Det er Fysisk Institutt som står bak oppgavesettet og ideen bak det var å lage en samling fysikkrelaterte oppgaver. Oppgavesettet kan derfor være en fin kilde til inspirasjon for fysikkrelevante programmeringsoppgaver.

[Oppgavesamling i kjemi](https://github.com/kodeskolen/vgs/blob/master/Oppgavesamlinger/Oppgavesamling%20i%20kjemi.pdf)
Disse oppgavene er laget som et supplement til introduksjonsemne i python programmering ved UiO. Oppgavene er laget for å gi kjemistudenter ved UiO relevante eksempler som kombinerer programmering og kjemi. Oppgavesettet kan derfor være en fin kilde til inspirasjon for kjemirelevante programmeringsoppgaver.

[Oppgavesamling i geo](https://github.com/kodeskolen/vgs/blob/master/Oppgavesamlinger/Oppgavesamling%20i%20geo.pdf)
Denne oppgavesamlingen inneholder programmeringsoppgaver i Python som er relevante for geofagstudenter ved UiO

[Oppgavesamling fra Langtangen](https://github.com/kodeskolen/vgs/blob/master/Oppgavesamlinger/Oppgavesamling%20fra%20Langtangen.pdf)
Oppgavesamling fra “A Primer on Scientific Programming with Python” av H. P. Langtangen. Boken brukes som lærebok i "IN1900 – Introduksjon i programmering for naturvitenskapelige anvendelser" som er et introduksjonsemne i python programmering ved UiO. Oppgavesettet inneholder grunnleggende programmeringsoppgaver med naturvitenskapelige anvedelser. Koden i boka er for Python 2.7, men oppgavene kan løses med Python 3.

[Ekstra oppgavesamling til Langtangen](https://github.com/kodeskolen/vgs/blob/master/Oppgavesamlinger/Ekstraoppgaver%20til%20Langtangen.pdf)
En samling supplementerende oppgaver for Langtangens bok.
