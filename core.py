#! /usr/bin/env python
# -*- coding: utf-8 -*-

from faker import Factory
from faker.providers import BaseProvider
import csv
import random
import numpy as np

NUM_SOUKO_ZAIKO = 107439
NUM_SOUKO_IDOU = 5309
NUM_SPLIT = 85925
NUM_HURIDASHI_IDOU = 14085

fake = Factory.create()
fake.add_provider(MyStatusProvider)

with open("warehouse_stock.csv", "w+") as f:

    csv_writer = csv.writer(f,delimiter=",", quotechar='"',quoting=csv.QUOTE_ALL)
    header = ["ec_warehouse_code","unity_store_code","l3_item_code","confirmed_stock","priority_stock","inventory_unavailable_for_sale","expected_write_off_inventory","inventory_under_investigation","file_created_date_time"]
    csv_writer.writerow(header)

    for i in range(NUM_SOUKO_ZAIKO):
        l = [5000,str(fake.random_number(6)).zfill(6),str(fake.random_number(13)).zfill(13),fake.random_number(3),0,0,0,0,"2018-04-01T13:00:00Z"]
        csv_writer.writerow(l)
        
with open("warehouse_move.csv", "w+") as f:

    csv_writer = csv.writer(f,delimiter=",", quotechar='"',quoting=csv.QUOTE_ALL)
    header = ["ec_warehouse_code","unity_store_code","inventory_adjustment_type","transfer_out_instruction_no","mgmt_no","inventory_type","l3_item_code","confirmed_stock","inventory_unavailable_for_sale","expected_write_off_inventory","inventory_under_investigation","created_at"]
    csv_writer.writerow(header)

    for i in range(NUM_SOUKO_IDOU):
        l = [5000,str(fake.random_number(6)).zfill(6),0,0,str(fake.random_number(17)).zfill(17),1,str(fake.random_number(13)).zfill(13),fake.random_number(3),0,0,0,"2018-04-01T13:00:00Z"]
        csv_writer.writerow(l)
        
with open("drawer_instruction.csv", "w+") as f:

    csv_writer = csv.writer(f,delimiter=",", quotechar='"',quoting=csv.QUOTE_ALL)
    header = ["ec_warehouse_code","unity_store_code","transfer_out_instruction_no","transfer_out_instruction_no_branch_no","voucher_type","fr_shipping_fee_payment_type","shipping_location_type","shipping_location_code","shipping_unity_store_code","shipping_address_postal_code","shipping_address_1","shipping_address_2","shipping_name","shipping_phone_number","l3_item_code","transfer_out_instructed_quantity","expected_shipping_date","expected_arrival_date","arranged_delivery_date","file_created_date_time","comment"]
    csv_writer.writerow(header)

    for i in range(NUM_SPLIT):
        l = [5000,str(fake.random_number(6)).zfill(6),str(fake.random_number(10)).zfill(10),1,"S020",1,"W",str(fake.random_number(4)).zfill(4),str(fake.random_number(6)).zfill(6),str(fake.random_number(7)).zfill(7),"大阪府","堺市堺区築港八幡町1番17","堺倉庫",fake.phone_number(),str(fake.random_number(13)).zfill(13),fake.random_number(2),"20180401","20180402",fake.random_number(3),"2018-04-01T13:00:00Z","SPLIT"]
        csv_writer.writerow(l)
        
with open("drawer_move.csv", "w+") as f:

    csv_writer = csv.writer(f,delimiter=",", quotechar='"',quoting=csv.QUOTE_ALL)
    header = ["ItemCd","Qty","IdentificationFlg","FromManageNo","ManageNo","CreateDate","StockIdentification","ShopCd"]
    csv_writer.writerow(header)

    for i in range(NUM_HURIDASHI_IDOU):
        l = [str(fake.random_number(13)).zfill(13),fake.random_number(3),1,str(fake.random_number(11)).zfill(11),str(fake.random_number(12)).zfill(12),"2018-04-01T13:00:00Z",1,"5000"]
        csv_writer.writerow(l)