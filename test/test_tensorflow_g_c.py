import tensorflow as tf

batch_size = 40
width = 256
height = 256
channels = 3

real = tf.placeholder(dtype=tf.float32, shape=[batch_size, width, height, channels])
fake = tf.placeholder(dtype=tf.float32, shape=[batch_size, width, height, channels])


real_ = tf.image.rgb_to_grayscale(real)
fake_ = tf.image.rgb_to_grayscale(fake)




with tf.Session() as sess:
    pass
