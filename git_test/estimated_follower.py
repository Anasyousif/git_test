def get_estimated_spread(audiences_followers):
    if audiences_followers == []:
        return 0
    total_followers = len(audiences_followers)    
    average_audience_followers =   sum(audiences_followers) / total_followers
    estimated_spread = average_audience_followers * ( total_followers ** 1.2 )
    return estimated_spread
