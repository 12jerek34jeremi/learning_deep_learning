Cześć, to jest repozytorium do "lekcji" z podstaw podstaw głębokiego uczenia maszynowego, któe będę prowadził. Fajnie było jeśli zrybiłbyś te rzeczy przed pierwszym spotkaniem:

1) Sklonuj na swój komputer to repozytorium.

2) Przygotuj sobie w Pythonie nowe środowisko wirtualne w którym będziesz miał zainstalowane numpy, matplotlib, PyTorch i jupyter (notebook).

3) Zainstaluj sobie (jeśli jeszcze tegoś nie zrobiłeś), coś w czym można łatwo edytować jupyter notebooks, na przykład Visual Studia Code.

Jak to zrobić (szczgółowe instrukcje):

1) Sklonuj na komputer to repozytorium. W lini polecen wpisz przejdz do folderu, w którym chcesz sklonować to repozytorium, na przykład Puplitu. Przykładowo z linii poleceń:<br>
 cd Desktop <br>
 git clone https://github.com/12jerek34jeremi/learning_deep_learning.git <br>

1.5) Jeżeli jeszcze nie masz zainstalowego pythona, to zainstaluj go sobie. Możesz go pobrac z <a href="https://www.python.org/downloads/release/python-3913">tej strony</a>

2) Przygotuj sobie środowisko wirtulane, w którym będziesz miał numpy, matplotlib i PyTorch. Przygotowałem plik requirements.txt, który ułatwi zadanie. Uwaga, ponieważ instalacja PyTorch'a jest trochę bardziej zagmatwana, to w pliku requirements.txt nie ma PyTorch'a. Przykładowo z linii polecen:
   1) Najperw przejdz do folderu w którym chcesz utworzyć now środowisko wirtualne. <br>
        <b>cd Desktop/learning_deep_learning</b>
   2) Utwurz nowe środowisko wirtualne przy pomocy pakietu venv Pythona. <br>
      <b>python -m venv .venv</b>
   3) Aktywuj środowisko wirtualne:<br>
      Na windows: <b>.venv\Scripts\activate<br></b>
      Na linux: <b>source .venv/bin/activate</b><br>
   4) Zainstaluj sobie numpy i matplotlib:
      1) Albo z plikurequirements.txt:  <b>pip install -r requirements.txt</b> <br>
      2) Albo ręcznie: <b>pip install numpy matplotlib</b>
   5) Na stronie <a href="https://pytorch.org/">tą strone</a> znajdziesz odpowiednią komendę do zainstalowania Pytorcha. W pierwszym rzędzie wybierz "Stable", w drugim swój system operacyjny, w trzecim "Pip", w czwartym "Python". Jeśli masz kartę graficzną producenta Nvidia to wybierz w piątym rzędzie opcje "CUDA 11.3", jeśli masz zintegrowaną kartę graficzną lub kartę innego producanta, na przykład Amd, to wybierz opcję "CPU". Skopuj odpowiednią komendę i ją wykanaj. Dla mnie to było:<br>
      <b>pip3 install torch torchvision torchaudio</b><br>
     Pytorcha będziemy używać dopiero na drugim spotkaniu.
   6) Teraz trzeba dodać jupyter'a do środowiska. Zrobisz to poniższą komendą, bądź cierpliwy jupyter może się parę minut instalować. <br>
    <b>pip install jupyter</b>
3) Poberz Visual Studio Code <a href="https://code.visualstudio.com/download">z tej strony.</a> Uruchom Visual Studio i z lewego pionowego meni wybierz zakładkę "Extensions", a następnie wyszukaj i zainstaluj rozszerzenia "Python" i "Jupyter". Gdy juz to zrobisz, to z górnego menu wybierz File->Open Folder. Wybierz folder, który sklonowałeś z githuba (learning_deep_learning). Teraz z menu po lewej stronie wybierz plik "numpy.ipynb". Uruchom pierwszą komórkę (zielona strzałka w górnym menu) i sprawdź, czy się uruchamia i nie wyświetla żadncyh błędów.
<br>
<br>
<br>
<br>
<a href = "https://docs.google.com/presentation/d/1DOKdcR1Zl3T95eQKt2Pw6XzmVOncgPz4THhCsVtyN1E/edit?usp=sharing">Link do prezentacji którą będę używał na spotkaniach.</a><br>
<a href="https://discord.gg/7VngznpC">Link do kanału na discord, na którym jest więcej informacji.</a>

