# start_jobs
1. 启动多个/单个备份或者恢复作业，需要提供作业的jobuuid
2. 使用api-key登录
3. JOBS_UUID_TUPLE中可以填入多个jobuuid或者一个jobuuid
  - 格式如下：
  - 启动单个作业：JOBS_UUID_TUPLE = ("job_uuid") 或者 JOBS_UUID_TUPLE = "d81465143a5111ee800000505692225b"
  - 启动多个作业：JOBS_UUID_TUPLE = ("job_uuid1", "job_uuid2", "job_uuid3"...)
