import pandas as pd 

df = pd.read_csv('imdb.csv')

result = df 
result = df.columns

#Dataset Hakkında Bilgi verir
result = df.info

#1- İlk 5 kaydı gösterir
result = df.head()

#2- İlk 10 kaydı gösterir
result = df.head(10)

#3- Son 5 kaydı gösterir
result = df.tail()

#4- Son 10 kaydı gösterir
result = df.tail(10)

#5- Sadece Movie_Title kolonunu getirir
result = df["Movie_Title"]

#6- Sadece Movie_Title kolonunun ilk 5 kaydını getirir.
result = df["Movie_Title"].head()

#7- Sadece Movie_Title ve Rating kolonlarının ilk 5 kaydını getirir.
result = df[["Movie_Title","Rating"]].head()

#8- Sadece Movie_Title ve Rating kolonlarının son 7 kaydını getirir.
result = df[["Movie_Title","Rating"]].tail(7)

#9- Sadece Movie_Title ve Rating kolonlarını içeren ikinci 5 kaydını getirir.
result = df[5:][["Movie_Title","Rating"]].head() #Aynı işi yapıyor -> result = df[5:10][["Movie_Title","Rating"]]

#10- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 ve üzerinde olan kayıtlardan ilk 50 tanesini getirir.
result = df[df["Rating"] >= 8.0][["Movie_Title","Rating"]].head(50)

#12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getirir.
result = df[(df["YR_Released"] >=2014 ) & (df["YR_Released"] <= 2015)][["Movie_Title","YR_Released"]]

#13- Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı 8 ile 9 arasında olan filmleri getirir.
result = df[(df["Num_Reviews"] > 100000 ) | ((df["Rating"] >= 8.0) & (df["Rating"] <= 9.0))][["Movie_Title","Num_Reviews","Rating"]]


print(result)