# Scraping personal account information from XP Investimentos

Extracting XP information.


run as:

```cd NotasCorretagens\
python -i chromedriver.py
```

Now you do your normal login + Token at the page (Chrome).

At the Home page you can run the command at prompt:
```
scraper.patrimonio()
```

And you will get your Net Worth.

Following the steps:

```In [5]: scraper.minha_conta()                                                                

In [6]: scraper.notas_corretagens()                                                          

In [7]: scraper.define_tipo_relatorio()                                                      

In [8]: scraper.gera_relatorio() ```

You will be in the brokerage notes page, with the report created in the page (pdf).

TO DO:

Be able to download the PDF or the parsed data!! (Transactions, assets, etc)


