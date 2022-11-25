<h1>Grandmetric RestAPI</h1>

<h1>1. O projekcie</h1>
Ten projekt jest wykonany jako testowe zlecenie dla Grandmetric na stanowisko backend developera.  Istotą zadania jest napisanie Rest Api.

<h1>2. Wstęp</h1>
Celem zadania jest napisanie REST HTTP API, które posiada dwa endpointy:
<ul>
  <li>GET `/status`, który odpowiada kodem HTTP 200 i wiadomością "ok"</li>
  <li>POST `/day`, który przyjmuje payload w formie JSON `{"date": "28.10.2022"}`</li>
</ul>
W odpowiedzi zwrotnej (HTTP 200) powinniśmy otrzymać body:<br>
{ <br>
      "28": "28 is the second perfect number.", <br>
      "10": "10 is a composite number, its proper divisors being 1, 2 and 5.", <br>
      "2022": "2022 is an uninteresting number." <br>
} <br>

<h1>3. Jak używać / sprawdzić</h1>
<ul>
  <li>Ściągnij projekt</li>
  <li>Zainstaluj Python https://www.python.org/downloads/</li>
  <li>Zainstaluj Pip https://pip.pypa.io/en/stable/cli/pip_install/</li>
  <li>Zainstaluj FastApi https://fastapi.tiangolo.com/tutorial/</li>
  <li>Zainstaluj Pydantic https://pydantic-docs.helpmanual.io/install/</li>
  <li>Zainstaluj Uvicorn https://www.uvicorn.org/#quickstart</li>
  <li>Zainstaluj Requests https://requests.readthedocs.io/en/latest/user/install/#install</li>
</ul>

<h1>Wykorzystanie / licencja</h1>
Ten projekt nie zawiera żadnych licencji ani praw autorskich, być może ten projekt będzie dobrym przykładem. 






