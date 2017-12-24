#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# 独立使用django的model

pwd = os.path.dirname(os.path.realpath(__file__))      # get script file path
sys.path.append(pwd+"../")      # get project root dir
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django
django.setup()

from goods.models import GoodsCategory       # 必须写在django.setup()之后，否则就认为没有指定DJANGO_SETTINGS_MODULE

from db_tools.data.category_data import row_data      # 不同的数据脚本导入不同数据
# from db_tools.data.category_data_new import row_data      # 用我自己的数据

for lev1_cat in row_data:
    lev1_intance = GoodsCategory()
    lev1_intance.code = lev1_cat["code"]
    lev1_intance.name = lev1_cat["name"]
    lev1_intance.category_type = 1
    lev1_intance.save()

    for lev2_cat in lev1_cat["sub_categorys"]:
        lev2_intance = GoodsCategory()
        lev2_intance.code = lev2_cat["code"]
        lev2_intance.name = lev2_cat["name"]
        lev2_intance.category_type = 2
        lev2_intance.parent_category = lev1_intance
        lev2_intance.save()

        for lev3_cat in lev2_cat["sub_categorys"]:
            lev3_intance = GoodsCategory()
            lev3_intance.code = lev3_cat["code"]
            lev3_intance.name = lev3_cat["name"]
            lev3_intance.category_type = 3
            lev3_intance.parent_category = lev2_intance
            lev3_intance.save()

