from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
              "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
              "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."]

@app.route("/")
def hello_world():
    return '<a href="/rastgele_gercek">Rastgele Gerçek</a>'

@app.route("/rastgele_gercek")
def rastgele_gercek():
    return f'<p>{random.choice(facts_list)}</p>'


def home():
    return '<a href="/yazi_tura">Yazı-Tura At</a>'

@app.route("/yazi_tura")
def yazi_tura():
    sonuc = random.choice(["Yazı", "Tura", 'Yazı mı tura mı'])
    return f'<p>{sonuc}</p>'

if __name__ == "__main__":
    app.run(debug=True)
