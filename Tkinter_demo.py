#!/usr/bin/env python
#coding=utf-8

import tkinter as tk
from tkinter import ttk
from make_trans import make

def go(*args):
	print(comboxlist.get())

windows = tk.Tk()
windows.title('汇率小工具')
windows.geometry('450x400')
var1 = tk.StringVar()
li1 = ['港元(HKD)', '澳门元(MOP)', '台币(TWD)', '欧元(EUR)', '美元(USD)', '英镑(GBP)', '澳元(AUD)', '韩元(KRW)', '日元(JPY)',
	   '离岸人民币(CNH)', '加拿大元(CAD)', '俄罗斯卢布(RUB)', '泰国铢(THB)', '菲律宾比索(PHP)', '阿尔巴尼亚列克(ALL)', '阿根廷比索(ARS)',
	   '阿鲁巴岛弗罗林(AWG)', '阿联酋迪拉姆(AED)', '列斯荷兰盾(ANG)', '阿塞拜疆新马纳特(AZN)', '安哥拉宽扎(AOA)', '巴哈马元(BSD)', '巴林第纳尔(BHD)',
	   '巴巴多斯元(BBD)', '白俄罗斯卢(BYR)', '伯利兹元(BZD)', '百慕大元(BMD)', '不丹卢比(BTN)', '玻利维亚诺(BOB)', '博茨瓦纳普拉(BWP)', '巴西里亚伊(BRL)',
	   '保加利亚列瓦(BGN)', '布隆迪法郎(BIF)', '孟加拉塔卡(BDT)', '文莱元(BND)', '佛得角埃斯库多(CVE)', '哥伦比亚比索(COP)', '哥斯达黎加科朗(CRC)',
	   '古巴比索(CUP)', '捷克克朗(CZK)', '瑞士法郎(CHF)', '塞浦路斯镑(CYP)', '智利比索(CLP)', '阿尔及利亚第纳尔(DZD)', '丹麦克朗(DKK)', '多米尼加比索(DOP)',
	   '吉布提法郎(DJF)', '埃及镑(EGP)', '埃塞俄比亚比尔(ETB)', '厄瓜多尔苏克雷(ECS)', '厄立特里亚(ERN)', '福克兰群岛镑(FKP)', '斐济元(FJD)', '冈比亚达拉西(GMD)',
	   '圭亚那元(GYD)', '加纳塞地(GHS)', '几内亚法郎(GNF)', '危地马拉格查尔(GTQ)', '直布罗陀镑(GIP)', '海地古德(HTG)', '洪都拉斯伦皮拉(HNL)', '克罗地亚库纳(HRK)',
	   '匈牙利福林(HUF)', '冰岛克朗(ISK)', '印度卢比(INR)', '印度尼西亚卢比盾(IDR)', '伊朗里亚尔(IRR)', '伊拉克第纳尔(IQD)', '以色列镑(ILS)', '牙买加元(JMD)',
	   '约旦第纳尔(JOD)', '朝鲜圆(KPW)', '哈萨克斯坦腾格(KZT)', '柬埔寨利尔斯(KHR)', '开曼岛元(KYD)', '科摩罗法郎(KMF)', '肯尼亚先令(KES)', '科威特第纳尔(KWD)',
	   '老挝基普(LAK)', '拉脱维亚拉图(LVL)', '黎巴嫩镑(LBP)', '莱索托洛提(LSL)', '利比里亚元(LRD)', '利比亚第纳尔(LYD)', '立陶宛里塔斯(LTL)', '斯里兰卡卢比(LKR)',
	   '马其顿第纳尔(MKD)', '马拉维克瓦查(MWK)', '马来西亚林吉特(MYR)', '马尔代夫卢非亚(MVR)', '毛里塔尼亚乌吉亚(MRO)', '毛里求斯卢比(MUR)', '墨西哥比索(MXN)',
	   '摩尔多瓦列伊(MDL)', '蒙古图格里克(MNT)', '摩洛哥道拉姆(MAD)', '缅甸元(MMK)', '马达加斯加阿里亚里(MGA)', '纳米比亚元(NAD)', '尼泊尔卢比(NPR)',
	   '尼加拉瓜科多巴(NIO)', '尼日利亚奈拉(NGN)', '挪威克朗(NOK)', '新西兰元(NZD)', '阿曼里亚尔(OMR)', '巴基斯坦卢比(PKR)', '巴拿马巴尔博亚(PAB)',
	   '巴布亚新几内亚基那(PGK)', '巴拉圭瓜拉尼(PYG)', '波兰兹罗提(PLN)', '秘鲁索尔(PEN)', '卡塔尔利尔(QAR)', '罗马尼亚新列伊(RON)', '卢旺达法郎(RWF)',
	   '瑞典克朗(SEK)', '萨尔瓦多科朗(SVC)', '圣多美多布拉(STD)', '沙特阿拉伯里亚尔(SAR)', '塞舌尔法郎(SCR)', '塞拉利昂利昂(SLL)', '斯洛文尼亚托拉捷夫(SIT)',
	   '所罗门群岛元(SBD)', '索马里先令(SOS)', '圣赫勒拿群岛磅(SHP)', '苏丹第纳尔(SDG)', '斯威士兰里兰吉尼(SZL)', '新加坡元(SGD)', '叙利亚镑(SYP)',
	   '土耳其新里拉(TRY)', '坦桑尼亚先令(TZS)', '汤加潘加(TOP)', '特立尼达和多巴哥元(TTD)', '突尼斯第纳尔(TND)', '塔吉克斯坦索莫尼(TJS)', '乌克兰赫夫米(UAH)',
	   '乌拉圭新比索(UYU)', '乌干达先令(UGX)', '瓦努阿图瓦图(VUV)', '委内瑞拉博利瓦(VEF)', '越南盾(VND)', '萨摩亚塔拉(WST)', '多哥非洲共同体法郎(XOF)',
	   '刚果中非共同体法郎(XAF)', '格林纳达东加勒比元(XCD)', '太平洋法郎(XPF)', '也门里亚尔(YER)', '津巴布韦元(ZWD)', '南非兰特(ZAR)', '赞比亚克瓦查(ZMW)']

def get_math():    #获取输入的人民币金额
	var = e.get()
	return var

def insert_result(): #计算换算的结果
	math = get_math() #将输入栏的人民币值赋给math参数
	var = make(b,math)
	text.insert(1.0,var) #显示换算结果

b1 = tk.Button(windows,text="输入人民币金额",width=15,height=2)
b1.pack()
e = tk.Entry(windows)
e.pack()
b2 = tk.Button(windows,text="请选择币种",width=15,height=2)
b2.pack()

comboxlist = ttk.Combobox(windows,textvariable=var1)#初始化下拉栏
comboxlist['values'] = li1 #将列表导入下拉栏
comboxlist['state'] = 'readonly'
comboxlist.current(0) #提取选中的后切换到第一个位置的选项
b = comboxlist.get() #获取选取框中的值
comboxlist.bind("choose currency",go) #绑定go函数
comboxlist.pack()

b3 = tk.Button(windows,text="兑换",width=15,height=2,command=insert_result)
b3.pack()

text = tk.Text(windows,height=2)
text.pack()

windows.mainloop()


