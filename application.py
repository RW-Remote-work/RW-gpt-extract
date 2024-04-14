import tornado.web
import config
from handlers.front.models.modelsService import ModelServiceHandler
from handlers.front.queryAllMachines import queryAllMachinesHandler
from handlers.front.queryAllAlgorithms import queryAllAlgorithmsHandler
from handlers.front.addAlgorithm import addAlgHandler
from handlers.front.addMachine import addMachineHandler
from handlers.front.deleteMachine import DeleteOneMachine
from handlers.front.changeSingleAlgState import singleAlgStateHandler
from handlers.front.findIndex import findIndexHandler
from handlers.front.multipleAlgOn import multipleAlgOnHandler
from handlers.front.multipleAlgOff import multipleAlgOffHandler
from handlers.front.changeMultipleAlgsState import ChangeMultipleAlgsStateHandler
from handlers.front.getAlgsVersion import GetAlgsVersionHandler
from handlers.front.getDefaultLongVideos import GetDefaultLongVideos
from handlers.front.modifyLongVideoTag import ModifyLongVideoTag
from handlers.front.modifyLongVideoGenre import ModifyLongVideoGenre
from handlers.front.modifyLongVideoConnectTag import ModifyLongVideoConnectTag
from handlers.front.querySpecialLongVideo import QuerySpecialLongVideo
from handlers.front.saveModelsConfig import SaveModelsConfig
from handlers.front.getAllModels import GetAllModels
from handlers.front.deleteInterface import DeleteInterface
from handlers.front.savaUserPoolFile import SaveUserPoolFile
from handlers.front.querySingleAlgInfo import QuerySingleAlgInfo
from handlers.front.queryInterfaceEffect import QueryInterfaceEffect
from handlers.front.saveFlowInfo import SaveFlowInfo
from handlers.front.queryUserFlow import QueryUserFlow
from handlers.front.queryShowName import QueryShowName
from handlers.front.longVideos.queryMoviesWithTitle import QueryMoviesByTitle, VirtualCategoryHandler
from handlers.front.longVideos.longvideo import LongVideo, TagHandler, BoutiqueTagHandler
from handlers.front.longVideos.queryVideoCertainTag import QueryVideoCertainTag
from handlers.front.longVideos.queryVideoCertainGenre import QueryVideoCertainGenre
from handlers.baseHandler import BaseHandler
from handlers.back.receiveHeartlibsHandler import HeartBeatHandler
from handlers.back.static import StaticInterfaceHandler
from handlers.back.filter import GlobalFilterHandler
from handlers.back.getUserPool import GetUserPool
from handlers.back.registerInterface import RegisterInterface
from handlers.test.getInfos import GetFilterIds
from handlers.front.interface import InterfaceHandler
from handlers.front.interface import InterfaceHandler1
from handlers.front.interface import EffectHandler
from handlers.front.user import UserHistoryHandler, UserHandler, GroupHandler
from handlers.front.menus import MenuHandler
from handlers.front.models import ModelHandler
from handlers.front.effect import (FlowMapHandler)
from handlers.front.interface import RuleHandler
from handlers.front.interface import WhiteListHandler



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # 前端页面路由
            (r'/', findIndexHandler),
            (r'/cms/queryAllMachines', queryAllMachinesHandler),  # 查询所有服务器
            (r'/cms/queryAllAlgorithms', queryAllAlgorithmsHandler),  # 查询所有算法
            (r'/cms/addAlg', addAlgHandler),  # 添加算法
            (r'/cms/querySingleAlgInfo', QuerySingleAlgInfo),  # 查询某一条接口的详细信息
            (r'/cms/deleteInterface', DeleteInterface),  # 删除某一个接口
            (r'/cms/addMachine', addMachineHandler),  # 添加服务器
            (r'/cms/deleteMachine', DeleteOneMachine),  # 删除服务器
            (r'/cms/changeAlgState', singleAlgStateHandler),  # 修改单条算法的上下线状态
            (r'/cms/multipleAlgOn', multipleAlgOnHandler),  # 批量上线算法后整体版本号加1
            (r'/cms/multipleAlgOff', multipleAlgOffHandler),
            (r'/cms/multipleAlgsOnOff', ChangeMultipleAlgsStateHandler),
            (r'/cms/getAlgsVersion', GetAlgsVersionHandler),  # 查询算法版本
            (r'/cms/getDefaultLongVideos',
             GetDefaultLongVideos),  # 长视频标签管理页面初始加载
            (r'/cms/modifyLongVideoTag', ModifyLongVideoTag),  # 长视频标签修改
            (r'/cms/modifyLongVideoGenre', ModifyLongVideoGenre),  # 长视频风格修改
            (r'/cms/modifyLongVideoConnectTag',
             ModifyLongVideoConnectTag),  # 长视频关联标签修改
            (r'/cms/querySpecialLongVideo', QuerySpecialLongVideo),  # 长视频检索
            (r'/cms/saveModelsConfig', SaveModelsConfig),  # 保存接口配置信息
            (r'/cms/getAllModels', GetAllModels),  # 获取所有配置好的模型
            (r'/cms/saveUserPoolFile', SaveUserPoolFile),  # 存储用户池文件
            (r'/cms/queryInterEffect', QueryInterfaceEffect),  # 查询接口效果
            (r'/cms/showDistinctName',
             QueryShowName),  # 查询数据库中不同的接口中文名显示在前端页面中
            (r'/cms/setUserFlow', SaveFlowInfo),  # 设置用户流
            (r'/cms/queryUserFlow', QueryUserFlow),  # 查询用户流
            (r'/cms/queryMoviesByTitle', QueryMoviesByTitle),  # 根据影片名称查询影片
            (r'/cms/queryLongVideo', LongVideo),  # 分页查询影片
            (r'/cms/queryVideoCertainTag', QueryVideoCertainTag),  # 查询长视频某一类标签
            (r'/cms/queryVideoCertainGenre',
             QueryVideoCertainGenre),  # 查询长视频某一类的风格
            (r'/cms/tags', TagHandler),
            (r'/cms/boutiqueTags', BoutiqueTagHandler),
            (r'/cms/permission', BaseHandler),
            (r'/cms/userHistory', UserHistoryHandler),
            (r'/cms/users', UserHandler),
            (r'/cms/menu', MenuHandler),
            (r'/cms/interface', InterfaceHandler1),  # 接口处理
            (r'/cms/models', ModelHandler),
            (r'/cms/modelService', ModelServiceHandler),
            (r'/cms/groups', GroupHandler),
            (r'/cms/flowMap', FlowMapHandler),  # 效果追踪--流量地图
            (r'/cms/effort', EffectHandler),
            (r'/cms/virtualCategory', VirtualCategoryHandler),
            (r'/cms/rules', RuleHandler),
            (r'/cms/whites', WhiteListHandler),
            # 后端接口
            (r'/cms/heartbeats', HeartBeatHandler),  # 接收心跳包
            (r'/cms/getUserPoolFiles', GetUserPool),  # 获取用户池
            (r'/cms/getInfos', GetFilterIds),  # 定时获取推荐页热门影片id
            (r'/cms/registerInterface', RegisterInterface),  # 接口注册
            (r'/cms/static', StaticInterfaceHandler),  # 静态文件　适合本地调用
            (r'/cms/filter', GlobalFilterHandler),  # 全局过滤
        ]

        super(Application, self).__init__(handlers, **config.setting)
