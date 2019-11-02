import logging
import torch.nn as nn
import numpy as np


class BaseNet(nn.Module):
    """Base class for all neural networks."""

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.rep_dim = None  # representation dimensionality, i.e. dim of the last layer

    def forward(self, *input):
        """
        Forward pass logic
        :return: Network output
        """
        raise NotImplementedError

    def summary(self):
        """Network summary."""
        net_parameters = filter(lambda p: p.requires_grad, self.parameters())
        params = sum([np.prod(p.size()) for p in net_parameters])
        self.logger.info('Trainable parameters: {}'.format(params))
        self.logger.info(self)

    def noise(x, std, phase, scope=None, reuse=None):
        with tf.name_scope(scope, 'noise'):
            eps = tf.random_normal(tf.shape(x), 0.0, std)
            output = tf.where(phase, x + eps, x)
        return output