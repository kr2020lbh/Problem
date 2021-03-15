def solution(routes):
    routes.sort(key=lambda x:x[1])
    c = -30001
    ans = 0
    for car_in,car_out in routes:
        if c < car_in :
            c = car_out
            ans += 1
    return ans



routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)