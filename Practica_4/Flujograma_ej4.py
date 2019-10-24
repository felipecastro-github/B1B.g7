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
        samp_rate = 1e6
        fftsize = 2048
        self.src = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 1000, 1, 0)
        self.nse = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1)
        self.add = misbloques.e_add_cc()
        self.thr = blocks.throttle(gr.sizeof_gr_complex, samp_rate, True)
        self.snk = qtgui.sink_c(
            fftsize, 
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
        )
        #Conexiones
        self.connect(self.src, (self.add, 0))
        self.connect(self.nse, (self.add, 1))
        self.connect(self.add, self.thr, self.snk)
        #Para graficar
        self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
        self.pyobj.show()
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
