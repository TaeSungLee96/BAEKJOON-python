x, y, w, h = map(int, input().split())

x_min = min(x, abs(w-x))
y_min = min(y, abs(h-y))
print(min(x_min, y_min))