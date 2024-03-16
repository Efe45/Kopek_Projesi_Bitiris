# İçe aktar
from flask import Flask, render_template,request, redirect
# Veri tabanı kitaplığını bağlama
from flask_sqlalchemy import SQLAlchemy
from modelll import *

app = Flask(__name__)
dogs = {
        "coban kopegi"  : """Çoban Köpeği, etkileyici görünümleri ve sağlam yapısıyla tanınan, çiftlik ve çobanlık gibi görevlerde kullanılan bir köpek türüdür. Orta ila büyük boyutlarıyla bilinirler ve güçlü kas kütlesine sahip iri yapıları vardır. Bu özellikleri, onları diğer köpeklerden ayıran belirgin bir özellik haline getirir.

Çoban Köpeklerinin en dikkat çekici özelliği, etkileyici görünümleri ve cesur kişilikleriyle bilinmeleridir. Kendine güvenen ve kararlı bir karaktere sahiptirler. Aynı zamanda, sahiplerine karşı sadık ve koruyucu bir bağ geliştirirler. İnsanlarla sakin ve dostça ilişkiler kurabilirler ancak yabancılara karşı mesafeli olabilirler.

Beslenme alışkanlıkları da önemlidir. Çoban Köpekleri, sağlıklı bir yaşam sürdürebilmek için dengeli bir diyet gerektirirler. Et ürünleri arasında tavuk eti, kuzu eti, sığır eti ve hindi eti gibi protein kaynakları önemlidir. Ayrıca, sebzelerden havuç, ıspanak, kabak ve brokoli gibi besinler de diyetlerinde bulunmalıdır. Bu sağlıklı beslenme alışkanlıkları, onların enerjik ve dayanıklı bir yapıya sahip olmalarına katkı sağlar.""",   	
"Akbas coban kopegi" : """Akbaş Çoban Köpeği, etkileyici görünümleri ve güçlü yapısıyla dikkat çeken bir çoban köpeği türüdür. Büyük boyutlarıyla bilinirler ve diğer köpek türlerine göre daha iri yapıları ve güçlü kas kütlesi vardır. Bu özellikleri, onları diğer köpeklerden ayıran belirgin bir özellik haline getirir.

Akbaş Çoban Köpeklerinin en dikkat çekici özelliği, etkileyici görünümleri ve cesur kişilikleriyle tanınmalarıdır. Kendine güvenen ve kararlı bir karaktere sahiptirler. Aynı zamanda, sahiplerine karşı sadık ve koruyucu bir bağ geliştirirler. İnsanlarla sakin ve dostça ilişkiler kurabilirler ancak yabancılara karşı mesafeli olabilirler.

Beslenme alışkanlıkları da önemlidir. Akbaş Çoban Köpekleri, sağlıklı bir yaşam sürdürebilmek için dengeli bir diyet gerektirirler. Et ürünleri arasında tavuk eti, kuzu eti, sığır eti ve hindi eti gibi protein kaynakları önemlidir. Ayrıca, sebzelerden havuç, ıspanak, kabak ve brokoli gibi besinler de diyetlerinde bulunmalıdır. Bu sağlıklı beslenme alışkanlıkları, onların enerjik ve dayanıklı bir yapıya sahip olmalarına katkı sağlar.""",

                
"yorkipoo": """Yorkipoo, sevimli ve şirin görünümleriyle dikkat çeken bir süs köpek türüdür. Küçük boyutlarıyla tanınırlar ve diğer köpek türlerine göre daha ufak yapıları ve hafif kiloları vardır. Bu özellikleri, onları diğer köpeklerden ayıran belirgin bir özellik haline getirir.
 					Yorkipooların en çekici özelliği, karşı konulması güç olan tatlı görünümleri ve sevecen kişilikleriyle bilinirler. İnsanlarla hızla bağ kurabilen ve arkadaş canlısı olan bu evcil hayvanlar, aynı zamanda oldukça zekidirler. Sahiplerine karşı sadık ve sevgi dolu bir bağ geliştirirler ve aileleriyle zaman geçirmekten keyif alırlar.
         			Beslenme alışkanlıkları da önemlidir. Yorkipooların severek tükettiği et ürünleri arasında tavuk eti, kuzu eti, sığır eti ve hindi eti bulunur. Ayrıca, sebzelerden brokoli, salatalık, patates ve balkabağı da en sevdikleri bitkisel ürünler arasındadır. Bu sağlıklı beslenme alışkanlıkları, onların enerjik ve sağlıklı bir yaşam sürmelerine katkı sağlar.""",                
"alman coban kopegi" : """Dişi cinsiyetli Alman çoban köpeklerinin ideal boyu 57,5 cm, erkeklerde ise 62,5 cm dir.
      2,5 santimetreye kadar olan boy uzunluğu sapması olağan karşılanır.
      Ağırlıkları ise dişilerde 22–32 kg., erkeklerde ise 35–40 kg. aralığındadır.
      Yüzü sert hatlı, alnı kubbe şeklinde ve burnu uzundur. Burun mantarı siyahtır.
      Çenesi güçlü olduğundan, keskin ısırışlara sahiptir.
      Gözleri orta büyüklükte, kahverengidir. Neşeli, zeki ve kendinden emin bakar.
      Kulakları geniş ve başa 90 derece dik olacak şekilde birbirine paralel duruşla konumlanmıştır.
      Boynu uzundur ve kaldırıp indirerek hareket esnasında hızını ayarlar. Kuyruğu uzun ve tüylüdür.
      Sindirim sistemi son derece hassas olan Alman çoban köpeği beslenirken kaliteli gıdalar tercih edilmelidir.
      Temel gıdası kuru mama olan köpekler, 1 yaşından sonra yetişkin mamasıyla beslenmelidir.
      Mamaların yüksek protein içermesinin haricinde sığır, tavuk ve kuzu eti gibi besin içeriğine sahip olması gerekir""",
"Amerikan Tilki tazısı" :   """Amerikan Tilki Tazısı, zarif görünümleri ve atletik yapısıyla tanınan, genellikle avcılık ve iz sürme gibi görevlerde kullanılan bir türdür. Orta boyutlarda olup, atletik yapıları ve ince kemik yapısıyla bilinirler. Bu özellikleri, onları diğer köpeklerden ayıran belirgin bir özellik haline getirir.

Amerikan Tilki Tazılarının en dikkat çekici özelliği, zarif görünümleri ve hızlı hareket kabiliyetleriyle bilinmeleridir. Cesur ve dikkatli bir karaktere sahiptirler. Aynı zamanda, sahiplerine karşı sadık ve sevgi dolu bir bağ geliştirirler. İnsanlarla genellikle dostça ilişkiler kurabilirler, ancak avlanma içgüdüleri yüksek olduğundan diğer evcil hayvanlarla aralarında çatışma olabilir.

Beslenme alışkanlıkları da önemlidir. Amerikan Tilki Tazıları, sağlıklı bir yaşam sürdürebilmek için dengeli bir diyet gerektirirler. Et ürünleri arasında tavuk eti, kuzu eti, sığır eti ve hindi eti gibi yüksek protein kaynakları önemlidir. Ayrıca, sağlık için gerekli vitamin ve mineralleri alabilmek için sebzelerden havuç, ıspanak, kabak ve brokoli gibi besinler de diyetlerinde bulunmalıdır. Bu sağlıklı beslenme alışkanlıkları, onların enerjik ve dayanıklı bir yapıya sahip olmalarına katkı sağlar.""",              
"Bloodhound"  :  """Bloodhound, güçlü koku alma yetenekleriyle ünlü, büyük ve güçlü bir av köpeği türüdür. İnce kemik yapısıyla değil, daha güçlü bir yapıya sahiptirler. Genellikle avcılık ve iz sürme görevlerinde kullanılan bu köpekler, iz sürme konusunda olağanüstü yeteneklere sahiptirler.

Bloodhound'lar, keskin koku alma yetenekleriyle bilinirler. Koku izlerini takip etme konusunda üstün yeteneklere sahip olmaları, onları kaybolan kişileri bulma veya suçluları takip etme gibi görevlerde çok değerli kılar. Bu özellikleri, arama ve kurtarma operasyonlarında da sıkça kullanılmalarını sağlar.

Genellikle cesur ve kararlı bir karaktere sahiptirler. Çalışma anlamında oldukça odaklı olabilirler ve sahiplerine karşı sadık bir bağ geliştirirler. Ancak, diğer evcil hayvanlarla ilişkileri konusunda bazen sorunlar yaşayabilirler, özellikle avlanma içgüdüleri yüksek olduğunda.

Beslenme alışkanlıkları da önemlidir. Bloodhound'lar, sağlıklı bir yaşam sürdürebilmek için dengeli bir diyet gerektirirler. Yüksek kaliteli protein kaynakları, vitaminler ve mineraller içeren bir beslenme programı onların dayanıklı ve enerjik kalmasına yardımcı olur. Et ürünleri, sebzeler ve uygun miktarlarda karbonhidrat içeren bir diyet, genel sağlıklarını destekler.

Bloodhound'lar, atletik yapıları ve güçlü koku alma yetenekleriyle dikkat çekerler. Sağlıklı bir yaşam sürdürebilmek ve görevlerini en iyi şekilde yerine getirebilmek için düzenli egzersiz ve uygun beslenme çok önemlidir.
""", 
"Golden retriever" : """Golden Retriever, dostane ve sevecen doğasıyla tanınan orta büyüklükte bir köpek türüdür. Zarif yapılı ve atletik yapılarıyla bilinirler. Genellikle aileler arasında popülerdirler ve çocuklarla iyi geçinme eğilimindedirler.

Golden Retriever'ların en dikkat çekici özelliklerinden biri, dostça ve sevecen doğalarıdır. Diğer insanlarla ve diğer evcil hayvanlarla genellikle uyumlu bir ilişki kurarlar. Sadık ve bağlı bir karaktere sahiptirler ve sahiplerine karşı büyük bir sevgi ve sadakat gösterirler.

Bu türün enerjik yapısı, düzenli egzersiz gereksinimleriyle dengelenmelidir. Yürüyüşler, koşular ve oyunlar, Golden Retriever'ların fiziksel sağlığını ve zindeliğini korumalarına yardımcı olur. Ayrıca, zihinsel uyarım sağlayan aktiviteler de önemlidir, çünkü bu köpekler zeki ve öğrenmeye açık olabilirler.

Beslenme alışkanlıkları da önemlidir. Golden Retriever'lar, sağlıklı bir yaşam sürdürebilmek için dengeli bir diyet gerektirirler. Yüksek kaliteli proteinler, sağlıklı yağlar, vitaminler ve mineraller içeren bir beslenme programı onların sağlıklı gelişimini destekler. Ayrıca, aşırı kilo alma eğilimleri olduğundan, porsiyon kontrolü de önemlidir.

Golden Retriever'lar, eğitilebilir ve işbirliğine açık bir yapıya sahiptirler. İyi bir sosyalleşme ve temel eğitimle, uyumlu ve davranış açısından dengeli bir yetişkin haline gelirler. Özellikle erken yaşlarda eğitime başlamak önemlidir, çünkü bu tür genellikle çocuklarla etkileşime girdikleri için iyi huylu davranışları öğrenmeleri önemlidir.

Sonuç olarak, Golden Retriever, sevgi dolu, dostane ve aktif bir köpek türüdür. Sağlıklı bir yaşam sürdürebilmek ve mutlu bir şekilde yaşlanabilmek için düzenli egzersiz, uygun beslenme ve sevgi dolu bir ortam sağlanmalıdır.""",
"Norwegian Elkhound" : """Norwegian Elkhound, güçlü ve dayanıklı yapısıyla tanınan orta büyüklükte bir köpek ırkıdır. Bu köpekler, avcılık ve çobanlık gibi görevler için özellikle Norveç'te yaygın olarak kullanılmıştır. Orta derecede kemik yapısına sahiptirler ve tipik olarak sağlam bir yapıya sahiptirler.

Norwegian Elkhound'ların en dikkat çekici özelliklerinden biri, cesur ve kararlı karakterleridir. Avlanma içgüdüleri yüksektir ve av izlerini takip etme konusunda oldukça yeteneklidirler. Aynı zamanda sahiplerine karşı sadık ve koruyucu olabilirler.

Bu köpeklerin enerjik bir yapısı vardır ve düzenli egzersiz gereksinimleri vardır. Uzun yürüyüşler, koşular veya oyunlar, fiziksel ve zihinsel uyarım sağlar ve onların mutlu ve dengeli bir yaşam sürmelerine yardımcı olur.

Beslenme alışkanlıkları da önemlidir. Norwegian Elkhound'lar, sağlıklı bir yaşam sürdürebilmek için dengeli bir diyet gerektirirler. Yüksek kaliteli protein kaynakları, sağlıklı yağlar, vitaminler ve mineraller içeren bir beslenme programı, onların sağlıklı gelişimini destekler. Ayrıca, aşırı kilo alma eğilimleri olduğundan, porsiyon kontrolü de önemlidir.

Norwegian Elkhound'lar, eğitilebilir ancak bazen inatçı olabilirler. Erken sosyalleşme ve temel eğitim, istenmeyen davranışların önlenmesine ve uyumlu bir yetişkin haline gelmelerine yardımcı olabilir. Disiplinli ancak adil bir liderlik altında eğitildiklerinde, sevecen ve dostane bir arkadaş olurlar.

Sonuç olarak, Norwegian Elkhound, güçlü, cesur ve sadık bir köpek ırkıdır. Sağlıklı bir yaşam sürdürebilmek ve mutlu bir şekilde yaşlanabilmek için düzenli egzersiz, uygun beslenme ve sevgi dolu bir ortam sağlanmalıdır.""",
"pitbull" : """Pitbull, güçlü ve atletik yapısıyla tanınan bir köpek ırkıdır. Orta büyüklükte olup, kaslı ve sağlam bir yapıya sahiptirler. Genellikle sağlam bir kemik yapısına ve kısa, parlak bir tüy örtüsüne sahiptirler. Bu özellikleri, onları diğer köpeklerden ayıran belirgin bir özellik haline getirir.

Pitbull'ların en dikkat çekici özelliği, güçlü yapısı ve cesur karakteridir. Sahiplerine karşı son derece sadık ve koruyucu olabilirler. Aynı zamanda, sosyal ve oyuncu bir doğaya da sahiptirler. İyi sosyalleştirilmiş Pitbull'lar genellikle diğer insanlar ve hayvanlarla iyi geçinirler.

Bu köpeklerin enerjik bir yapısı vardır ve düzenli egzersiz gereksinimleri vardır. Uzun yürüyüşler, koşular veya oyuncaklarla oyunlar, fiziksel ve zihinsel uyarım sağlar ve onların mutlu ve dengeli bir yaşam sürmelerine yardımcı olur.

Beslenme alışkanlıkları da önemlidir. Pitbull'lar, sağlıklı bir yaşam sürdürebilmek için dengeli bir diyet gerektirirler. Yüksek kaliteli protein kaynakları, sağlıklı yağlar, vitaminler ve mineraller içeren bir beslenme programı, onların sağlıklı gelişimini destekler. Ayrıca, aşırı kilo alma eğilimleri olduğundan, porsiyon kontrolü de önemlidir.

Pitbull'lar, eğitilebilir ve zeki köpeklerdir. İyi bir sosyalleşme ve temel eğitimle, uyumlu ve davranış açısından dengeli bir yetişkin haline gelirler. Sahiplerinin isteklerini anlamak ve onlarla işbirliği yapmak için eğitilmelidirler.

Sonuç olarak, Pitbull, güçlü, sadık ve oyuncu bir köpek ırkıdır. Sağlıklı bir yaşam sürdürebilmek ve mutlu bir şekilde yaşlanabilmek için düzenli egzersiz, uygun beslenme ve sevgi dolu bir ortam sağlanmalıdır. Ayrıca, doğru eğitimle, sevecen ve uyumlu bir arkadaş olabilirler."""  ,

"schnoodle" : """Schnoodle, Schnauzer ve Poodle cinslerinin melezlenmesiyle elde edilen harika bir köpek türüdür. Orta büyüklükte olup, sevimli ve enerjik bir yapıya sahiptirler. Karışık bir köpek olmalarına rağmen genellikle kürkleri kıvırcık ve yumuşaktır, bu da onları alerji sorunu olan kişiler için uygun bir seçenek haline getirir.

Schnoodle'ların en dikkat çekici özelliği, akıllı ve dostane karakterleridir. Hem Schnauzer hem de Poodle cinsleri zeki köpekler olduğundan, Schnoodle'lar da aynı şekilde eğitilebilir ve zeki olma eğilimindedirler. Sahiplerine karşı sevgi dolu ve bağlı bir bağ geliştirirler, aynı zamanda çocuklar ve diğer evcil hayvanlarla da iyi geçinme eğilimindedirler.

Bu köpeklerin enerji seviyeleri genellikle orta düzeydedir ve düzenli egzersiz gereksinimleri vardır. Yürüyüşler, oyunlar ve zihinsel uyarım sağlayan aktiviteler, Schnoodle'ların sağlıklı ve dengeli bir yaşam sürmelerine yardımcı olur.

Beslenme alışkanlıkları da önemlidir. Schnoodle'lar, sağlıklı bir yaşam sürdürebilmek için dengeli bir diyet gerektirirler. Yüksek kaliteli protein kaynakları, sağlıklı yağlar, vitaminler ve mineraller içeren bir beslenme programı, onların sağlıklı gelişimini destekler. Ayrıca, uygun porsiyon kontrolü de kilo kontrolü açısından önemlidir.

Schnoodle'lar, sevecen, zeki ve enerjik bir köpek türüdür. Sağlıklı bir yaşam sürdürebilmek ve mutlu bir şekilde yaşlanabilmek için düzenli egzersiz, uygun beslenme ve sevgi dolu bir ortam sağlanmalıdır. İyi sosyalleşme ve temel eğitimle, Schnoodle'lar harika aile evcil hayvanları olabilirler ve sahipleri için gerçek birer arkadaş olabilirler."""   
                }
@app.route('/', methods=['GET','POST']) 
def anasayfa():
	
	dog_names = dogs.keys()
	
	return render_template('index.html', dogs = dog_names)

@app.route('/card/<dogname>')
def card(dogname):
    dog_info = dogs[dogname]
    return render_template('dog.html', dogname = dogname, dog_info = dog_info)

@app.route('/detect')
def detect():
    return render_template('detect.html')	

@app.route('/dog_detect', methods=['GET','POST'])
def dog_detect():
    if request.method == 'POST':
        file = request.files['file']
        
        if file:
            filename = file.filename
            file.save("static/img/" + filename)
            class_name, confidence_score = predict_image_class("static/img/" + filename)
        
        return redirect('detection.html', class_name = class_name, confidence_score = confidence_score )
    else:
        return render_template('detect.html')
    
app.run(debug=True)
