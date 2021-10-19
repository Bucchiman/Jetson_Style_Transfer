import keras


class VGGNormalize(keras.layers.Layer):
    """A custom layer to normalize an image for input into a VGG model.

    This consists of swapping channel order and centering pixel values.

    Centering values come from:
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/keras/_impl/keras/applications/imagenet_utils.py  # NOQA
    """

    def __init__(self, **kwargs):
        """Initialize the layer.

        Args:
            **kwargs - arguments passed to the Keras layer base.
        """
        super(VGGNormalize, self).__init__(**kwargs)
        # work around for a bug introduced in diffences between the tf.keras and keras APIs
        self.outbound_nodes = self._outbound_nodes

    def build(self, input_shape):
        """Build the layer."""
        pass

    def call(self, x, reverse_channels=True):
        """Apply the layer.

        Args:
            x - an input tensor.
            reverse_channels - if True, reverse the channel order
        """
        # Swap channel order: 'RGB'->'BGR'
        if reverse_channels:
            x = x[:, :, :, ::-1]

        # Center pixel values. Technically each channel should have its
        # own center value, but the tensor computation is annoying so we'll
        # just center them all with the same value.
        x -= 120.0

        return x


class DeprocessStylizedImage(keras.layers.Layer):
    """A layer to deprocess style transfer layer output.

    The style transfer network outputs an image where pixel values are
    between -1 and 1 due to a tanh activation. This layer converts that back
    to normal values between 0 and 255.
    """

    def __init__(self, **kwargs):
        """Initialize the layer.

        Args:
            **kwargs - arguments passed to the Keras layer base.
        """
        super(DeprocessStylizedImage, self).__init__(**kwargs)

    def build(self, input_shape):
        """Build the layer."""
        pass

    def call(self, x):
        """Apply the layer."""
        return (x + 1.0) * 127.5
