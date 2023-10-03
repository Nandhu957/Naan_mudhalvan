def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

products = ["shoes","boot","loafer","apple","shoes","sandal","shoes","apple"]
target="shoes"
target2='apple'
result_1= linear_search_product(products,target)
print ("Target-1 : " ,result_1 )
result_2 = linear_search_product(products,target2)
print ("Target-2 : " ,result_2)
