import paddle
from symbolic_trace import symbolic_trace

def case1(x):
    y = x + 2 
    ret = paddle.subtract(y, 1)
    print("yes")
    print("no")
    #for i in range(10):
    ret = ret + 2 + x
    return ret

def case2(x):
    y = x + 2 
    ret = paddle.subtract(y, 1)
    for i in range(10):
        ret = ret + 2 + x
    return ret

x = paddle.to_tensor([1.0])
symbolic_trace(case1, with_log=False)(x)
symbolic_trace(case1, with_log=False)(x)
symbolic_trace(case2, with_log=False)(x)
