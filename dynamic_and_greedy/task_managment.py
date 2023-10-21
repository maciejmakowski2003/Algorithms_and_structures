def tm(spans):
    n=len(spans)
    spans.sort(key = lambda x: x[1]) 

    prev = spans[0]
    result=[prev] 

    for i in range(1,n):
        if spans[i][0]>prev[1]:
            result.append(spans[i]) 
            prev = spans[i]
