## 登陆云Hadoop集群



集群名：july

用户名: student 密码: student

ip：47.110.89.171  端口: 22

登陆方式：通过Xshell或SecureCRT等软件远程登录到集群中



(yarn 等)网页链接登陆用户名密码： 用户名: op 密码 bigdata123
Yarn: https://knox.c-d61ff25365d822df.cn-hangzhou.emr.aliyuncs.com:8443/gateway/cluster-topo/yarn/?spm=a2c8w.12375636.link_list.2.434c28d0RjHDij


## ssh  登陆方式：

使用 SecureCRT 或 Putty 等远程登录软件登陆（以 SecureCRT 为例）：
新建连接，配置 IP，端口为 22，用户名为 student 

## 操作命令参考-假设学号为 5642214
大家一开始可以将 teacher下的文件夹拷贝到自己的目录，**“不要删除teacher文件夹下的数据”**，比如：
cp -r teacher/* 5642214/

### 创建hdfs目录

hadoop fs -mkdir -p /sxy-new/5642214/input
### 将本地文件上传到hdfs中
大家感兴趣的话，可以通过 `rz -bey` 命令上传自己的文件到linux机器中

hadoop fs -put data/text*.txt /sxy-new/5642214/input

hadoop fs -ls /sxy-new/5642214/input

hadoop fs -mkdir -p /sxy-new/5642214/output

### 本地验证代码是否正确

echo "foo foo quux labs foo bar quux" | python count_mapper.py

echo "foo foo quux labs foo bar quux" | python count_mapper.py | sort -k1,1 | python count_reducer.py

head text1.txt | python count_mapper.py

head text1.txt | python count_mapper.py | sort -k1,1 | python count_reducer.py > result.txt

### 运行MapReduce程序

hadoop jar hadoop-streaming-2.8.5.jar  -D mapreduce.job.name="5642214_test" -file code/count_mapper.py  -mapper code/count_mapper.py  -file code/count_reducer.py -reducer code/count_reducer.py -input /sxy-new/5642214/input*  -output /sxy-new/5642214/output/1

### 获取结果数据

hadoop fs -getmerge /sxy-new/5642214/output/1 output.txt