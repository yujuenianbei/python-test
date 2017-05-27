# 字典格式化字符串
phoneBook = {'benth':'123','tom':'456','alice':'789'}
print("tom's number is %(tom)s" % phoneBook)
# clear 删除字典所有项 因为是原地操作 所以没有返回值
returned_value = phoneBook.clear()
print(phoneBook)