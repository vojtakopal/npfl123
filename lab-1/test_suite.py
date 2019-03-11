from distance import dist, wer

print(dist(hyp='', gold=''))
print(dist(hyp='a a a', gold='a a a'))
print(dist(hyp='a b', gold='a a a'))
print(dist(hyp='a b c a', gold='a a a'))
print(dist(hyp='a b c a d a a', gold='a a d a'))

print('zero wer', wer(hyp='a a a', gold='a a a') == 0)
print('si wer', wer(hyp='a b', gold='a a a') == 2.0/3)