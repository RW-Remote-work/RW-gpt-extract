## 文档整理

### 1. 影片分页接口
   接口url:
   http://localhost:9000/cms/queryLongVideo?page_index=1&page_size=10

    1.1 查询条件
        page_index 
        page_size 
           "data": {
                "total": 73544,
                "items": [
                    {
                        "id": "NV000000000001",
                        "title": "神魔契约之如意厨房",
                        "genre": "爱情|玄幻",
                        "tag": "新闻|超自然|穿越|催泪|温暖|当代|网络大电影",
                        "tag_raw": "华语,剧情,资讯,国内/大陆,普通话,超自然,穿越,催泪,温暖,文艺,当代,烂片,网络大电影,内地,4K,独播",
                        "connect_tag": "aaa",
                        "director": "李暻天 ",
                        "cast": "朱丽岚|叶小开",
                        "score": 7.2,
                        "category": "电影",
                        "boutique_tags": "你好|你好1|"
                    },
            
    
    1.2 修改精品标签 http://localhost:9000/cms/queryLongVideo
    {
        "id":"NV000000000001",
        "tag_id_list":"1|2",
        "method":"update_boutique_tags"
    }
