def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .06, 74.5317442824, 10)

count = 0

def square(x):
    global count
    count += 1
    print count
    return x**2

    
print square(square(square(square(3))))