import math


def get_influencer_score(num_followers, average_engagement_percentage):
# Calculate the log base 2 of the followers
    follower_log = math.log2(num_followers)
    
    # Multiply the engagement percentage by that log result
    influencer_score = average_engagement_percentage * follower_log
    
    return influencer_score