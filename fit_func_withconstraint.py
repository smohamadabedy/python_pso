import math
##for fun!
def myfunc(var1):
    v = str(var1)
    print(v.center(50))
##optimization objective function
def func(pos):
    x = pos[0];
    y = pos[1];

    if(x > 0 and y > 0 and (18*x + 54*y <= 972) and (x+y <= 20) and (3*x+y<=30)):
        return -(2*x + y)
    else:
        return 1000
##search for best of all
def find_bestg(gr):
    i = 0
    best_group = {
        "gbest" : gr[0]["fval"][0]
        }; 
    for m in gr:
        if(gr[m]["fval"][0] <= best_group["gbest"]):
            best_group["gbest"] = gr[m]["fval"][0];
            best_group["pos"] = gr[m]["pos"];
    
        i = i+1
    print("********")    
    print(best_group["gbest"])
    print(round(best_group["pos"][0],4)," _|_ ",round(best_group["pos"][1],4))

    return best_group
