import numpy as np
from gnuradio import gr

class e_add_cc(gr.sync_block):
	def __init__(self):
		self.coef = 1.0
		gr.sync_block.__init__(self,
			name='e_dd_ff',
			in_sig=[np.complex64,np.complex64],
			out_sig=[np.complex64]
        )
    	
	def work(self, input_items, output_items):
		in0 = input_items[0]
		in1 = input_items[1]
		out0 = output_items[0]
		out0[:]=(in0+in1)*self.coef
		return len(out0)



