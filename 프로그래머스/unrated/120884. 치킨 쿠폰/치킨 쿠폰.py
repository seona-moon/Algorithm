def solution(chicken):
    coupon = chicken//10 + chicken%10 #108 + 1
    service = chicken//10
    while coupon>=10:
        service += coupon//10 #108+10 #1
        coupon = coupon//10 + coupon%10 #10+8 #1+8
    
    return service