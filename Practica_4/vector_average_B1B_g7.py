#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import numpy
from gnuradio import gr
 
class vector_average_B1B_g7(gr.sync_block): 
    def __init__(self, N, Nensayos):
        gr.sync_block.__init__(self, name="vector_average", in_sig=[(numpy.float32, N)], out_sig=[(numpy.float32, N)])

        self.N=N
        self.Nensayos=numpy.uint64=Nensayos
        self.med=numpy.empty(N,dtype=numpy.float64)
        self.count=numpy.uint64=0
 
    def work(self, input_items, output_items):
 
        # Traducción de matrices 3D a 2D 
        in0 = input_items[0]
        out0=output_items[0]
        
        # El tamano de la matriz in0 es L[0]xL[1]=L[0]xN
        L=in0.shape
 
        # conteo de funciones muestras (filas de matriz) procesadas
        if self.count < self.Nensayos:
            self.count += L[0] 
 
        # La media de las funciones muestras (filas de matriz) que tiene in0
        mean=in0.mean(0)    
 
        # ajuste de la media ya calculada, con la media de in0
        self.med = (self.med*(self.count-L[0])+mean*L[0])/self.count
 
        # Entrega de resultado
        out0[:]=self.med
        return len(out0)
