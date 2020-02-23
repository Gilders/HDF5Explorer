# -*- coding: utf-8 -*-
"""
@author: Onera
"""

import numpy as np
import h5py as h5
import pyqtgraph as pg
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtGui, QtCore


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
