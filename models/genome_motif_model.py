#/bin/python
import theano.tensor as T
from lasagne.init import Constant, Normal, Uniform, GlorotNormal
from lasagne.init import GlorotUniform, HeNormal, HeUniform

def genome_motif_model(shape, num_labels):

	input_var = T.tensor4('inputs')
	target_var = T.dmatrix('targets')

	# create model
	layer1 = {'layer': 'input',
			  'input_var': input_var,
			  'shape': shape,
			  'name': 'input'
			  }
	layer2 = {'layer': 'convolution', 
			  'num_filters': 200, 
			  'filter_size': (12, 1),
			  'pool_size': (4, 1),
			  'W': GlorotUniform(),
			  'b': Constant(0.05),
			  'norm': 'batch', 
			  'activation': 'relu',
			  'name': 'conv1'
			  }
	layer3 = {'layer': 'convolution', 
			  'num_filters': 300, 
			  'filter_size': (8, 1),
			  'pool_size': (4, 1),
			  'W': GlorotUniform(),
			  'b': Constant(0.05),
			  'norm': 'batch', 
			  'activation': 'relu',
			  'name': 'conv2'
			  }
	layer4 = {'layer': 'convolution', 
			  'num_filters': 300, 
			  'filter_size': (8, 1),
			  'pool_size': (4, 1),
			  'W': GlorotUniform(),
			  'b': Constant(0.05),
			  'norm': 'batch', 
			  'activation': 'relu',
			  'name': 'conv3'
			  }
	layer5 = {'layer': 'dense', 
			  'num_units': 1000, 
			  'W': GlorotUniform(),
			  'b': Constant(0.05), 
			  'dropout': .5,
			  'norm': 'batch', 
			  'activation': 'relu', 
			  'name': 'dense4'
			  }
	layer6 = {'layer': 'dense', 
			  'num_units': num_labels, 
			  'W': GlorotUniform(),
			  'b': Constant(0.05),
			  'activation': 'sigmoid', 
			  'name': 'output'
			  }
			  
	model_layers = [layer1, layer2, layer3, layer4, layer5, layer6]

	# optimization parameters
	optimization = {"objective": "binary",
					"optimizer": "adam"
					#"weight_norm": 10
					#"l1": 1e-7,
					#"l2": 1e-8, 
					}

	return model_layers, input_var, target_var, optimization

