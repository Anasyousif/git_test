def get_avg_brand_followers(all_handles, brand_name):
    if not all_handles:
        return 0
    tota_brand_mentions = 0
    for audience in all_handles: 
        for handle in audience:
            if brand_name in handle:
                tota_brand_mentions +=1
                
    return tota_brand_mentions / len(all_handles)  