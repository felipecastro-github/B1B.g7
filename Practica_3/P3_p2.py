#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Sitema de visualización (primer esquema)
# Generated: Fri Oct 04 2019
##################################################
from gnuradio import gr
from gnuradio import audio
from gnuradio import analog
from PyQt5 import QtWidgets,QtCore,Qt
from gnuradio import qtgui
from gnuradio import blocks
from gnuradio.filter import firdes
import sys, sip
#######################################################
class esquema(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
        self.qapp = Qt.QApplication(sys.argv)

        sample_rate = 32000
        samp_rate = 16e3
        fftsize = 2048
	ampl = 0.1
        self.src0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 350, ampl)
        self.src1 = analog.noise_source_f(analog.GR_GAUSSIAN, ampl)
        self.dst = audio.sink(sample_rate, "")
        self.add = blocks.add_ff()
        self.thr = blocks.throttle(gr.sizeof_gr_complex, samp_rate, True)

        self.snk = qtgui.sink_f(fftsize,firdes.WIN_BLACKMAN_hARRIS,0,samp_rate,"",True,True,True,True)

        self.connect(self.src0, (self.dst, 0))
        self.connect(self.src1, (self.dst, 1))
        self.connect(self.src0, (self.add, 0))
        self.connect(self.src1, (self.add, 1))
        self.connect(self.add, self.snk)
        # Se establece como deseamos ver los resultados graficos
        self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
        self.pyobj.show()

def main():
    tb = esquema()
    tb.start()
    tb.qapp.exec_()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass


