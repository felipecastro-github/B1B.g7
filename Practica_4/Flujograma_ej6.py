#!/usr/bin/env python2
from gnuradio import gr
from gnuradio import analog
from gnuradio import blocks
from gnuradio.filter import firdes
from gnuradio import qtgui
from PyQt5 import Qt
import sys, sip

sys.path.append('/home/felipe/Documentos/8_semestre/Comu_II/B1B.g7/Librerias')
import Bqs_B1B_g7 as misbloques

class flujograma(gr.top_block):
	def __init__(self):
		gr.top_block.__init__(self)
		samp_rate = 64000
		f=2000
		N= 1024
		src = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f, 1, 0)
		nse = analog.noise_source_f(analog.GR_GAUSSIAN, 0.1)
		add = misbloques.e_add_ff(1.0)
		snk = qtgui.time_sink_f(128,samp_rate,"senal promediada",1)
		str2vec=blocks.stream_to_vector(gr.sizeof_float*1, N)
		e_fft=misbloques.e_vector_fft_ff(N)
		vsnk = qtgui.vector_sink_f(
			N,
			-samp_rate/2.,
			samp_rate/N,
			"frecuencia",
			"Magnitud",
			"FT en Magnitud",
			1
		)
		vsnk.enable_autoscale(True)
		
		#conexiones
		self.connect(src, (add, 0))
		self.connect(nse, (add, 1))
		self.connect(add, snk)
		self.connect(add, str2vec, e_fft, vsnk)
 
		#graficar
		pyobjv = sip.wrapinstance(vsnk.pyqwidget(), Qt.QWidget)
		pyobj = sip.wrapinstance(snk.pyqwidget(), Qt.QWidget)
		pyobjv.show()
		pyobj.show()
 
def main():
    qapp = Qt.QApplication(sys.argv)
    simulador_de_la_envolvente_compleja = flujograma()
    simulador_de_la_envolvente_compleja.start()
    qapp.exec_()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
