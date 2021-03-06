# Rest Api Test Script

## Kullanılan kütüphaneler

* Python-requests: HTTP istekleri ve bu isteklerin yanıtlarını incelemek amacıyla kullanıldı.
HTTP yanıtındaki isteğin durum kodunun parse edilebilmesi için status_code metodu kullanıldı. İstendiği üzere 200 HTTP durum koduna eşit ise "başarılı" geri kalan tüm durumlar için "başarısız" çıktısı verecek şekilde yazıldı.

* Python-logging: Uyarı mesajları göstermek ve debug işlemini kolaylaştırmak amacıyla kullanıldı.

* Python-urlparse: Girilen URI'in doğru formatta olup olmadığının testi için kullanıldı.



# miniserver Python Script:


## Kullanılan kütüphaneler

* Python-flask: Testin testini yapabilmek için flask ile mini http sunucu uygulaması yazılmıştır. 

Örnek amacıyla sadece bazı test case'leri yazılan bu script, extra olarak eklenmiştir. 

_'hostname/200'_ adresine istek gönderilirse HTTP durum yaniti 200 verecek; _'hostname/not200'_ adresine istek gönderildiğinde ise 401 HTTP durum yanıtı dönmektedir.

miniserver.py çalışır durumda iken test(main.py) scriptimizin bu 2 adrese istek yaptığında **'başarılı'** veya **'başarısız'** çıktılarını vermesi beklenmektedir.

