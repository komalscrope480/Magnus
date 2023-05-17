miao = int(input("请输入总秒数："))
print("一共是：" + str(miao // 3600) + "小时零" + str((miao % 3600) // 60) + "零" + str((miao % 3600) % 60))
