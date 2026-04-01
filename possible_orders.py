def num_possible_orders(num_posts):
    posts = 1
    for i in range (2,num_posts+1):
        posts *= i
    return posts
