import tensorflow as tf
gpu = len(tf.config.experimental.list_physical_devices('GPU'))
print(f"So you've got {gpu} soul(s) in your hands, eh?")

x = tf.range(12); print(x)
#   I don't really think that running this every single time is such a great idea.
#   My RTX is literally screaming for help, everytime I do so.