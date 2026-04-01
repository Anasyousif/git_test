def decayed_followers(initial_followers, fraction_lost_daily, days):
    fraction_lost_daily = (1- fraction_lost_daily)
    total = initial_followers * (fraction_lost_daily ** days)
    return total