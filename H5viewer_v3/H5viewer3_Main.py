# -*- coding: utf-8 -*-
"""
Fichier de lancement.
@author: Adrien
"""

from PyQt5 import QtGui
import sys

import H5viewer4_guitest  # On importe notre fichier de config interface (.ui)
            # convertie en .py via "pyuic <>.ui -o <>.py"



#%%###########################################################################
#
#   Classe principale hériatant de l'interface importé et générant les actions
#rt
##############################################################################

print("Running.")
print("____________________________________________________________________\n")


class Main(QtGui.QMainWindow, H5viewer4_guitest.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)                                      # Initialisation du GUI
        self.connectActions()                                   # Lancement de la methode de déclenchement des actions

    def connectActions(self):                                   # Methode liant les actions UI aux fonctions du programme
        self.actionQuit.triggered.connect(self.close_window)
        self.actionOpenMulti.triggered.connect(self.load_imageAll)
        self.actionOpenMono.triggered.connect(self.load_imageSingle)
        self.actionOpenImg1.triggered.connect(self.load_image1)
        self.actionOpenImg2.triggered.connect(self.load_image2)
        self.actionOpenImg3.triggered.connect(self.load_image3)
        self.actionOpenImg4.triggered.connect(self.load_image4)

        self.actionCacher1.triggered.connect(self.cache_img1)
        self.actionCacher2.triggered.connect(self.cache_img2)
        self.actionCacher3.triggered.connect(self.cache_img3)
        self.actionCacher4.triggered.connect(self.cache_img4)

        self.actionCacherAll.triggered.connect(self.cache_imgAll)
        self.actionBackAll.triggered.connect(self.load_fondAll)
        self.actionBack1.triggered.connect(self.load_back1)
        self.actionBack2.triggered.connect(self.load_back2)
        self.actionBack3.triggered.connect(self.load_back3)
        self.actionBack4.triggered.connect(self.load_back4)

        self.actionFondhide1.triggered.connect(self.cache_back1)
        self.actionFondhide2.triggered.connect(self.cache_back2)
        self.actionFondhide3.triggered.connect(self.cache_back3)
        self.actionFondhide4.triggered.connect(self.cache_back4)

        self.actionFondhideAll.triggered.connect(self.cache_backAll)



    def load_imageAll(self):                                       # Methode invoquant les fonctions du widget d'affichage
        global trigg
        trigg = False
        self.graphclass1.show()
        self.graphclass2.show()
        self.graphclass3.show()
        self.graphclass4.show()
        self.graphclass3.open_rawAll()
        self.graphclass1.processing_img()
        self.graphclass1.displaying()
        self.graphclass2.processing_img()
        self.graphclass2.displaying()
        self.graphclass3.processing_img()
        self.graphclass3.displaying()
        self.graphclass4.processing_img()
        self.graphclass4.displaying()


    def load_imageSingle(self):                                       # Methode invoquant les fonctions du widget d'affichage
        global trigg
        trigg = True
        self.graphclass1.show()
        self.graphclass2.hide()
        self.graphclass3.hide()
        self.graphclass4.hide()
        self.graphclass1.open_raw()
        self.graphclass1.processing_img_mono()
        self.graphclass1.displaying()

    def load_image1(self):
        global trigg
        trigg = False
        self.graphclass1.show()
        self.graphclass1.open_raw()
        self.graphclass1.processing_img()
        self.graphclass1.displaying()

    def load_image2(self):
        self.graphclass2.show()
        self.graphclass2.open_raw()
        self.graphclass2.processing_img()
        self.graphclass2.displaying()

    def load_image3(self):
        self.graphclass3.show()
        self.graphclass3.open_raw()
        self.graphclass3.processing_img()
        self.graphclass3.displaying()

    def load_image4(self):
        self.graphclass4.show()
        self.graphclass4.open_raw()
        self.graphclass4.processing_img()
        self.graphclass4.displaying()


    def load_fondAll(self):
        self.graphclass3.open_fondAll()
        self.graphclass1.displaying()
        self.graphclass2.displaying()
        self.graphclass3.displaying()
        self.graphclass4.displaying()


    def load_back1(self):
        global trigg

        self.graphclass1.open_fond()
        if trigg == False:
            self.graphclass1.processing_fond()
        else:
            self.graphclass1.processing_fond_mono()
        self.graphclass1.displaying()



    def load_back2(self):
        self.graphclass2.open_fond()
        self.graphclass2.processing_fond()
        self.graphclass2.displaying()


    def load_back3(self):
        self.graphclass3.open_fond()
        self.graphclass3.processing_fond()
        self.graphclass3.displaying()

    def load_back4(self):
        self.graphclass4.open_fond()
        self.graphclass4.processing_fond()
        self.graphclass4.displaying()


    def cache_img1(self):
        self.graphclass1.camouf()

    def cache_img2(self):
        self.graphclass2.camouf()

    def cache_img3(self):
        self.graphclass3.camouf()

    def cache_img4(self):
        self.graphclass4.camouf()


    def cache_imgAll(self):
        self.graphclass1.camouf()
        self.graphclass2.camouf()
        self.graphclass3.camouf()
        self.graphclass4.camouf()

    def cache_backAll(self):
        self.graphclass1.displaying_fond()
        self.graphclass1.displaying()
        self.graphclass2.displaying_fond()
        self.graphclass2.displaying()
        self.graphclass3.displaying_fond()
        self.graphclass3.displaying()
        self.graphclass4.displaying_fond()
        self.graphclass4.displaying()


    def cache_back1(self):
        self.graphclass1.displaying_fond()
        self.graphclass1.displaying()

    def cache_back2(self):
        self.graphclass2.displaying_fond()
        self.graphclass2.displaying()

    def cache_back3(self):
        self.graphclass3.displaying_fond()
        self.graphclass3.displaying()

    def cache_back4(self):
        self.graphclass4.displaying_fond()
        self.graphclass4.displaying()


    def close_window(self): #Action de fermeture
        self.close()
        print("_____________________________________________________________\n")
        print("Closing.")




if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    imageViewer = Main()
    imageViewer.show()
    app.exec_()
