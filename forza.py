import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
from PyQt6 import uic

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'C:\Users\seby_\Desktop\Info\fh5\Forza Randomizer\forza.ui', self)
        self.button.clicked.connect(self.click)
        self.setWindowTitle('Forza Horizon 5 Randomizer')
    
    def click(self):
        #upgrade
        div = random.randrange(self.slider.value(), 7)
        if(div==1):
            upgrade = "D CLASS"
        elif(div==2):
            upgrade = "C CLASS"
        elif(div==3):
            upgrade = "B CLASS"
        elif(div==4):
            upgrade = "A CLASS"
        elif(div==5):
            upgrade = "S1 CLASS"
        else:
            upgrade = "S2 CLASS OR MAX PI"
        self.result.setText(upgrade)
        #race
        a=['ROAD', 'DIRT', 'CROSS COUNTRY', 'STREET']
        road=['Bahia de plano circuit','Arch of mulege circuit','Los jardines circuit','Chihuahua circuit','Tierra prospera circuit','Playa azul circuit','Lookout circuit','Horizon Mexico circuit','Emerald circuit','Dunas blancas sprint','Descansar dorado sprint','Estadio circuit','Cathedral circuit','Reservorio sprint','Copper canyon sprint','Volcan sprint','Gran pantano sprint','Sierra verde sprint','Plaza circuit','Llanuras sprint','Panoramica sprint','Riviera sprint','Bola ocho circuit','The Goliath','The Colossus']
        dirt=['River scramble','Mangrove scramble','Mulege town scramble','San juan scramble','Horizon BAJA scramble','Teotihuacan scramble','Caldera scramble','La selva scramble','El pipila scramble','Cascada trail','Montana trail','Desierto trail','Baja California trail','Bajio trail','Cordillera trail','Tapalpa trail','Fuera del camino trail','Tulum trail','Barranca trail','The Gauntlet']
        cross=['Baja CC circuit','Costera CC circuit','Cstadio CC circuit','Las ranas CC','Urban CC circuit','Las dunas CC','Ribera rocosa CC','Costa este CC','El descenso CC','Oasis CC','Tropico CC','Las granjas CC','Restos CC','Foto final CC','Ek\' Balam CC circuit','Copper canyon CC','Herencia CC circuit','Airfield CC circuit','The Titan','Festival CC']
        street=['El lago blanco','Ruta norte','Festival gatecrash','Coast run','Carretera chase','Costa rocosa','Horizon callejera','Hilltop descent','Jungle descent','Las laderas','Granjas de tapalpa','Wetland charge','Las afueras','Cruce del valle','Tunnel run','Bosque del sur','Guanajato sur','Highland climb','Canon run','Castillo del mar','The Marathon']
        season=random.choice(['Hot season','Wet season','Dry season','Storm season'])
        if (season == 'Hot season'):
            weather = random.choice(['Clear','Clear post rain','Cloudy','Cloudy post rain','Overcast','Heavy precipitation','Light precipitation','Dust storm','Gale','Fog'])
        elif(season == 'Storm season'):
            weather = random.choice(['Clear','Clear post rain','Cloudy','Cloudy post rain','Overcast','Heavy precipitation','Light precipitation','Tropical storm','Gale','Fog'])
        else:
            weather = random.choice(['Clear','Clear post rain','Cloudy','Cloudy post rain','Overcast','Heavy precipitation','Light precipitation','Gale','Fog'])
        time = random.choice(['Dawn','Sunrise','Morning','Early afternoon','Late afternoon','Sunset','Evening','Night'])
        type = random.choice(a)
        if (type == 'ROAD'):
            race = random.choice(road)
        elif (type == 'DIRT'):
            race = random.choice(dirt)
        elif (type =='CROSS COUNTRY'):
            race = random.choice(cross)
        elif (type=='STREET'):
            race = random.choice(street)
        self.settings.setText('<br>'.join([type, race, season, weather, time]))

if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing window...')

