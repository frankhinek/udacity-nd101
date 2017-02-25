'''
A simple example showing how to restore two TensorFlow variables from disk.
The accompanying tf-save-vars.py script demonstrates how to save these
variables.
'''

import tensorflow as tf

# The file path to save the data
save_file = "./model.ckpt"

# Two Variables: weights and bias
weights = tf.Variable(tf.truncated_normal([2, 3]))
bias = tf.Variable(tf.truncated_normal([3]))

# Class used to save and/or restore Tensor Variables
saver = tf.train.Saver()

with tf.Session() as sess:
    # Load the weights and bias
    saver.restore(sess, save_file)

    # Show the values of weights and bias
    print('Weight:')
    print(sess.run(weights))
    print('Bias:')
    print(sess.run(bias))
