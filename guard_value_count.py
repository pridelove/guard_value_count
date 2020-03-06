import requests

# 输入你的Cookie
Ck = ''
room_id = 0  # 房间号 需要长号
ruid = 0  # 主播uid

url = f'https://api.live.bilibili.com/xlive/app-room/v1/guardTab/topList?roomid={room_id}&page=1&ruid={ruid}&page_size=10'
headers = {
    'Host': "api.live.bilibili.com",
    'Origin': "https://live.bilibili.com",
    'Referer': f"https://live.bilibili.com/{room_id}",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    'Cookie': Ck
}
response = requests.request('get', url, headers=headers).json()
# 舰长页数
page = response['data']['info']['page']
# 舰长总数量
count_guard = response['data']['info']['num']
# 总督
guard_1 = 0
# 提督
guard_2 = 0
# 舰长
guard_3 = 0
# top3居然是额外算的..
if count_guard != 0:
    for each in range(0, 3):
        guard_value = response['data']['top3'][each]['guard_level']
        print('第%d项 guard_value=%d' % (each, guard_value))
        if guard_value == 1:
            guard_1 += 1
        elif guard_value == 2:
            guard_2 += 1
        elif guard_value == 3:
            guard_3 += 1
    for i in range(1, page + 1):
        url = f'https://api.live.bilibili.com/xlive/app-room/v1/guardTab/topList?roomid={room_id}&page={i}&ruid={ruid}&page_size=10'
        headers = {
            'Host': "api.live.bilibili.com",
            'Origin': "https://live.bilibili.com",
            'Referer': f"https://live.bilibili.com/{room_id}",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            'Cookie': Ck
        }
        re = requests.request('get', url, headers=headers).json()
        list_num = len(re['data']['list'])
        print('第%d页' % i)
        for index in range(0, list_num):
            guard_value = re['data']['list'][index]['guard_level']
            print('第%d项 guard_value=%d' % (index, guard_value))
            if guard_value == 1:
                guard_1 += 1
            elif guard_value == 2:
                guard_2 += 1
            elif guard_value == 3:
                guard_3 += 1
    sum = guard_1 * 19998 + guard_2 * 1998 + guard_3 * 198
    print("当前房间号:%d,船员数量%d,其中舰长%d个,提督%d个,总督%d个,合计价值%d元" % (room_id, count_guard, guard_3, guard_2, guard_1, sum))
else:
    print("房间:%d船员数为0" % room_id)
