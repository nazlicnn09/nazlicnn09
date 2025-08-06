#themoviedb.org =film ve dizi arşivi
#themoviedbnin sunduğu apiyi uygulamamızda kullanıcaz
#anahtar kelimeye göre arama 
#en popüler film listesi 
#vizyondaki film listesi

"""
Yani biz bu sitenin bize sunduğu apiyi bize özel api keyi kullanarak
anahtar kelime araması popüler dizi listeleme ve 
vizyondaki filmleri listeleme uygulaması yapcıaz

bunun için öcenlikle https iteklerini yöneten request modülünü import edicez yani ben yaptığım projemde bir sitenin apisini 
kullanıcaksam ömncelikle http isteği yapmak için request modülü kullanmam gerekir.
"""
import requests

class theMovieDb:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3"
        self.api_key="deb51c6bedbc3e34353f190f690c3f18"
#bir fonksiyona parmetre koyduğun zaman sonra o fonskiyonu çağırdığında parametre ister.

    def getPopulars(self):
        response=requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()  # dönen bilgiyi pythonda kullanabilmek için json formatına çevirdik.
    
    def serchMovies(self,keyword):
         response=requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
         return response.json()

movieapi=theMovieDb()  # theMovieDb sınıfından nesne oluşturduk ki metodu istediğimiz yerde nesne üzerinden çağırabilelim.
while True:
    secim=input("1-Popular Movies\n2-Search Movies\n3-Exit\n Seçiniz: ")
    if secim=="3":
        break
    else:
        if secim=="1":
            movies=movieapi.getPopulars()
            for movie in movies["results"]:
                    print(movie["title"])

        if secim=="2":
             keyword=input("keyword:")
             movies =movieapi.serchMovies(keyword)
             for movie in movies["results"]:
                  print(movie["name"])
        