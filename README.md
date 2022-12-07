# schaefer-peters.com product information scraper

Scraper zum auslesen der Produktinformationen in dem Onlineshop schaefer-peters.com


Start URL ist immer das Untermenu z.b. `https://shop.schaefer-peters.com/de/Schrauben/Holzschrauben/`.
In diesem Fall werden für alle Holzschauben in jeder Grösse die Informationen ausgelesen.

Der Scraper kann mit folgendem Befehl gestartet werden

```
scrapy crawl productspider -O holzschrauben.csv  
```

Dateiname kann beliebig sein.

