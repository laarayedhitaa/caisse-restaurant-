from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def suprimer_item(item):
    t=w.to.text()
    total=float(t[:len(t)-2])
    nom=item.text()
    if nom== "pasta_bolognèse 13.700dt":
        total-= 13.700
    elif nom== "pasta_sauce 15dt":
        total-= 15
    elif nom== "pasta_à la creme 20dt":
        total-= 20 
    elif nom== "pasta_fruit de mer 25.500dt":
        total-= 25.500
    elif nom== "pasta_salade 13.200dt":
        total-= 13.200
    elif nom== "pasta_pisto 17dt":
        total-= 17
    elif nom== "caneloni 15.500dt":
        total-= 15.500
    elif nom== "lasagne 18dt":
        total-= 18
    elif nom== "crevette_pané 22.700dt":
        total-= 22.700
    elif nom== "plat healthy 13dt":
        total-= 13
    elif nom== "cordon bleu 11.500dt":
        total-= 11.500
    elif nom== "plat poisson 20dt":
        total-= 20
    elif nom== "escalope à la creme 15dt":
        total-= 15
    elif nom== "plat chawarma 14dt":
        total-=14
    elif nom== "plat escalope pané 12dt":
        total-=12
    elif nom== "steck 14dt":
        total-=14
    elif nom== "tacos 12.500":
        total-=12.500
    elif nom== "sandwitch 10dt":
        total-=10
    elif nom== "hamburger 15dt":
        total-=15
    elif nom== "taco mexicain 17dt":
        total-=17
    elif nom== "sandwitch français 11dt":
        total-=11
    elif nom== "toast 11.700dt":
        total-=11.700
    elif nom== "sandwitch chawarma 13dt":
        total-=13
    elif nom== "pizza escalope 23dt":
        total-=23
    elif nom== "pizza margherita 15.800":
        total-= 15.800
    elif nom== "pizza pepperoni 16.500":
        total-=16.500
    elif nom== "pizza hawain 15.500dt":
        total-=15.500
    elif nom== "pizza viande haché 23dt":
        total-=23
    elif nom== "salade de fruits à 8 dt":
        total-=8
    elif nom=="pizza 4 fromage 22dt":
        total-=22
    elif nom== "pizza vegeterien 15dt":
        total-=15
    elif nom== "pizza champignon & huil 25dt":
        total-=25
    elif nom== "fondant 7.500dt":
        total-=7.500
    elif nom== "crèpe sucré 9.800dt":
        total-=9.800
    elif nom== "pancake 8.700dt":
        total-=8.700
    elif nom== "tiramissu 9.500dt":
        total-=9.500
    elif nom== "gaufre 11dt":
        total-=11
    elif nom== "donuts 7dt":
        total-=7
    elif nom== "cheesecake 10dt":
        total-=10
    elif nom== "jus 5.500dt":
        total-=5.500
    elif nom== "mojito 7dt":
        total-=7
    elif nom== "spanish latte 13dt":
        total-=13
    elif nom== "vanille latte 11dt":
        total-=11
    elif nom== "iced thea 9dt":
        total-=9
    elif nom== "iced coffee 13dt":
        total-=13
    elif nom== "milkshake 12dt":
        total-=12
    elif nom== "matcha 10dt":
        total-=10
    w.list.takeItem(w.list.row(item))
    w.to.setText(str(total)+"dt")
def dd_click():
    w.list.itemDoubleClicked.connect(suprimer_item)
    w.list.addItem("pasta_sauce 15dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(15)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+15
        w.to.setText(str(a)+"dt")
def aa_click():
    w.list.itemDoubleClicked.connect(suprimer_item)
    w.list.addItem("pasta_bolognèse  13.700dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(13.700)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+13.700
        w.to.setText(str(a)+"dt")
def ee_click():
    w.list.itemDoubleClicked.connect(suprimer_item)
    w.list.addItem("pasta_à la creme 20dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(20)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+20
        w.to.setText(str(a)+"dt")
def ff_click():
    w.list.itemDoubleClicked.connect(suprimer_item)
    w.list.addItem("pasta_fruit de mer 25.500dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(25.500)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+25.500
        w.to.setText(str(a)+"dt")
def hh_click():
    w.list.itemDoubleClicked.connect(suprimer_item)
    w.list.addItem("pasta_salade 13.200dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(13.200)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+13.200
        w.to.setText(str(a)+"dt")
def bb_click():
    w.list.addItem("pasta_pisto 17dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(17)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+17
        w.to.setText(str(a)+"dt")
def cc_click():
    w.list.addItem("caneloni 15.500dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(15.500)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+15.500
        w.to.setText(str(a)+"dt")
def gg_click():
    w.list.addItem("lasagne 18dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(18))+"dt"
    else:
        s=s[:len(s)-2]
        a=float(s)+18
        w.to.setText(str(a)+"dt")
def kk_click():
    w.list.addItem("crevette_pané 22.700dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(22.700)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+22.700
        w.to.setText(str(a)+"dt")
def ww_click():
    w.list.addItem("plat healthy 13dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(13)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+13
        w.to.setText(str(a)+"dt")
def xx_click():
    w.list.addItem("cordon bleu 11.500dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(11.500)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+11.500
        w.to.setText(str(a)+"dt")
def mm_click():
    w.list.addItem("plat poisson 20dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(20)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+20
        w.to.setText(str(a)+"dt")
def ll_click():
    w.list.addItem("escalope à la creme 15dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(15)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+15
        w.to.setText(str(a)+"dt")
def nn_click():
    w.list.addItem("plat chawarma 14dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(14)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+14
        w.to.setText(str(a)+"dt")
def vv_click():
    w.list.addItem("plat escalope pané 12dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(12)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+12
        w.to.setText(str(a)+"dt")
def aaa_click():
    w.list.addItem("steck 14dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(14)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+14
        w.to.setText(str(a)+"dt")
def a6_click():
    w.list.addItem("tacos 12.500")
    s=w.to.text()
    if s=="":
        w.to.setText(str(12.500)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+12.500
        w.to.setText(str(a)+"dt")
def ttt_click():
    w.list.addItem("sandwich saucisse 12")
    s=w.to.text()
    if s=="":
        w.to.setText(str(12)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+12
        w.to.setText(str(a)+"dt")
def a8_click():
    w.list.addItem("hamburger 15dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(15)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+15
        w.to.setText(str(a)+"dt")
def a3_click():
    w.list.addItem("taco mexicain 17dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(17)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+17
        w.to.setText(str(a)+"dt")
def a4_click():
    w.list.addItem("sandwitch 10dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(10)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+10
        w.to.setText(str(a)+"dt")
def a1_click():
    w.list.addItem("sandwitch français 11dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(11)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+11
        w.to.setText(str(a)+"dt")
def a5_click():
    w.list.addItem("toast 11.700dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(11.700)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+11.700
        w.to.setText(str(a)+"dt")
def a7_click():
    w.list.addItem("sandwitch chawarma 13dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(13)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+13
        w.to.setText(str(a)+"dt")
def yy_click():
    w.list.addItem("pizza escalope 23dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(23)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+23
        w.to.setText(str(a)+"dt")
def zz_click():
    w.list.addItem("pizza margherita 15.800")
    s=w.to.text()
    if s=="":
        w.to.setText(str(15.800)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+1.500
        w.to.setText(str(a)+"dt")
def pp_click():
    w.list.addItem("pizza pepperoni 16.500")
    s=w.to.text()
    if s=="":
        w.to.setText(str(16.500)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+16.500
        w.to.setText(str(a)+"dt")
def eee_click():
    w.list.addItem("pizza hawain 15.500dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(15.500)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+15.500
        w.to.setText(str(a)+"dt")
def tt_click():
    w.list.addItem("pizza viande haché 23dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(23)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+23
        w.to.setText(str(a)+"dt")
def ss_click():
    w.list.addItem("pizza 4 fromage 22dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(22)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+22
        w.to.setText(str(a)+"dt")
def uuu_click():
    w.list.addItem("pizza vegeterien 1500dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(11)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+11
        w.to.setText(str(a)+"dt")
def fff_click():
    w.list.addItem("pizza champignon & huil 25dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(25)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+25
        w.to.setText(str(a)+"dt")
def a21_click():
    w.list.addItem("spanish latte 13dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(13)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+13
        w.to.setText(str(a)+"dt")
def a19_click():
    w.list.addItem("iced thea 9dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(9)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+9
        w.to.setText(str(a)+"dt")
def a23_click():
    w.list.addItem("mojito 7dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(7)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+7
        w.to.setText(str(a)+"dt")
def a22_click():
    w.list.addItem("jus 5.500dt ")
    s=w.to.text()
    if s=="":
        w.to.setText(str(5.500)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+5.500
        w.to.setText(str(a)+"dt")
def a18_click():
    w.list.addItem("matcha 10dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(10)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+10
        w.to.setText(str(a)+"dt")
def a20_click():
    w.list.addItem("vanille latte 11dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(11)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+11
        w.to.setText(str(a)+"dt")
def a17_click():
    w.list.addItem("iced coffee 13dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(13)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+13
        w.to.setText(str(a)+"dt")
def a16_click():
    w.list.addItem("milkshake 12dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(12)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+12
        w.to.setText(str(a)+"dt")
def a30_click():
    w.list.addItem("fondant 7.500dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(7.500)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+7.500
        w.to.setText(str(a)+"dt")
def a31_click():
    w.list.addItem("crèpe sucré 9.800dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(9.800)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+9.800
        w.to.setText(str(a)+"dt")
def a27_click():
    w.list.addItem("pancake 8.700dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(8.700)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+8.700
        w.to.setText(str(a)+"dt")
def a25_click():
    w.list.addItem("tiramissu 9.500dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(9.500)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+1.500
        w.to.setText(str(a)+"dt")
def a26_click():
    w.list.addItem("cheesecake 10dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(10)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+10
        w.to.setText(str(a)+"dt")
def a28_click():
    w.list.addItem("croissant 6dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(6)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+6
        w.to.setText(str(a)+"dt")
def a24_click():
    w.list.addItem("donuts 7dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(7)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+7
        w.to.setText(str(a)+"dt")
def a29_click():
    w.list.addItem("gaufre 11dt")
    s=w.to.text()
    if s=="":
        w.to.setText(str(11)+"dt")
    else:
        s=s[:len(s)-2]
        a=float(s)+11
        w.to.setText(str(a)+"dt")
def effacer_click():
    w.list.clear()
def remise_click():
    t=w.to.text()
    p=float(t[:len(t)-2])
    s=p 
    if w.chek1.isChecked() and w.chek2.isChecked() and w.chek3.isChecked() and w.chek4.isChecked() and w.chek5.isChecked():
        s = p * 0.8
    w.to.setText(str(s) +"dt")
def autre_click():
    w.to.clear()
    w.chek1.setChecked(False)
    w.chek2.setChecked(False)
    w.chek3.setChecked(False)
    w.chek4.setChecked(False)
    w.chek5.setChecked(False)
    w.list.clear()
def coeur(btn):
    if btn.is_red == False:
        btn.setText("🤍")
        btn.is_red = True
    else:
        btn.setText("💚")
        btn.is_red = False
    
def btn1_click():
    w.btn1.is_red = False
    w.btn1.clicked.connect(lambda: coeur(w.btn1))
def btn2_click():
    w.btn2.is_red = False
    w.btn2.clicked.connect(lambda: coeur(w.btn2))
def btn3_click():
    w.btn3.is_red = False
    w.btn3.clicked.connect(lambda: coeur(w.btn3))
def btn4_click():
    w.btn4.is_red = False
    w.btn4.clicked.connect(lambda: coeur(w.btn4))
def btn5_click():
    w.btn5.is_red = False
    w.btn5.clicked.connect(lambda: coeur(w.btn5))
def btn6_click():
    w.btn6.is_red = False
    w.btn6.clicked.connect(lambda: coeur(w.btn6))
def btn7_click():
    w.btn7.is_red = False
    w.btn7.clicked.connect(lambda: coeur(w.btn7))
def btn8_click():
    w.btn8.is_red = False
    w.btn8.clicked.connect(lambda: coeur(w.btn8))
def btn9_click():
    w.btn9.is_red = False
    w.btn9.clicked.connect(lambda: coeur(w.btn9))
def btn10_click():
    w.btn10.is_red = False
    w.btn10.clicked.connect(lambda: coeur(w.btn10))
def btn11_click():
    w.btn11.is_red = False
    w.btn11.clicked.connect(lambda: coeur(w.btn11))
def btn12_click():
    w.btn12.is_red = False
    w.bnt12.clicked.connect(lambda: coeur(w.btn12))
def btn13_click():
    w.btn13.is_red = False
    w.btn13.clicked.connect(lambda: coeur(w.btn13))
def btn14_click():
    w.btn14.is_red = False
    w.btn14.clicked.connect(lambda: coeur(w.btn14))
def btn15_click():
    w.btn15.is_red = False
    w.btn15.clicked.connect(lambda: coeur(w.btn15))
def btn16_click():
    w.btn16.is_red = False
    w.btn16.clicked.connect(lambda: coeur(w.btn16))
def btn17_click():
    w.btn17.is_red = False
    w.btn17.clicked.connect(lambda: coeur(w.btn17))
def btn18_click():
    w.btn18.is_red = False
    w.btn18.clicked.connect(lambda: coeur(w.btn18))
def btn19_click():
    w.btn19.is_red = False
    w.btn19.clicked.connect(lambda: coeur(w.btn19))
def btn20_click():
    w.btn20.is_red = False
    w.btn20.clicked.connect(lambda: coeur(w.btn20))
def btn21_click():
    w.btn21.is_red = False
    w.btn21.clicked.connect(lambda: coeur(w.btn21))
def btn22_click():
    w.btn22.is_red = False
    w.btn22.clicked.connect(lambda: coeur(w.btn22))
def btn23_click():
    w.btn23.is_red = False
    w.btn23.clicked.connect(lambda: coeur(w.btn23))
def btn24_click():
    w.btn24.is_red = False
    w.btn24.clicked.connect(lambda: coeur(w.btn24))
def btn25_click():
    w.btn25.is_red = False
    w.btn25.clicked.connect(lambda: coeur(w.btn25))
def btn26_click():
    w.btn26.is_red = False
    w.btn26.clicked.connect(lambda: coeur(w.btn26))
def btn27_click():
    w.btn27.is_red = False
    w.btn27.clicked.connect(lambda: coeur(w.btn27))
def btn28_click():
    w.btn28.is_red = False
    w.btn28.clicked.connect(lambda: coeur(w.btn28))
def btn29_click():
    w.btn29.is_red = False
    w.btn29.clicked.connect(lambda: coeur(w.btn29))
def btn30_click():
    w.btn30.is_red = False
    w.btn30.clicked.connect(lambda: coeur(w.btn30))
def btn31_click():
    w.btn31.is_red = False
    w.btn31.clicked.connect(lambda: coeur(w.btn31))
def btn32_click():
    w.bt32.is_red = False
    w.btn32.clicked.connect(lambda: coeur(w.btn32))
def btn33_click():
    w.btn33.is_red = False
    w.btn33.clicked.connect(lambda: coeur(w.btn33))
def btn34_click():
    w.btn34.is_red = False
    w.btn34.clicked.connect(lambda: coeur(w.btn34))
def btn35_click():
    w.btn35.is_red = False
    w.btn35.clicked.connect(lambda: coeur(w.btn35))
def btn36_click():
    w.btn36.is_red = False
    w.btn36.clicked.connect(lambda: coeur(w.btn36))
def btn37_click():
    w.btn37.is_red = False
    w.btn37.clicked.connect(lambda: coeur(w.btn37))
def btn38_click():
    w.btn38.is_red = False
    w.btn38.clicked.connect(lambda: coeur(w.btn38))
def btn39_click():
    w.btn39.is_red = False
    w.btn39.clicked.connect(lambda: coeur(w.btn39))
def btn40_click():
    w.btn40.is_red = False
    w.btn40.clicked.connect(lambda: coeur(w.btn40))
def btn42_click():
    w.btn41.is_red = False
    w.btn41.clicked.connect(lambda: coeur(w.btn41))
def btn41_click():
    w.btn42.is_red = False
    w.btn42.clicked.connect(lambda: coeur(w.btn42))
def btn43_click():
    w.btn43.is_red = False
    w.btn43.clicked.connect(lambda: coeur(w.btn43))  
def btn44_click():
    w.btn44.is_red = False
    w.btn44.clicked.connect(lambda: coeur(w.btn44))
def btn45_click():
    w.btn45.is_red = False
    w.btn45.clicked.connect(lambda: coeur(w.btn45))
def btn46_click():
    w.btn46.is_red = False
    w.btn46.clicked.connect(lambda: coeur(w.btn46))
def btn47_click():
    w.btn47.is_red = False
    w.btn47.clicked.connect(lambda: coeur(w.btn47))
def btn48_click():
    w.btn48.is_red = False
    w.btn48.clicked.connect(lambda: coeur(w.btn48))
app = QApplication([])
w =  loadUi ("C:/projet informatique/caissee2.ui")
w.show()
w.dd.clicked.connect ( dd_click )
w.aa.clicked.connect ( aa_click )
w.ee.clicked.connect ( ee_click )
w.ff.clicked.connect ( ff_click )
w.hh.clicked.connect ( hh_click )
w.bb.clicked.connect ( bb_click )
w.cc.clicked.connect ( cc_click )
w.gg.clicked.connect ( gg_click )
w.kk.clicked.connect ( kk_click )
w.ww.clicked.connect ( ww_click )
w.xx.clicked.connect ( xx_click )
w.mm.clicked.connect ( mm_click )
w.ll.clicked.connect ( ll_click )
w.nn.clicked.connect ( nn_click )
w.vv.clicked.connect ( vv_click )
w.aaa.clicked.connect ( aaa_click )
w.a6.clicked.connect ( a6_click )
w.ttt.clicked.connect ( ttt_click )
w.a3.clicked.connect ( a3_click )
w.a4.clicked.connect ( a4_click )
w.a1.clicked.connect ( a1_click )
w.a5.clicked.connect ( a5_click )
w.a7.clicked.connect ( a7_click )
w.yy.clicked.connect ( yy_click )
w.zz.clicked.connect ( zz_click )
w.pp.clicked.connect ( pp_click )
w.eee.clicked.connect ( eee_click )
w.tt.clicked.connect ( tt_click )
w.ss.clicked.connect ( ss_click )
w.uuu.clicked.connect ( uuu_click )
w.fff.clicked.connect ( fff_click )
w.a8.clicked.connect ( a8_click )
w.a21.clicked.connect ( a21_click )
w.a19.clicked.connect ( a19_click )
w.a23.clicked.connect ( a23_click )
w.a22.clicked.connect ( a22_click )
w.a18.clicked.connect ( a18_click )
w.a20.clicked.connect ( a20_click )
w.a17.clicked.connect ( a17_click )
w.a16.clicked.connect ( a16_click )
w.a30.clicked.connect ( a30_click )
w.a31.clicked.connect ( a31_click )
w.a27.clicked.connect ( a27_click )
w.a25.clicked.connect ( a25_click )
w.a26.clicked.connect ( a26_click )
w.a28.clicked.connect ( a28_click )
w.a24.clicked.connect ( a24_click )
w.a29.clicked.connect ( a29_click )
w.autre.clicked.connect ( autre_click )
w.effacer.clicked.connect ( effacer_click )
w.remise.clicked.connect ( remise_click )
w.btn1.clicked.connect ( btn1_click )
w.btn2.clicked.connect ( btn2_click )
w.btn3.clicked.connect ( btn3_click )
w.btn4.clicked.connect ( btn4_click )
w.btn5.clicked.connect ( btn5_click )
w.btn6.clicked.connect ( btn6_click )
w.btn7.clicked.connect ( btn7_click )
w.btn8.clicked.connect ( btn8_click )
w.btn9.clicked.connect ( btn9_click )
w.btn10.clicked.connect ( btn10_click )
w.btn11.clicked.connect ( btn11_click )
w.btn12.clicked.connect ( btn12_click )
w.btn13.clicked.connect ( btn13_click )
w.btn14.clicked.connect ( btn14_click )
w.btn15.clicked.connect ( btn15_click )
w.btn16.clicked.connect ( btn16_click )
w.btn17.clicked.connect ( btn17_click )
w.btn18.clicked.connect ( btn18_click )
w.btn19.clicked.connect ( btn19_click )
w.btn20.clicked.connect ( btn20_click )
w.btn21.clicked.connect ( btn21_click )
w.btn22.clicked.connect ( btn22_click )
w.btn23.clicked.connect ( btn23_click )
w.btn24.clicked.connect ( btn24_click )
w.btn25.clicked.connect ( btn25_click )
w.btn26.clicked.connect ( btn26_click )
w.btn27.clicked.connect ( btn27_click )
w.btn28.clicked.connect ( btn28_click )
w.btn29.clicked.connect ( btn29_click )
w.btn30.clicked.connect ( btn30_click )
w.btn31.clicked.connect ( btn31_click )
w.btn32.clicked.connect ( btn32_click )
w.btn33.clicked.connect ( btn33_click )
w.btn34.clicked.connect ( btn34_click )
w.btn35.clicked.connect ( btn35_click )
w.btn36.clicked.connect ( btn36_click )
w.btn37.clicked.connect ( btn37_click )
w.btn38.clicked.connect ( btn38_click )
w.btn39.clicked.connect ( btn39_click )
w.btn40.clicked.connect ( btn40_click )
w.btn41.clicked.connect ( btn41_click )
w.btn42.clicked.connect ( btn42_click )
w.btn43.clicked.connect ( btn43_click )
w.btn44.clicked.connect ( btn44_click )
w.btn45.clicked.connect ( btn45_click )
w.btn46.clicked.connect ( btn46_click )
w.btn47.clicked.connect ( btn47_click )
w.btn48.clicked.connect ( btn48_click )

app.exec_()