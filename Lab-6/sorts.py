import random
import time

def selection_sort(alist):
    comps = 0
    if len(alist) < 2:
        return comps
    for idx in range(len(alist) - 1):
        min = alist[idx]
        for idx2 in range(idx + 1, len(alist)):
            comps = comps + 1
            if min > alist[idx2]:
                min = alist[idx2]
                min_idx = idx2          
        if min != alist[idx]:
            temp = alist[idx]
            alist[idx] = min
            alist[min_idx] = temp 
    return comps
        
def insertion_sort(alist):
    comps = 0
    if len(alist) < 2:
        return comps
    for idx in range(1, len(alist)):
        for idx2 in range(idx - 1, -1, -1):
            comps = comps + 1
            if alist[idx] < alist[idx2]:
                temp = alist[idx2]
                alist[idx2] = alist[idx]
                alist[idx] = temp
                idx = idx - 1
                idx2 = idx2 - 1
            else:
                break    
    return comps
                
def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

