from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.utils import plot_model

inputs = Input(shape=(127, 127, 3))
conv1 = Conv2D(filters=64, kernels=(3, 3), padding='same' dilation_rate=(1, 1))(inputs)
conv2 = Conv2D(filters=128, kernels=(3, 3), padding='valid' dilation_rate=(1, 1))(conv1)
conv3 = Conv2D(filters=128, kernels=(3, 3), padding='same' dilation_rate=(2, 2))(conv2)

model = Model(inputs=inputs, outputs=conv2)
plot_model(model, to_file='./model_visual.png', show_shapes=True)