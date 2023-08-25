# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:06:55 2023

@author: 86159
"""

import requests
import json

API_KEY='72c413237e5aa1eecbaf2860b51b023e'
JOBS_UUID_TUPLE = ("d81465143a5111ee800000505692225b")
#JOBS_UUID_TUPLE = ("63ed11d442fa11ee800000505692225b","6404c0b842fa11ee800000505692225b","6417362642fa11ee800000505692225b","6423d30442fa11ee800000505692225b","6437548842fa11ee800000505692225b","644892fc42fa11ee800000505692225b","6459160442fa11ee800000505692225b","646aa95a42fa11ee800000505692225b","6480235242fa11ee800000505692225b","64919e6642fa11ee800000505692225b","64ab6c6042fa11ee800000505692225b","64b9f7ee42fa11ee800000505692225b")

def start_jobs(jobs_list):
    data = []
    # tuple只有一个时，为str类型
    if isinstance(jobs_list,str):
        data = [{"job_uuid":jobs_list, "action": "start"}]
    else:
        for i in range(len(jobs_list)):
            tpobj = {"job_uuid":jobs_list[i], "action": "start"}
            data.append(tpobj)
    r = requests.post('http://192.168.3.118/d2/r/v2/job/action', json=data, headers={"X-API-Key":API_KEY})
    if json.loads(r.text)['error']['code'] == 0:
        return '已启动'
    else:
        return '错误:'+r.text
    
if __name__ == '__main__':
    result = start_jobs(JOBS_UUID_TUPLE)
    print(result)