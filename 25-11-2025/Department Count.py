x = {
"e1": {"dept": "IT"},
"e2": {"dept": "HR"},
"e3": {"dept": "IT"},
}

ans={}

for i,j in x.items():
    for q,w in j.items():
        if w in ans:
            ans[w]+=1
        else:
            ans[w]=1

print(ans)
