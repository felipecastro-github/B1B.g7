#!/usr/bin/env python2
from gnuradio import gr
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import qtgui
from PyQt5 import Qt
import sys, sip

sys.path.append('/home/felipe/Documentos/8_semestre/Comu_II/B1B.g7/Librerias')
import Bqs_B1B_g7 as misbloques

class flujograma(gr.top_block):
	def __init__(self):
		gr.top_block.__init__(self)
		N= 2**15
		samp_rate =50000
		src = blocks.wavfile_source('/home/felipe/Documentos/8_semestre/Comu_II/B1B.g7/Practica_4/Record.wav', True)
		resampler = filter.rational_resampler_fff(
                interpolation=samp_rate,
                decimation=44100,
                taps=None
        )
		str2vec=blocks.stream_to_vector(gr.sizeof_float*1, N)
		v_avg=misbloques.vector_average_hob(N,10000)
		e_fft=misbloques.e_vector_fft_square_ff(N,samp_rate)
		snk = qtgui.time_sink_f(N,samp_rate,"senal en tiempo",1)
		vsnk = qtgui.vector_sink_f(
			N,
			-samp_rate/2.,
			(samp_rate*1.0)/N,
			"frecuencia",
			"Magnitud",
			"FT en Magnitud",
			1
		)
		vsnk.enable_autoscale(True)
		snk.enable_autoscale(True)
		#conexiones
 		self.connect(src, resampler, str2vec, e_fft, v_avg, vsnk)
 		self.connect(src, snk)
		#graficar
		pyobjv = sip.wrapinstance(vsnk.pyqwidget(), Qt.QWidget)
		pyobjv.show()
		pyobj = sip.wrapinstance(snk.pyqwidget(), Qt.QWidget)
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

