from collections import deque
 
def solution(cacheSize, cities):
    # 캐시가 없는 경우
    if cacheSize == 0:
        return len(cities) * 5

    # 캐시가 있는 경우
    cache = deque([])

    def update_cache(target, is_hit):
        
        current_size = len(cache)
        
        if is_hit:
            for _ in range(current_size):
                temp = cache.popleft()
                if temp != target:
                    cache.append(temp)
        else:
            if current_size >= cacheSize:
                cache.popleft()

        cache.append(target)
        
    time = 0
    
    for city in cities:

        current = city.lower()
        
        if current in cache:
            time += 1
            update_cache(current, True)
        else:
            time += 5
            update_cache(current, False)
    
    return time