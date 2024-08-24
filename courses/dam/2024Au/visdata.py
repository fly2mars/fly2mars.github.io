import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
csv_file = 'mdata4clustering.csv'  # 替换为你的 CSV 文件路径
data = pd.read_csv(csv_file)

# 提取 x, y 和 class 列
x = data['x']
y = data['y']
classes = data['class']

# 创建一个新的图形
plt.figure(figsize=(8, 6))

# 根据类别绘制数据点
for class_value in classes.unique():
    # 获取当前类别的数据
    class_data = data[data['class'] == class_value]
    plt.scatter(class_data['x'], class_data['y'], label=f'Class {class_value}')

# 设置图形的标题和标签
plt.title('Data Points Visualization')
plt.xlabel('x')
plt.ylabel('y')

# 显示图例
plt.legend()

# 显示图形
plt.show()
