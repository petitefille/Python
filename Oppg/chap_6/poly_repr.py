def pol_eval_list(p, x) :
    val = 0.0
    for i in range(len(p)) :
        val += p[i]*x**i

    return val

def pol_eval_dict(p,x) :
    val = 0.0
    for i in p :
        val += p[i]*x**i

    return val

p_list = [0] * 101
p_list[0] = -.5
p_list[100] = 2.

print p_list
print pol_eval_list(p_list, 1.05)

p_dict = {}
p_dict[0] = -.5
p_dict[100] = 2.

print p_dict
print pol_eval_dict(p_dict, 1.05)

"""

python poly_repr.py
[-0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.0]
262.502515693
{0: -0.5, 100: 2.0}
262.502515693

"""