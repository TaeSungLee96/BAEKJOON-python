a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# 1. (a1 - c) > 0,                  (a1 > c)
#       1-1. f_(n) <= 0 이 항상 불만족
#
# 2. (a1 - c) == 0,                 (a1 == c)
#       2-1. a0 > 0 이면, f_(n) <= 0 이 항상 불만족
#       2-2. a0 == 0 이면, f_(n) = 0 이 항상 만족   ( f(n) = c*n )
#       2-3. a0 < 0 이면, f_(n) < 0 이 항상 만족    ( f(n) < c*n )
#
# 3. (a1 - c) < 0 이면, n0에서       (a1 < c)
#       3-1. f_(n0) > 0 이면, 불만족
#       3-2. f_(n0) <= 0 이면, 만족

f_ = lambda x: (a1 - c)*x + a0

is_right = 0
# 2-2번, 2-3번 조건
if a1 == c and a0 <= 0:
    is_right = 1
# 3-2번 조건
elif a1 < c and f_(n0) <= 0:
    is_right = 1

print(is_right)