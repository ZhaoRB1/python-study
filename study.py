  #  import matplotlib.pyplot as plt
   # x=[1,2,3,4,5]
   # y=[1,2,3,4,5]
   # y1=[1,2,3,2,1]


   # plt.bar(x,y,tick_label=["2018RASP","综述"])
   # plt.bar(x,y1,bottom=y)
   # plt.show()


import matplotlib.pyplot as plt

# 数据
categories = ['2018RASP', 'overview']
datasets = [
    [8,22],
    [8,8],
    [2,4],
    [2,10],
    [8,6],
    [0,1],
    [9,7],
    [15,9],
    [0,0] ]
labels = ['Human', 'Mouse', 'Other Animals', 'Plant', 'Fungi',
          'Protist', 'Bacteria', 'Virus', 'Others']  # 数据集标签

# 创建堆积柱形图
bottom_values = [0] * len(categories)  # 初始堆叠高度为0
for i, data in enumerate(datasets):
    plt.bar(categories, data, bottom=bottom_values, label=labels[i])
    bottom_values = [bottom + value for bottom, value in zip(bottom_values, data)]

# 添加图例
plt.legend()

# 添加标题和标签
plt.title('Stacked Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Number of articles')

# 显示图形
plt.show()
