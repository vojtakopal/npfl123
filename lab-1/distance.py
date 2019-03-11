def min_by(items, projection):
    min_item = None
    min_val = float("inf")

    for item in items:
        val = projection(item)
        if val < min_val:
            min_val = val
            min_item = item

    return min_item
        

def dist_step(hyp_list, gold_list, state = ([], 0)):
    (operations, distance) = state

    if len(hyp_list) == 0:
        appendix = []
        for c in gold_list:
            appendix += [('d', c)]
        
        return (operations + appendix, distance + len(appendix))
    
    if len(gold_list) == 0:
        appendix = []
        for c in hyp_list:
            appendix += [('i', c)]
        
        return (operations + appendix, distance + len(appendix))

    if hyp_list[0] == gold_list[0]:
        return dist_step(hyp_list[1:], gold_list[1:], (operations + [('n')], distance))

    state_add = dist_step(hyp_list[1:], gold_list, (operations + [('i', hyp_list[0])], distance + 1))
    state_del = dist_step(hyp_list, gold_list[1:], (operations + [('d', gold_list[0])], distance + 1))
    state_sub = dist_step(hyp_list[1:], gold_list[1:], (operations + [('s', gold_list[0], hyp_list[0])], distance + 1))

    return min_by([state_add, state_sub, state_del], lambda state : state[1])

# returns (list of operations, minimum distance)
#  - operation: (name of operation [,characters]), e.g. 
#       - ('n'): nothing, 
#       - ('d', 'A'): delete A
#       - ('i', 'B'): insert B
#       - ('s', 'C', 'D'): subsitute C for D
def dist(hyp, gold, delimiter = ' '):
    hyp_list = hyp.split(delimiter)
    gold_list = gold.split(delimiter)

    return dist_step(hyp_list, gold_list)

def wer(hyp, gold, delimiter = ' '):
    hyp_list = hyp.split(delimiter)
    gold_list = gold.split(delimiter)

    (_, d) = dist_step(hyp_list, gold_list)
    return float(d) / len(gold_list)
