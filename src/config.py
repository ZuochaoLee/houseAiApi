# -*- coding: UTF-8 -*-
#redis 配置参数
redis={
	#'host':'16c51b2287ed4bd2.m.cnbja.kvstore.aliyuncs.com',
	#'post':6379,
	#'db':4,
	#'passwd':'16c51b2287ed4bd2:zhugeZHAOFANG1116'
	'host':'localhost',
	'post':6380,
	'db':4,
	'passwd':''
}
#＊＊＊＊提取模版＊＊＊＊
pat_re={
	#价钱
	'price':u'[\u4e24\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*[万|w|W]',
	#面积
	'area':u'[\u4e24\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*平',
	#居室
	'room':u'[\u0000-\ueeee][居|室]',
	#厅
	'hall':u'[\u0000-\ueeee]厅',
	#卫
	'toilet':u'[\u0000-\ueeee]卫',
	#楼层
	'floor':u'([\u4e24\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*层|低楼层|高楼层|中楼层|阁楼|顶层|跃层|独栋|联排)',
	#户型
	'huxing':u'(别墅|公寓|平房|四合院|住宅|写字楼|单间|二手房|合租|整租|学区房)',
	#朝向
	'towards':u'(朝东|朝西|朝南|朝北|朝东南|朝东北|朝西北|朝西南)',
	#安全
	'security':u'(治安|安全|犯罪|公安|警察|风险|人身安全|财产安全|抢劫|盗窃|杀人|强奸|强暴|偷东西|小偷|入室|跳楼|自杀|保安)',
	#环境
	'environment':u'(公园|公园名称|绿化好|绿化率高|空气好|健康|锻炼|养生|健身|遛狗|养宠物|有老人|年纪大|注意身体)',
	#地段
	'diduan':u'(市中心|城郊|城乡结合|郊区|城外)',
	#环线
	'huanxian':u'[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*环',
	#地铁线
	'subway':u'([\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*号线|大兴线|昌平线|房山线|亦庄线|机场专线|八通线)',
	#公交线
	'bus':u'[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*路',
}
#＊＊＊＊去关键词模版＊＊＊＊
pat_sub={
	#价钱
	'price':u'(万|w|W)',
	#面积
	'area':u'(平|平米|米)',
	#居室
	'room':u'(居|居室|室)',
	#厅
	'hall':u'厅',
	#卫
	'toilet':u'卫',
	#楼层
	'floor':'',
	#户型
	'huxing':'',
	#朝向
	'towards':'',
	#安全
	'security':'',
	#环境
	'environment':'',
	#地段
	'diduan':'',
	#环线
	'huanxian':u'环',
	#地铁线
	'subway':u'号线',
	#公交线
	'bus':u'路'
}
#＊＊＊＊集合文件＊＊＊＊
set_file={
	#小区
	'borough':'borough.txt',
	#城区
	'cityarea':'cityarea.txt',
	#商圈
	'cityarea2':'cityarea2.txt',
	#楼盘
	'station':'subway.txt',
	#地铁
	#'building':'building.txt',
	#医院
	'hospital':'hospital.txt',
	#小学
	'primary.':'primary.txt'
}
#情感词典
feel_file={
	'positive':'positive.txt',
	'negative':'negative.txt'
}
#链接地址词典
url={
	'tuling':'http://www.tuling123.com/openapi/api?key=6c2cfaf7a7f088e843b550b0c5b89c26&&info=',
	'fy':'http://www.zhugefang.com',
	'xiaoqu':'http://www.zhugefang.com',
	'fjjsq':'http://www.zhugefang.com',
	'yhq':'http://www.zhugefang.com',
	'zjf':'http://www.zhugefang.com'
}
#意图词典
intent={
	'ree':u'[\u0000-\ueeee]*买|租|查询|查询一下|查一下|查一查|查查|找个|找一下|查|查找|看看|找找|要[\u0000-\ueeee]*房源|房子|好房|别墅|公寓|平房|四合院|住宅|写字楼|单间|二手房|合租房|整租房|学区房',
	#'ree':u'查一下',
	'intro':u'你是谁|你是什么？'
}
#文案词典
wenan={
	'intro':u'我是小诸葛啊',
	'fy':u'小诸葛为您推荐的房源，戳这里',
	'xqxx':u'请看小区基本信息',
	'xqzb':u'请看小区周边信息',
	'xqjg':u'请看小区价格信息',
	'xq':u'请看更多小区信息',
	'fjjsq':u'欢迎使用小诸葛房源计算器',
	'yhq':u'戳这里，优惠券大大滴有',
	'zjf':u'小诸葛告诉你中介费的秘密 都在这里了，嘿嘿'
}
#数字转换的词典
CN_NUM = {u'〇' : 0,u'一' : 1,u'二' : 2,u'三' : 3,u'四' : 4,u'五' : 5,u'六' : 6,u'七' : 7,u'八' : 8,u'九' : 9, u'零' : 0,
          u'壹' : 1,u'贰' : 2,u'叁' : 3,u'肆' : 4,u'伍' : 5,u'陆' : 6,u'柒' : 7,u'捌' : 8,u'玖' : 9,u'貮' : 2,u'两' : 2,}
CN_UNIT = {u'十' : 10,u'拾' : 10,u'百' : 100,u'佰' : 100,u'千' : 1000,u'仟' : 1000,u'万' : 10000,u'萬' : 10000,
           u'亿' : 100000000,u'億' : 100000000,u'兆' : 1000000000000,}
#分析模版词典
analysis={
	"v_chaxuncha":u"查询|查一下|查一查|查查|查找|问|告诉我|我想知道|挑选",
	"v_jisuan":u"算一下|算一算|计算",
	"v_yao":u"我想要|给我|发|来一打|买不起房|物价好贵|穷死了|给点钱|发给红包呗|发红包|有红包没|求红包",
	"v_duibi":u"对比|比较",
	"q_nanjia":u"哪家",
	"q_ruhe":u"如何|怎么样|怎么说|怎么收|贵吗",
	"q_jiaqian":u"多贵|多钱|多少钱|什么价|多少",#zhuyi多少
	"q_youma":u"有什么|有哪些",
	"q_shenme":u"什么|有什么用|是什么|什么意思|怎么回事|如何理解|代表什么|怎么讲|讲什么的|介绍|简介",#zhuyi什么
	"q_zuoshenme":u"做什么|干什么|讲什么|关于什么",
	"q_shijianchang":u"多久|多长时间|多少时间|几个小时",
	"q_nali":u"哪里|哪儿|什么地方|何处|哪",
	"a_pianyi":u"便宜|划算",
	# "ad_shijian":u"最新|刚刚|刚|最近|近期|这段时间",
	# "ad_nian":u"今年|去年|前年|2015年|2015年上半年|2015年下半年|上半年|下半年|\d*年",
	# "ad_jidu":u"(第)?[\u4e24\u4e00\u4e8c\u4e09]*季(度)?",
	# "ad_yue":u"[\u4e24\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*月",
	# "ad_ri":u"[\u4e24\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*(日|号)",
	"ad_shijian":u"@",
	"ad_nian":u"@",
	"ad_jidu":u"@",
	"ad_yue":u"@",
	"ad_ri":u"@",
	#优惠券
	"n_youhuiquan":u"优惠卷|大礼包|礼品|奖品",
	#中介费
	"n_zhongjiefei":u"中介费|中介费用|佣金|中介价格",
	"n_zhongjiegongsi":u"链家|我爱我家|麦田|爱屋吉乌|酷房|中原|21世纪|Q房|丽兹行|搜房|自如|家家顺|丁丁|房多多|寓见公寓|快有家|中诚致|汉宇|美联物业|德祐|蘑菇公寓|万福|青客公寓|安个家|安居客",
	#房价计算
	"n_fangjiajisuan":u"首付|月供",
	"n_cheng":u"[\u4e24\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*成",
	#房价查询
	"n_fangjia":u"房价|价格|成交价|挂牌价|均价",
	#小区周边
	"n_wo":u"我|这里|我这|我的位置|我所在的位置",
	"n_juli":u"距离|离|到|距",
	"n_fuwu":u"治安|绿化|安全|环境",
	"n_yinhang":u"银行|交通",
	"n_canting":u"餐厅|吃饭的地方|吃东西的地方|餐馆|中餐馆|中餐厅|自助餐|川菜|湘菜|粤菜|东北菜|大排档|西餐厅|披萨店|法国菜|日本料理|韩国料理|快餐店|肯德基|麦当劳|永和大王|冰淇淋店|火锅店|海底捞",
	"n_yingjuyuan":u"影剧院|电影院|KTV|游泳馆|篮球场|茶楼|咖啡厅|网吧|游戏厅|酒吧|美容店|美发店|旅行社|游乐园",
	"n_gongyuan":u"公园|景点|名胜古迹|纪念馆|博物馆",
	"n_xuexiao":u"学校|小学|中学|高中|大学|医院",
	"n_shangdian":u"商店|便利店|超市|商场|购物中心|ATM机|取款机|卫生间|洗手间|公共厕所|旅馆|宾馆|酒店",
	"n_gonganju":u"公安局|派出所|交通队|邮局",
	# "n_qita":u"地铁站|公交站|加油站|停车场|修理厂|高速口|高速公路|过街天桥|地下通道",
	"n_qita":u"@",
	# "n_fangzi":u"房源|房子|好房|别墅|公寓|平房|四合院|住宅|写字楼|单间|二手房|合租房|整租房|学区房",
	"n_fangzi":u"@",
	#价钱
	"price":u"[\u4e24\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*[万|w|W]",
	#面积
	"area":u"[\u4e24\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*平",
	#居室
	"room":u"[\u0000-\ueeee][居|室]",
	#厅
	"hall":u"[\u0000-\ueeee]厅",
	#卫
	"toilet":u"[\u0000-\ueeee]卫",
	#楼层
	"floor":u"([\u4e24\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*层|低楼层|高楼层|中楼层|阁楼|顶层|跃层|独栋|联排)",
	#户型
	"huxing":u"(别墅|公寓|平房|四合院|住宅|写字楼|单间|二手房|合租|整租|学区房)",
	#朝向
	"towards":u"(朝东|朝西|朝南|朝北|朝东南|朝东北|朝西北|朝西南)",
	#安全
	"security":u"(治安|安全|犯罪|公安|警察|风险|人身安全|财产安全|抢劫|盗窃|杀人|强奸|强暴|偷东西|小偷|入室|跳楼|自杀|保安)",
	#环境
	"environment":u"(公园|公园名称|绿化好|绿化率高|空气好|健康|锻炼|养生|健身|遛狗|养宠物|有老人|年纪大|注意身体)",
	#地段
	"diduan":u"(市中心|城郊|城乡结合|郊区|城外)",
	#环线
	"huanxian":u"[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*环",
	#地铁线
	"subway":u"[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*号线",
	#公交线
	"bus":u"[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\d]*路"
}
files={
	#小区
	'borough':'borough.txt',
	#城区
	'cityarea':'cityarea.txt',
	#商圈
	'cityarea2':'cityarea2.txt',
	#楼盘
	'station':'subway.txt',
	#地铁
	#'building':'building.txt',
	#医院
	'hospital':'hospital.txt',
	#小学
	'primary.':'primary.txt'
}
slave=["10.171.122.85","10.171.93.224","10.165.123.211","localhost"]






























