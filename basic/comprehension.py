# coding=utf-8
if __name__ == '__main__':
    # 推导式,列表、元组、集合的推导式一致
    # [表达式 for 变量 in 列表]
    # [out_exp_res for out_exp in input_list]
    #
    # 或者
    #
    # [表达式 for 变量 in 列表 if 条件]
    # [out_exp_res for out_exp in input_list if condition]

    # 列表推导式，[16, 15, 14]
    lt = [6, 5, 4, 3, 2, 1]
    print [x + 10 for x in lt if x > 3]

    # 字典推导式
    # { key_expr: value_expr for value in collection }
    #
    # 或
    #
    # { key_expr: value_expr for value in collection if condition }
    dt = {"a": 1, "b": 2, "c": 3}
    print {k + "_key": dt[k] + 1 for k in dt}
