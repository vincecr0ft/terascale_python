def Get_Primes(some_range):
    numbers = range(2,some_range)
    primes = {2:0}
    for i in numbers:
        for d in primes.keys():
            if i%d==0:
                primes[d] += 1
                break
        else:
            primes[i]=0
    largest=0
    for p in primes:
        if(primes[p]>0 and p>largest):
            largest=p
    results = {"largest prime":list(primes.keys())[-1], "largest factor":largest}

    return(results);