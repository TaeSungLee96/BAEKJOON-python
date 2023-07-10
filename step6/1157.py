S = list(input().lower())
ct_ls = []
str_ls = []

for s in list(set(S)):
    ct_ls.append(S.count(s))
    str_ls.append(s)

max_num_ct = ct_ls.count(max(ct_ls))
if max_num_ct > 1 or len(list(set(str_ls))) == 1 and len(S) != 1:
    print("?")
else:
    print((str_ls[
        ct_ls.index(max(ct_ls))
    ]).upper())
