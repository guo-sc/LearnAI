import os

from map_reduce_simulation import test_map_reduce

# =========================================================================================================

if not os.path.exists('./output'):
    os.makedirs('./output')
##########################################  fill nan    ###################################################
#shop_deal_cnt_fill_nan_mapper = 'fill_miss_nan_mapper.py'
#shop_deal_cnt_fill_nan_file = './output/shop_info_fill_nan'
#deal_path = './input/shop_info'
#test_map_reduce([deal_path], shop_deal_cnt_fill_nan_mapper, None, \
#                shop_deal_cnt_fill_nan_file, None)
#########################################  shop_deal_cnt  #################################################
shop_deal_cnt_mapper = 'shop_deal_cnt_mapper.py'
shop_deal_cnt_reducer = 'shop_deal_cnt_reducer.py'
shop_deal_cnt_mapper_file = './output/shop_deal_cnt_mapper'
shop_deal_cnt_reducer_file = './output/shop_deal_cnt_reducer'
deal_path = './input/user_pay'

test_map_reduce([deal_path], shop_deal_cnt_mapper, shop_deal_cnt_reducer, \
                shop_deal_cnt_mapper_file, shop_deal_cnt_reducer_file, key=lambda x: x[:2])
###################################   shop_combine_deal   ###############################################
shop_combine_deal_mapper = 'shop_combine_deal_mapper.py'
shop_combine_deal_reducer = 'shop_combine_deal_reducer.py'
shop_combine_deal_mapper_file = './output/shop_combine_deal_mapper'
shop_combine_deal_reducer_file = './output/shop_combine_deal_reducer'
shop_path = './output/shop_info_fill_nan'
shop_deal_cnt = './output/shop_deal_cnt_reducer'

test_map_reduce([shop_deal_cnt, shop_path], shop_combine_deal_mapper, shop_combine_deal_reducer, \
                shop_combine_deal_mapper_file, shop_combine_deal_reducer_file, key=lambda x: x[:1])
##########################################################################################################
shop_deal_avg_mapper = 'shop_deal_avg_mapper.py'
shop_deal_avg_reducer = 'shop_deal_avg_reducer.py'
shop_deal_avg_mapper_file = './output/shop_deal_avg_mapper'
shop_deal_avg_reducer_file = './output/shop_deal_avg_reducer'
shop_combine_deal = './output/shop_combine_deal_reducer'

test_map_reduce([shop_combine_deal], shop_deal_avg_mapper, shop_deal_avg_reducer, \
                shop_deal_avg_mapper_file, shop_deal_avg_reducer_file, key=lambda x: (x[0], x[1]))

