
import numpy as np

"""
前向传播神经网络
"""

"""
标量（一维张量）测试
"""
input_value_cat = 1.0  # 输入值：1.0（猫）
input_value_dog = 2.0  # 输入值：2.0（狗）
input_value = input_value_cat
target_value = 1.0  # 标注：1.0（猫）、2.0（狗）、3.0（鸭子）
# 权重
weight_scalar = 2.0
# 偏置
bias_scalar = 2.0


# 神经元
def neuron(weight, predict, bias):
    return weight * predict + bias


# 激活函数（激励函数）
def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


# 代价函数(损失函数)
def mse_cost(predict_value, actual_value):
    return 0.5 * (predict_value - actual_value) ** 2


if __name__ == '__main__':
    # 前向传播
    return_value_neuron = neuron(weight_scalar, input_value, bias_scalar)
    print("神经元的返回值: ", neuron(weight_scalar, input_value, bias_scalar))  # 输出神经元的返回值

    return_value_sigmoid = sigmoid(return_value_neuron)
    print("激活函数的返回值: ", sigmoid(weight_scalar))  # 输出激活函数的返回值

    return_value_mse_cost = mse_cost(return_value_sigmoid, target_value)
    print("损失函数的返回值: ", return_value_mse_cost)  # 输出损失函数的返回值

    print("前向传播神经网络的预测值: ", return_value_mse_cost)  # 输出损失函数的值
    print("权重：", weight_scalar, "，偏置：", bias_scalar, "，输入值：", input_value, "，标签：", target_value)
