# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:43:45 2019

@author: admin
"""

import sys
import numpy as np
import h5py as h5
import pyqtgraph as pg
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtGui, QtCore

#%% GUI de l'application

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1193, 801)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphclass1 = PyQtGraphWid1(self.centralwidget)
        self.graphclass1.setObjectName(_fromUtf8("graphclass1"))
        self.gridLayout.addWidget(self.graphclass1, 0, 0, 1, 1)
        self.graphclass2 = PyQtGraphWid2(self.centralwidget)
        self.graphclass2.setObjectName(_fromUtf8("graphclass2"))
        self.gridLayout.addWidget(self.graphclass2, 0, 1, 1, 1)
        self.graphclass3 = PyQtGraphWid3(self.centralwidget)
        self.graphclass3.setObjectName(_fromUtf8("graphclass3"))
        self.gridLayout.addWidget(self.graphclass3, 1, 0, 1, 1)
        self.graphclass4 = PyQtGraphWid4(self.centralwidget)
        self.graphclass4.setObjectName(_fromUtf8("graphclass4"))
        self.gridLayout.addWidget(self.graphclass4, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuImage = QtGui.QMenu(self.menubar)
        self.menuImage.setObjectName(_fromUtf8("menuImage"))
        self.menuFond = QtGui.QMenu(self.menubar)
        self.menuFond.setObjectName(_fromUtf8("menuFond"))
        self.menuAfficher_cacher = QtGui.QMenu(self.menubar)
        self.menuAfficher_cacher.setObjectName(_fromUtf8("menuAfficher_cacher"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenMono = QtGui.QAction(MainWindow)
        self.actionOpenMono.setObjectName(_fromUtf8("actionOpenMono"))
        self.actionOpenMulti = QtGui.QAction(MainWindow)
        self.actionOpenMulti.setObjectName(_fromUtf8("actionOpenMulti"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionOpenImg1 = QtGui.QAction(MainWindow)
        self.actionOpenImg1.setObjectName(_fromUtf8("actionOpenImg1"))
        self.actionOpenImg2 = QtGui.QAction(MainWindow)
        self.actionOpenImg2.setObjectName(_fromUtf8("actionOpenImg2"))
        self.actionOpenImg3 = QtGui.QAction(MainWindow)
        self.actionOpenImg3.setObjectName(_fromUtf8("actionOpenImg3"))
        self.actionOpenImg4 = QtGui.QAction(MainWindow)
        self.actionOpenImg4.setObjectName(_fromUtf8("actionOpenImg4"))
        self.actionBackAll = QtGui.QAction(MainWindow)
        self.actionBackAll.setObjectName(_fromUtf8("actionBackAll"))
        self.actionBack1 = QtGui.QAction(MainWindow)
        self.actionBack1.setObjectName(_fromUtf8("actionBack1"))
        self.actionBack2 = QtGui.QAction(MainWindow)
        self.actionBack2.setObjectName(_fromUtf8("actionBack2"))
        self.actionBack3 = QtGui.QAction(MainWindow)
        self.actionBack3.setObjectName(_fromUtf8("actionBack3"))
        self.actionBack4 = QtGui.QAction(MainWindow)
        self.actionBack4.setObjectName(_fromUtf8("actionBack4"))
        self.actionCacher1 = QtGui.QAction(MainWindow)
        self.actionCacher1.setObjectName(_fromUtf8("actionCacher1"))
        self.actionCacher2 = QtGui.QAction(MainWindow)
        self.actionCacher2.setObjectName(_fromUtf8("actionCacher2"))
        self.actionCacher3 = QtGui.QAction(MainWindow)
        self.actionCacher3.setObjectName(_fromUtf8("actionCacher3"))
        self.actionCacher4 = QtGui.QAction(MainWindow)
        self.actionCacher4.setObjectName(_fromUtf8("actionCacher4"))
        self.actionFondhide1 = QtGui.QAction(MainWindow)
        self.actionFondhide1.setObjectName(_fromUtf8("actionFondhide1"))
        self.actionFondhide2 = QtGui.QAction(MainWindow)
        self.actionFondhide2.setObjectName(_fromUtf8("actionFondhide2"))
        self.actionFondhide3 = QtGui.QAction(MainWindow)
        self.actionFondhide3.setObjectName(_fromUtf8("actionFondhide3"))
        self.actionFondhide4 = QtGui.QAction(MainWindow)
        self.actionFondhide4.setObjectName(_fromUtf8("actionFondhide4"))
        self.actionCacherAll = QtGui.QAction(MainWindow)
        self.actionCacherAll.setObjectName(_fromUtf8("actionCacherAll"))
        self.actionFondhideAll = QtGui.QAction(MainWindow)
        self.actionFondhideAll.setObjectName(_fromUtf8("actionFondhideAll"))
        self.menuFichier.addAction(self.actionOpenMono)
        self.menuFichier.addAction(self.actionOpenMulti)
        self.menuFichier.addAction(self.actionQuit)
        self.menuImage.addAction(self.actionOpenImg1)
        self.menuImage.addAction(self.actionOpenImg2)
        self.menuImage.addAction(self.actionOpenImg3)
        self.menuImage.addAction(self.actionOpenImg4)
        self.menuFond.addAction(self.actionBackAll)
        self.menuFond.addAction(self.actionBack1)
        self.menuFond.addAction(self.actionBack2)
        self.menuFond.addAction(self.actionBack3)
        self.menuFond.addAction(self.actionBack4)
        self.menuAfficher_cacher.addAction(self.actionCacher1)
        self.menuAfficher_cacher.addAction(self.actionCacher2)
        self.menuAfficher_cacher.addAction(self.actionCacher3)
        self.menuAfficher_cacher.addAction(self.actionCacher4)
        self.menuAfficher_cacher.addAction(self.actionFondhide1)
        self.menuAfficher_cacher.addAction(self.actionFondhide2)
        self.menuAfficher_cacher.addAction(self.actionFondhide3)
        self.menuAfficher_cacher.addAction(self.actionFondhide4)
        self.menuAfficher_cacher.addAction(self.actionCacherAll)
        self.menuAfficher_cacher.addAction(self.actionFondhideAll)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuFond.menuAction())
        self.menubar.addAction(self.menuAfficher_cacher.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "H5viewer 3", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuImage.setTitle(_translate("MainWindow", "Image", None))
        self.menuFond.setTitle(_translate("MainWindow", "Fond", None))
        self.menuAfficher_cacher.setTitle(_translate("MainWindow", "Afficher/cacher", None))
        self.actionOpenMono.setText(_translate("MainWindow", "Ouvrir fichier une voie", None))
        self.actionOpenMulti.setText(_translate("MainWindow", "Ouvrir fichier multi-voies", None))
        self.actionQuit.setText(_translate("MainWindow", "Quitter", None))
        self.actionOpenImg1.setText(_translate("MainWindow", "Nouvelle image 1", None))
        self.actionOpenImg2.setText(_translate("MainWindow", "Nouvelle image 2", None))
        self.actionOpenImg3.setText(_translate("MainWindow", "Nouvelle image 3", None))
        self.actionOpenImg4.setText(_translate("MainWindow", "Nouvelle image 4", None))
        self.actionBackAll.setText(_translate("MainWindow", "Charger fond multi-voies", None))
        self.actionBack1.setText(_translate("MainWindow", "Charger fond image 1", None))
        self.actionBack2.setText(_translate("MainWindow", "Charger fond image 2", None))
        self.actionBack3.setText(_translate("MainWindow", "Charger fond image 3", None))
        self.actionBack4.setText(_translate("MainWindow", "Charger fond image 4", None))
        self.actionCacher1.setText(_translate("MainWindow", "Image 1", None))
        self.actionCacher2.setText(_translate("MainWindow", "Image 2", None))
        self.actionCacher3.setText(_translate("MainWindow", "Image 3", None))
        self.actionCacher4.setText(_translate("MainWindow", "Image 4", None))
        self.actionFondhide1.setText(_translate("MainWindow", "Fond 1", None))
        self.actionFondhide2.setText(_translate("MainWindow", "Fond 2", None))
        self.actionFondhide3.setText(_translate("MainWindow", "Fond 3", None))
        self.actionFondhide4.setText(_translate("MainWindow", "Fond 4", None))
        self.actionCacherAll.setText(_translate("MainWindow", "Toutes les images", None))
        self.actionFondhideAll.setText(_translate("MainWindow", "Tous les fond", None))





#%% Classe d'affichage du graph ou des images

#----------- Variables globales ------------
file_fond1 = []
file_mire1 = []
result_image1 = []
file_fond2 = []
file_mire2 = []
result_image2 = []
file_fond3 = []
file_mire3 = []
result_image3 = []
file_fond4 = []
file_mire4 = []
result_image4 = []


here1 = False
here2 = False
here3 = False
here4 = False
Back1 = False
Back2 = False
Back3 = False
Back4 = False
trigg = False


#-------------------------------------------



class PyQtGraphWid1(pg.ImageView):
    def __init__(self, parent=None, **kargs):
        pg.ImageView.__init__(self, **kargs)
        self.setParent(parent)
#        self.setWindowTitle('Acquistion microbolometre : single camera')

    def open_raw(self):
        global file_mire1

        getimg = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir un fichier H5 d'images d'acquisition",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        pathimg = getimg[0]
        file_mire1 = h5.File(str(pathimg),'r')
        print("New file is opened")



    def processing_img_mono(self):
        global file_mire1
        global result_image1

        group = file_mire1.get('groupe1')
        datasetlist = list(group.keys())
        key1 = datasetlist[0]
        data_tempo = np.array(group.get(key1))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))

        result_image1 = np.float32(img0)
        print("Image 1 is processed")


    def processing_img(self):
        global file_mire1
        global result_image1

#        grouplist = list(file_mire1.keys())
#        print "Liste des groupes du fichier: \n"
#        print grouplist
        group = file_mire1.get('groupe1')
        datasetlist = list(group.keys())
#        print "List of datasets in this file: \n"
#        print datasetlist
        key1 = datasetlist[1]
        data_tempo = np.array(group.get(key1))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))

        result_image1 = np.float32(img0)
        print("Image 1 is processed")



    def displaying(self):
        global result_image1

        plt.imshow(result_image1)  # ==> images en couleurs
        plt.colorbar()
        self.setImage(np.transpose(result_image1))

        plt.imshow(result_image1)  # ==> images en couleurs
        plt.colorbar()
        self.setImage(np.transpose(result_image1))

        print("Image 1 is displayed")
        print("------------------\n")

    def camouf(self):
        global here1
        if here1 == False:
            self.hide()
            here1 = True
        else:
            self.show()
            here1 = False



    def open_fond(self):
        global file_fond1

        getimg = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir le fichier H5 de fond",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        pathimg = getimg[0]
        file_fond1 = h5.File(str(pathimg),'r')


    def processing_fond(self):
        global file_fond1
        global file_mire1
        global Back1
        global result_image1
        global backfloat1

        group = file_mire1.get('groupe1')
        datasetlist = list(group.keys())
        key1 = datasetlist[1]
        data_tempo = np.array(group.get(key1))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))
        result_image1 = np.float32(img0)

        groupf = file_fond1.get('groupe1')
        datasetlistf = list(groupf.keys())
        key1f = datasetlistf[1]
        d_temp_fond = np.array(groupf.get(key1f))

        img0_fond = d_temp_fond[0].reshape((480, 640))
        backfloat1 = np.float32(img0_fond)
        result_image1 = result_image1-backfloat1
        Back1 = True

    def processing_fond_mono(self):
        global file_fond1
        global file_mire1
        global Back1
        global result_image1
        global backfloat1

        group = file_mire1.get('groupe1')
        datasetlist = list(group.keys())
        key1 = datasetlist[0]
        data_tempo = np.array(group.get(key1))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))
        result_image1 = np.float32(img0)

        groupf = file_fond1.get('groupe1')
        datasetlistf = list(groupf.keys())
        key1f = datasetlistf[0]
        d_temp_fond = np.array(groupf.get(key1f))

        img0_fond = d_temp_fond[0].reshape((480, 640))
        backfloat1 = np.float32(img0_fond)
        result_image1 = result_image1-backfloat1
        Back1 = True


    def displaying_fond(self):
        global file_fond1
        global result_image1
        global Back1
        global backfloat1


        if Back1 == True:
            result_image1 = result_image1 + backfloat1
            Back1 = False
        else:
            result_image1 = result_image1 - backfloat1
            Back1 = True



###########################################################################"
############################################################################


class PyQtGraphWid2(pg.ImageView):
    def __init__(self, parent=None, **kargs):
        pg.ImageView.__init__(self, **kargs)
        self.setParent(parent)
#        self.setWindowTitle('Acquistion microbolometre : single camera')

    def open_raw(self):
        global file_mire2

        getimg = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir un fichier H5 d'images d'acquisition",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        pathimg = getimg[0]
        file_mire2 = h5.File(str(pathimg),'r')
        print("New file is opened")




    def processing_img(self):
        global file_mire2
        global result_image2

#        grouplist = list(file_mire2.keys())
#        print "Liste des groupes du fichier: \n"
#        print grouplist
        group = file_mire2.get('groupe1')
        datasetlist = list(group.keys())
#        print "List of datasets in this file: \n"
#        print datasetlist
        key2 = datasetlist[2]
        data_tempo = np.array(group.get(key2))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))
        result_image2 = np.float32(img0)
        print("Image 2 is processed")


    def displaying(self):
        global result_image2

        plt.imshow(result_image2)  # ==> images en couleurs
        plt.colorbar()
        self.setImage(np.transpose(result_image2))

        plt.imshow(result_image2)  # ==> images en couleurs
        plt.colorbar()
        self.setImage(np.transpose(result_image2))

        print("Image 2 is displayed")
        print("------------------\n")

    def camouf(self):
        global here2
        if here2 == False:
            self.hide()
            here2 = True
        else:
            self.show()
            here2 = False

    def open_fond(self):
        global file_fond2


        getimg = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir le fichier H5 de fond",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        pathimg = getimg[0]
        file_fond2 = h5.File(str(yiv),'r')



    def processing_fond(self):
        global file_fond2
        global file_mire2
        global Back2
        global result_image2
        global backfloat2

        group = file_mire2.get('groupe1')
        datasetlist = list(group.keys())
        key2 = datasetlist[2]
        data_tempo = np.array(group.get(key2))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))
        result_image2 = np.float32(img0)

        groupf = file_fond2.get('groupe1')
        datasetlistf = list(groupf.keys())
        key2f = datasetlistf[2]
        d_temp_fond = np.array(groupf.get(key2f))

        img0_fond = d_temp_fond[0].reshape((480, 640))
        backfloat2 = np.float32(img0_fond)
        result_image2 = result_image2-backfloat2
        Back2 = True

    def displaying_fond(self):
        global file_fond2
        global result_image2
        global Back2
        global backfloat2

        if Back2 == True:
            result_image2 = result_image2 + backfloat2
            Back2 = False
        else:
            result_image2 = result_image2 - backfloat2
            Back2 = True





#############################################################################
#############################################################################





class PyQtGraphWid3(pg.ImageView):
    def __init__(self, parent=None, **kargs):
        pg.ImageView.__init__(self, **kargs)
        self.setParent(parent)
#        self.setWindowTitle('Acquistion microbolometre : single camera')

    def open_raw(self):
        global file_mire3

        getimg = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir un fichier H5 d'images d'acquisition",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        pathimg = getimg[0]
        file_mire3 = h5.File(str(pathimg),'r')
        print("New file is opened")

    def open_rawAll(self):
        global file_mire1
        global file_mire2
        global file_mire3
        global file_mire4

        getimg = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir un fichier H5 d'images d'acquisition",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        pathimg = getimg[0]
        file_mire1 = h5.File(str(pathimg),'r')
        file_mire2 = file_mire1
        file_mire3 = file_mire1
        file_mire4 = file_mire1
        print("New files are opened")




    def processing_img(self):
        global file_mire3
        global result_image3

#        grouplist = list(file_mire2.keys())
#        print "Liste des groupes du fichier: \n"
#        print grouplist
        group = file_mire3.get('groupe1')
        datasetlist = list(group.keys())
#        print "List of datasets in this file: \n"
#        print datasetlist
        key3 = datasetlist[3]
        data_tempo = np.array(group.get(key3))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))
        result_image3 = np.float32(img0)
        print("Image 3 is processed")


    def displaying(self):
        global result_image3

        plt.imshow(result_image3)  # ==> images en couleurs
        plt.colorbar()
        self.setImage(np.transpose(result_image3))

        plt.imshow(result_image3)  # ==> images en couleurs
        plt.colorbar()
        self.setImage(np.transpose(result_image3))

        print("Image 3 is displayed")
        print("------------------\n")

    def camouf(self):
        global here3
        if here3 == False:
            self.hide()
            here3 = True
        else:
            self.show()
            here3 = False

    def open_fond(self):
        global file_fond3

        getimg = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir le fichier H5 de fond",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        pathimg = getimg[0]
        file_fond3 = h5.File(str(pathimg),'r')


    def processing_fond(self):
        global file_fond3
        global file_mire3
        global Back3
        global result_image3
        global backfloat3

        group = file_mire3.get('groupe1')
        datasetlist = list(group.keys())
        key3 = datasetlist[3]
        data_tempo = np.array(group.get(key3))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))
        result_image3 = np.float32(img0)

        groupf = file_fond3.get('groupe1')
        datasetlistf = list(groupf.keys())
        key3f = datasetlistf[3]
        d_temp_fond = np.array(groupf.get(key3f))

        img0_fond = d_temp_fond[0].reshape((480, 640))
        backfloat3 = np.float32(img0_fond)
        result_image3 = result_image3-backfloat3
        Back3 = True

    def open_fondAll(self):
        global file_fond3
        global file_fond1
        global file_fond2
        global file_fond4

        getimg = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir le fichier H5 de fond",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        pathimg = getimg[0]
        file_fond3 = h5.File(str(pathimg),'r')
        file_fond2 = file_fond3
        file_fond1 = file_fond3
        file_fond4 = file_fond3
        Process1 = PyQtGraphWid1()
        Process2 = PyQtGraphWid2()
        Process4 = PyQtGraphWid4()
        Process1.processing_fond()
        Process2.processing_fond()
        Process4.processing_fond()
        self.processing_fond()


    def displaying_fond(self):
        global file_fond3
        global result_image3
        global Back3
        global backfloat3


        if Back3 == True:
            result_image3 = result_image3 + backfloat3
            Back3 = False
        else:
            result_image3 = result_image3 - backfloat3
            Back3 = True

#############################################################################
#############################################################################

class PyQtGraphWid4(pg.ImageView):
    def __init__(self, parent=None, **kargs):
        pg.ImageView.__init__(self, **kargs)
        self.setParent(parent)
#        self.setWindowTitle('Acquistion microbolometre : single camera')

    def open_raw(self):
        global file_mire4

        getimg = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir un fichier H5 d'images d'acquisition",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        pathimg = getimg[0]
        file_mire4 = h5.File(str(pathimg),'r')
        print("New file is opened")




    def processing_img(self):
        global file_mire4
        global result_image4

#        grouplist = list(file_mire2.keys())
#        print "Liste des groupes du fichier: \n"
#        print grouplist
        group = file_mire4.get('groupe1')
        datasetlist = list(group.keys())
#        print "List of datasets in this file: \n"
#        print datasetlist
        key4 = datasetlist[4]
        data_tempo = np.array(group.get(key4))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))
        result_image4 = np.float32(img0)
        print("Image 2 is processed")


    def displaying(self):
        global result_image4

        plt.imshow(result_image4)  # ==> images en couleurs
        plt.colorbar()
        self.setImage(np.transpose(result_image4))

        plt.imshow(result_image4)  # ==> images en couleurs
        plt.colorbar()
        self.setImage(np.transpose(result_image4))

        print("Image 4 is displayed")
        print("------------------\n")

    def camouf(self):
        global here4
        if here4 == False:
            self.hide()
            here4 = True
        else:
            self.show()
            here4 = False

    def open_fond(self):
        global file_fond4


        yiv = QtGui.QFileDialog.getOpenFileName(self,"Ouvrir le fichier H5 de fond",QtCore.QDir.homePath(),"Fichiers H5 (*.hdf5 *.h5)")
        file_fond4 = h5.File(str(yiv),'r')



    def processing_fond(self):
        global file_fond4
        global file_mire4
        global Back4
        global result_image4
        global backfloat4

        group = file_mire4.get('groupe1')
        datasetlist = list(group.keys())
        key4 = datasetlist[4]
        data_tempo = np.array(group.get(key4))

        img0 = data_tempo[0] # ==> dans ce cas on a ==> array([[32398, 32333, 32566, ..., 33886, 33556, 33839]], dtype=uint16)
        img0 = img0.reshape((480, 640))
        result_image4 = np.float32(img0)

        groupf = file_fond4.get('groupe1')
        datasetlistf = list(groupf.keys())
        key4f = datasetlistf[4]
        d_temp_fond = np.array(groupf.get(key4f))

        img0_fond = d_temp_fond[0].reshape((480, 640))
        backfloat4 = np.float32(img0_fond)
        result_image4 = result_image4-backfloat4
        Back4 = True

    def displaying_fond(self):
        global file_fond4
        global result_image4
        global Back4
        global backfloat4

        if Back4 == True:
            result_image4 = result_image4 + backfloat4
            Back4 = False
        else:
            result_image4 = result_image4 - backfloat4
            Back4 = True



#%%###########################################################################
#
#   Classe principale hériatant de l'interface importé et générant les actions
#
##############################################################################

print("Running.")
print("____________________________________________________________________\n")


class Main(QtGui.QMainWindow, Ui_MainWindow):
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
