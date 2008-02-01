
from core import *
import gof

from gof import PatternOptimizer as pattern_opt, OpSubOptimizer as op_sub

"""
This variable is used in compile.prog as the optimizer for all programs built
using either compile.single, compile.to_func, and compile.prog.

"""

def optimizer(lst):
    begin = gof.SeqOptimizer([])
    end   = gof.SeqOptimizer([gof.DummyRemover])
    seq_opt = gof.SeqOptimizer(begin + lst + end)
    return gof.PythonOpt(gof.MergeOptMerge(seq_opt))

if 0:
    optimizer_begin = gof.SeqOptimizer([opt for name, opt in [
             ['double_transpose_eliminator', pattern_opt((transpose, (transpose, 'x')), 'x')],

             ['addxx_to_twice',              pattern_opt((add_elemwise, 'x', 'x'), (twice, 'x'))],

             ['twice_to_itwice',             op_sub(twice, itwice)],

             ['mulxx_to_sqr',                pattern_opt((mul_elemwise, 'x', 'x'), (sqr, 'x'))],

             ['sqr_to_isqr',                 op_sub(sqr, isqr)],

             ['add_to_iadd',                 op_sub(add_elemwise, iadd_elemwise)],

             ['add_to_iadd_reverse',         pattern_opt((add_elemwise, 'x', 'y'),
                 (iadd_elemwise, 'y', 'x'))]]])
#         ['remove_copies',               gof.OpRemover(array_copy)],
#         [None,                          gof.DummyRemover] # has to be at the end
