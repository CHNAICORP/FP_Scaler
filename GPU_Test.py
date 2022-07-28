# 方法一
import tensorflow as tf

# <function is_gpu_available at 0x000001628AD0F9D0>
print(tf.test.is_gpu_available)

# # 方法二
# import tensorflow as tf
#
"""
2022-07-27 21:44:01.560536: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized
with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical
operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-07-27 21:44:02.009112: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /device:GPU:0 with
6007 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 2060 SUPER, pci bus id: 0000:01:00.0, compute capability: 7.5
2022-07-27 21:44:02.010292: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /device:GPU:0 with
6007 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 2060 SUPER, pci bus id: 0000:01:00.0, compute capability: 7.5
Default GPU Device: /device:GPU:0
"""
# if tf.test.gpu_device_name():
#     print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
# else:
#     print("Please install GPU version of TF")

# 方法三
"""
2022-07-27 21:45:39.674487: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized 
with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical 
operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-07-27 21:45:40.116476: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /device:GPU:0 with 
6005 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 2060 SUPER, pci bus id: 0000:01:00.0, compute capability: 7.5
"""
# import tensorflow as tf
#
# tf.test.gpu_device_name()

# 方法四
"""
2022-07-27 21:48:23.666767: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized
 with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical 
 operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-07-27 21:48:24.108830: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /device:GPU:0 with 
6007 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 2060 SUPER, pci bus id: 0000:01:00.0, compute capability: 7.5
"""
# from tensorflow.python.client import device_lib
#
# device_lib.list_local_devices()
