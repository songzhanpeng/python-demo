import json

data_str = """全车空调温度同步			icon_action_TemperatureSynchronization
前除霜			icon_action_FrontDefrosting
空调工作模式			icon_action_HAVCWorkingMode
负离子			icon_action_NegativeIon
远光灯闪烁			icon_action_HighBeam
干燥除味			icon_action_DryDeodorization
电动桌板			icon_action_ElectricTable
禁用雨刮			icon_action_DisableRainHanger
屏幕滑动			icon_action_ScreenSliding
解锁通风开关			icon_action_ReleaseVentSwitch
视线唤醒			icon_action_EyeAwakening
香氛运行时间			icon_action_FragranceRunningTime
导航路线推荐			icon_condition_NavigationRouteRecommendation
高音控制			icon_action_TREBLE
中音控制			icon_action_MidToneControl
低音控制			icon_action_BASS
重低音控制			icon_action_SubwooferControl
屏幕开关			icon_action_ScreenSwitch
屏幕滑动禁用			icon_action_ScreenSlidingDisabled
播放模式			icon_action_PlaybackMode
开始播放			icon_action_StartPlaying
暂停播放			icon_action_StopPlaying
下一曲			icon_action_NextSong
上一曲			icon_action_PreviousSong
照片			icon_action_Photo
录像			icon_action_PictureRecording
播报天气			icon_action_BroadcastWeather
兴趣点搜索			icon_condition_PointOfInterest
导航到目的地			icon_action_Navi
雨量强度							icon_condition_RainfallIntensity
道路类型							icon_condition_Road
无线充电状态							icon_condition_WirelessChargingStatus
性别							icon_condition_Gender
副驾驶性别							icon_action_GenderOfCoDriver
疲劳							icon_condition_Tired
分心							icon_condition_Distraction
服饰颜色							icon_condition_ClothingColor
放电状态							icon_action_DischargeState"""

arr = data_str.split('\n')
image_files = []
data_json_str = '{'

for i in arr:
    res = i.split('\t')
    zh_name = res[0]
    name = res[-1]
    image_files.append(f'{name}.png')
    data_json_str += f"""
        "{name}": {{
            "commandIcon": require("./white/{name}.png"),
            "conditionIcon": require("./black/{name}.png"),
            "name": "{name}",
            "alias": ["{name}", "{zh_name}"]
        }},
    """

data_json_str += '}'
print(data_json_str)


# 将list保存为JSON文件
with open('excel.json', 'w') as json_file:
    json.dump(image_files, json_file, indent=4)

print("icons.json 文件已创建")
