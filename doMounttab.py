#写一个打印环境里挂载镜像的程序
#在linux系统当中
#proc/mounts/内容分别是 设备路径;挂载点;以什么文件系统挂载
import os


def parse_mounts():
    result = []
    if os.path.exists('/proc/mounts'):
        fobj = open('/proc/mounts')
        for line in fobj:
            line = line.strip()
            words = line.split()
            if len(words) > 5:
                res = (words[0],words[1],words[2],'({})'.format(' '.join(words[3:-2])))
            else:
                res = (words[0],words[1],words[2])
            result.append(res)
        fobj.close() 
    return result

def mount_details():
    result = parse_mounts()
    for x in result:
        if len(x) == 4:
            print('{} on type {} {}'.format(*x))
        else:
            print('{} on type {}'.format(*x))
        
mount_details()