# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


import pandas as pd
from pymongo import MongoClient


class SunlightPipeline(object):

    def open_spider(self,spider):
        self.num=0
        client = MongoClient()

        self.collection = client["sunlight"]["data"]

    # def close_spider(self,spider):
    #     self.df.to_csv("./data.csv")

    def process_item(self, item, spider):
        item["content"]=self.process_content(item["content"])
        self.collection.insert(dict(item))

        #print(item["title"], item["href"], item["publish_date"], "|".join(item["content"]), "|".join(item["content_img"]))
        # title=item["title"]
        # href=item["href"]
        # time=item["publish_date"]
        # text= "|".join(item["content"]) if "|".join(item["content"]) is not None else "none"
        # pic="|".join(item["content_img"]) if "|".join(item["content_img"]) is not None else "none"

        # temp_df=pd.DataFrame([title,href,time,text,pic],
        #                      columns=["title","href","time","content","image"])
        # # self.df=self.df.append(temp_df)
        # print(temp_df)
        #print([title,href,time,text,pic])

        # print(self.num)
        # self.df.iloc[self.num]=[title,href,time,text,pic]
        self.num += 1
        print(self.num)
        return item


    def process_content(self,content):
        content=[re.sub(r"\xa0|\s","",i) for i in content]
        content=[i for i in content if i.strip()!="" ]
        return content