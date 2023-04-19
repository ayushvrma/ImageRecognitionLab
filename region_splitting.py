import numpy as np

def split_regions(img):
    # Check if the image can be split further
    if np.max(img) - np.min(img) <= 3:
        return [img]
    
    # Split the image into four regions
    height, width = img.shape
    half_height, half_width = height // 2, width // 2
    
    regions = [
        img[:half_height, :half_width],
        img[:half_height, half_width:],
        img[half_height:, :half_width],
        img[half_height:, half_width:]
    ]
    
    # Recursively split each region
    result = []
    for region in regions:
        result.extend(split_regions(region))
    
    return result

# def segments(sub_regions):
    
#     # Join the sub-regions that satisfy the condition and
#     # store the ones that don't in a separate list
#     joined_regions = []
#     non_joined_regions = []

#     print(sub_regions)
#     for region in sub_regions:
#         if np.max(region) - np.min(region) <= 3:
#             joined_regions.append(region)
#         else:
#             non_joined_regions.append(region)
    
#     return joined_regions, non_joined_regions

def segments(sub_regions):

    joined_regions = [sub_regions[0]]
    sub_regions.pop(0)
    m_max,m_min = np.max(sub_regions[0]), np.min(sub_regions[0])
    non_joined_regions = []
    for region in sub_regions:
        # print(region)
        maxo, mino = max(m_max, np.max(region)) , min(m_min, np.min(region))
        if maxo - mino <= 3:
            m_max = maxo
            m_min = mino
            joined_regions.append(region)
        else:
            non_joined_regions.append(region)
    
    return joined_regions, non_joined_regions

# define main

img = [[5,6,6,6,7,7,6,6], [6,7,6,7,5,5,4,7], [6,6,4,4,3,2,5,6], [5,4,5,4,2,3,4,6], [0,3,2,3,3,2,4,7], [0,0,0,0,2,2,5,6], [1,1,0,1,0,3,4,4], [1,0,1,0,2,3,5,4]]

img = np.array(img)
sub_regions = split_regions(img)
# print(sub_regions)
result = segments(sub_regions)
print('joined reigons',result[0])
print('non joined reigons',result[1])




