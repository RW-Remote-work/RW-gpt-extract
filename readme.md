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
### 2. 标签 
   查询标签接口url:
   http://localhost:9000/cms/tags

    2.1 查询参数：
    category: 默认查询标签池以及风格所有数据 
              
    返回数据格式 
    {"tag":[***{"id","name"}],"genre":[***{"id","name"}]}
    2.1 若不带参数返回总标签以及所有风格
    2.2 带参数分类 则返回分类下的标签以及风格
    e.g: http://localhost:9000/cms/tags?category=电影
    
    
    新增标签
    2.2 新增参数：
    {
	"tag_name":"黑色",
	
	"method":"create_tag"
	"category": "**"
	}
	若category为空或者为all, 则表示标签在所有分类中都新增
	若category为其中一类, 则表示在分类中的其中一项新增标签
   
    删除标签
     {
	"tag_name":"黑色",
	
	"method":"delete_tag"
	"category": "**"
	}
    
    修改标签
     {
	"tag_name":"黑色",
	"method":"update_tag"
    "tag_name_new":"3083"
	"category": "**"
	}
    
    新增风格
     {
	"genre_name":"黑色",
	
	"method":"create_genre"
	"category": "**"
	}
	
	
	
	
### 3. 查询精品标签接口url:
   http://localhost:9000/cms/boutiqueTags
   {
   {
    "retCode": 0,
    "msg": "请求执行成功",
    "data": [
        "你好",
        "你好1"
    ]
}
}
    
    新增精品标签
    {
	"method":"create_tag",
	"tag_name":"你好2"
    }
    
    删除标签
    {

	"method":"delete_tag",
	"tag_name":"你好2"
    }

### 4. 下发接口
#### 4.1 查询接口列表: GET
接口url:
http://localhost:9000/cms/interface

返回结果：
```
{
    "retCode": 0,
    "msg": "请求执行成功",
    "data": [
        {
            "id": 1,
            "algHandler": "猜你想看12",
            "desc": "到哦是计算机数据",
            "status": false
        },
        {
            "id": 2,
            "algHandler": "猜你想看121",
            "desc": "到哦是计算机数据",
            "status": false
        },
        {
            "id": 3,
            "algHandler": "猜你想看1211",
            "desc": "到哦是计算机数据",
            "status": false
        }
    ]
}
```

#### 4.2 查询接口详情列表: GET
接口url:
http://localhost:9000/cms/interface?id=**
返回结果：
```
{
    "retCode": 0,
    "msg": "请求执行成功",
    "data": {
        "id": 3,
        "algHandler": "猜你想看1211",
        "contentClassify": "电影",
        "filterDay": "15",
        "filterMoviesInfo": "",
        "filterType": [],
        "highlightsMoviesInfo": "",
        "modelsRecNum": [
            "1",
            "2",
            "3"
        ],
        "orderType": "机器排序",
        "recMovieType": [
            "警",
            "察"
        ],
        "returnCount": 10,
        "strategys": [
            "大海的",
            "0ujsd"
        ]
    }
}
```
#### 4.3 注册接口
接口url:
http://localhost:9000/cms/interface
post body:
```
{
    "method": "create_interface",
	"handler":**,
    "description":**
}
```


#### 4.4 修改接口详情列表: POST
接口url:
http://localhost:9000/cms/interface?id=**

post body:
```
{
	"method":"update_interface_detail",
	"contentClassify":"电影",
	"filterDay":15,
	"filterType":["播放历史","vip付费"],
	"modelsRecNum":["1","2","3"],
	"orderType":"机器排序",
	"returnCount":10,
	"strategys":["大海的","0ujsd"]
}
```

返回结果：


#### 4.5 修改接口状态-> 下发接口
接口url:
http://localhost:9000/cms/interface?id=**
post body:
```
{
	"method":"update_interface_state",
}
```

#### 4.6 删除接口
接口url:
http://localhost:9000/cms/interface?id=**
post body:
```
{
	"method":"delete_interface",
}
```


### 5 用户操作记录 method: get
接口url:
http://localhost:9000/cms/userHistory

返回格式：
```
{
    "retCode": 0,
    "msg": "请求执行成功",
    "data": {
        "username": "liuhang6",
        "action_list": [
            {
                "operate": "create",
                "model_table": "interface",
                "operate_time": "2020-05-11 09:45:17"
            },
            {
                "operate": "update",
                "model_table": "interface_detail",
                "operate_time": "2020-05-11 10:14:49"
            },
            {
                "operate": "update",
                "model_table": "interface_detail",
                "operate_time": "2020-05-11 10:17:12"
            },
            {
                "operate": "update",
                "model_table": "interface_detail",
                "operate_time": "2020-05-11 16:14:02"
            },
            {
                "operate": "update",
                "model_table": "interface_detail",
                "operate_time": "2020-05-11 17:00:29"
            },
            {
                "operate": "update",
                "model_table": "interface_detail",
                "operate_time": "2020-05-11 17:25:31"
            }
        ]
    }
}

```

### 6 用户菜单权限查询 method: get
接口url:
http://localhost:9000/cms/permission
```
{
    "retCode": 0,
    "msg": "请求执行成功",
    "data": [
        {
            "id": 1,
            "title": "服务器管理",
            "key": "/machine",
            "icon": "ant-cloud",
            "children": [
                {
                    "id": 2,
                    "title": "服务器列表",
                    "key": "/machine/machinelist",
                    "icon": "bars"
                },
                {
                    "id": 3,
                    "title": "添加服务器",
                    "key": "/machine/addmachine",
                    "icon": "plus-circle"
                }
            ]
        },
        {
            "id": 4,
            "title": "接口管理",
            "key": "/algorithms",
            "icon": "setting",
            "children": [
                {
                    "id": 5,
                    "title": "接口列表",
                    "key": "/algorithms/alglist",
                    "icon": "bars"
                },
                {
                    "id": 6,
                    "title": "添加接口",
                    "key": "/algorithms/addalg",
                    "icon": "plus-circle"
                },
                {
                    "id": 7,
                    "title": "接口配置",
                    "key": "/algorithms/config",
                    "icon": "appstore"
                }
            ]
        },
        {
            "id": 8,
            "title": "标签管理",
            "key": "/tags",
            "icon": "tags",
            "children": [
                {
                    "id": 9,
                    "title": "长视频影片池",
                    "key": "/tags/longVideoInfos",
                    "icon": "instagram"
                },
                {
                    "id": 10,
                    "title": "长视频标签池",
                    "key": "/tags/longTagInfos",
                    "icon": "carry-out"
                }
            ]
        },
        {
            "id": 11,
            "title": "效果追踪",
            "key": "/effects",
            "icon": "rise",
            "children": [
                {
                    "id": 12,
                    "title": "用户分组",
                    "key": "/effects/user_classify",
                    "icon": "user"
                },
                {
                    "id": 13,
                    "title": "推荐接口",
                    "key": "/effects/recommend",
                    "icon": "youtube"
                },
                {
                    "id": 14,
                    "title": "搜索展示",
                    "key": "/effects/search",
                    "icon": "reddit"
                }
            ]
        }
    ]
}
```

### 7 模型查询 method: get
接口url:
http://localhost:9000/cms/models
```
{
    "retCode": 0,
    "msg": "请求执行成功",
    "data": [
        {
            "id": 1,
            "model_key": "activity",
            "model_value": "舆情",
            "platform": "mivideo",
            "model_type": "基于影片"
        },
        {
            "id": 2,
            "model_key": "avg_user_tags",
            "model_value": "平均用户标签画像",
            "platform": "mivideo",
            "model_type": "基于影片"
        },
        {
            "id": 3,
            "model_key": "hot_movies",
            "model_value": "热点",
            "platform": "mivideo",
            "model_type": "基于影片"
        },
        {
            "id": 4,
            "model_key": "long_time_tags_",
            "model_value": "长期偏好",
            "platform": "mivideo",
            "model_type": "基于用户"
        },
        {
            "id": 5,
            "model_key": "real_time_tags_",
            "model_value": "实时偏好",
            "platform": "mivideo",
            "model_type": "基于用户"
        },
        {
            "id": 6,
            "model_key": "short_time_tags_",
            "model_value": "短期偏好",
            "platform": "mivideo",
            "model_type": "基于用户"
        },
        {
            "id": 7,
            "model_key": "user_",
            "model_value": "用户聚合特征",
            "platform": "mivideo",
            "model_type": "基于用户"
        },
        {
            "id": 8,
            "model_key": "watch_movie_action",
            "model_value": "实时观影记录",
            "platform": "mivideo",
            "model_type": "基于用户"
        },
        {
            "id": 10,
            "model_key": "_actor",
            "model_value": "相似演员召回",
            "platform": "mivideo",
            "model_type": "基于影片"
        },
        {
            "id": 11,
            "model_key": "_boutique_tag",
            "model_value": "精选标签召回",
            "platform": "mivideo",
            "model_type": "基于影片"
        },
        {
            "id": 12,
            "model_key": "_director",
            "model_value": "导演召回",
            "platform": "mivideo",
            "model_type": "基于影片"
        },
        {
            "id": 13,
            "model_key": "_fis",
            "model_value": "频繁项集",
            "platform": "mivideo",
            "model_type": "基于影片"
        },
        {
            "id": 14,
            "model_key": "_item",
            "model_value": "基于ItemCF",
            "platform": "mivideo",
            "model_type": "基于影片"
        },
        {
            "id": 15,
            "model_key": "_person",
            "model_value": "人为控制",
            "platform": "mivideo",
            "model_type": "基于影片"
        },
        {
            "id": 16,
            "model_key": "_sim",
            "model_value": "基于标签相似",
            "platform": "mivideo",
            "model_type": "基于影片"
        }
    ]
}
```

#### 7.1 新增模型
params: 
platform: 
值： mivideo, mitv
接口url:
http://localhost:9000/cms/models
post body:
```
{
	"method":"create_model",
    "model_key":"",
    "model_value":"",
    "platform":"",
    "model_type":"",
}
```

#### 7.1 修改模型
接口url:
http://localhost:9000/cms/models?id=1
post body:
```
{
	"method":"update_model",
    "model_key":"",
    "model_value":"",
    "platform":"",
    "model_type":"",
}
```

### 8. 用户认证

#### 8.1 查询用户
http://localhost:9000/cms/users
```
{
    "retCode": 0,
    "msg": "请求执行成功",
    "data": [
        {
            "id": 1,
            "last_login": "2020-05-11 09:32:14",
            "is_superuser": true,
            "username": "liuhang6",
            "is_active": false,
            "groups": ""
        },
    ]
}

```
#### 8.2 修改用户权限
http://localhost:9000/cms/users?id=1
post body:
```
{
	
	"method":"update_user",
	"groups": "1",
	"is_superuser": "1",
	"is_active": "1"
}
```

#### 8.3 查询组
http://localhost:9000/cms/groups
```
{
    "retCode": 0,
    "msg": "请求执行成功",
    "data": [
        {
            "id": 1,
            "name": "小米视频运营组"
        },
        {
            "id": 2,
            "name": "ott运营组"
        }
    ]
}
```
#### 8.4 查询组以及其菜单权限
http://localhost:9000/cms/groups?id=1
```
{
    "retCode": 0,
    "msg": "请求执行成功",
    "data": {
        "id": 1,
        "name": "小米视频运营组",
        "groups": [
            "接口管理",
            "接口列表",
            "添加接口",
            "接口配置",
            "效果追踪",
            "用户分组",
            "推荐接口",
            "搜索展示"
        ]
    }
}
```

#### 8.5 修改组可见菜单
接口url
http://localhost:9000/cms/groups?id=1
post body:
```
{
	
	"method":"update_group",
	"menus":["4","5","6","7","11","12","13","14"],
	"group_name": "",
}
}
```

