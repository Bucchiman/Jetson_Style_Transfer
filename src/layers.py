import keras


class VGGNormalize(keras.layers.Layer):
    def __init__(self, **kwargs):
        super(VGGNormalize, self).__init__(**kwargs)
        self.outbound_nodes = self._outbound_nodes

    def build(self, input_shape):
        pass

    def call(self, x, reverse_channels=True):
        if reverse_channels:
            x = x[:, :, :, ::-1]

        x -= 120.0

        return x


class DeprocessStylizedImage(keras.layers.Layer):
    def __init__(self, **kwargs):
        super(DeprocessStylizedImage, self).__init__(**kwargs)

    def build(self, input_shape):
        pass

    def call(self, x):
        return (x + 1.0) * 127.5
