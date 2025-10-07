def solution(fees, records):
    base_minutes, base_fee, unit_minutes, unit_fee = fees
    
    cars_in_time = {}
    cars_minutes = {}
    
    for record in records:

        time, car_number, in_out = record.split(' ')
        
        if in_out == 'IN':
            cars_in_time[car_number] = time
            if cars_minutes.get(car_number) is None:
                cars_minutes[car_number] = 0
        else:
            in_time = cars_in_time[car_number]

            minutes = calculate_minutes(in_time, time)
            cars_minutes[car_number] += minutes
            
            del cars_in_time[car_number]

    for car_number, in_time in cars_in_time.items():
        minutes = calculate_minutes(in_time, '23:59')
        cars_minutes[car_number] += minutes
            
    car_numbers = sorted(cars_minutes.keys())
    
    return [calculate_fee(cars_minutes[car_number] , base_minutes, base_fee, unit_minutes, unit_fee) for car_number in car_numbers]

def calculate_minutes(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(':'))
    out_hour, out_minute = map(int, out_time.split(':'))
    
    total_minutes = (out_hour - in_hour) * 60 + (out_minute - in_minute)
        
    return total_minutes

def calculate_fee(time, base_minutes, base_fee, unit_minutes, unit_fee):
    if time <= base_minutes:
        return base_fee
    else:
        # 120 // 10 = 12
        # 121 // 10 = 12 -> 13
        return base_fee + unit_fee * ((time - base_minutes + unit_minutes - 1) // unit_minutes)