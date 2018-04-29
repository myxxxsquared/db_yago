
```7252:M 28 Apr 13:30:06.033 # Can't save in background: fork: Cannot allocate memory```

```redis.exceptions.ResponseError: Command # 1 (SADD b' ' b'Jesper_Arvidsson') of pipeline caused error: MISCONF Redis is configured to save RDB snapshots, but it is currently not able to persist on disk. Commands that may modify the data set are disabled, because this instance is configured to report errors during writes if RDB snapshotting fails (stop-writes-on-bgsave-error option). Please check the Redis logs for details about the RDB error.```

vm.overcommit_memory=1
/proc/sys/vm/overcommit_memory
This file contains the kernel virtual memory accounting mode. Values are:
    0: heuristic overcommit (this is the default)
    1: always overcommit, never check
    2: always check, never overcommit
    In mode 0, calls of mmap(2) with MAP_NORESERVE set are not checked, and the default check is very weak, leading to the risk of getting a process "OOM-killed".  Under Linux 2.4
    any non-zero value implies mode 1.  In mode 2 (available since Linux 2.6), the total virtual address space on the system is limited to (SS + RAM*(r/100)), where SS is the size
    of the swap space, and RAM is the size of the physical memory, and r is the contents of the file /proc/sys/vm/overcommit_ratio.


# Enable journaling, http://www.mongodb.org/display/DOCS/Journaling
journal=false

数据形式为三元组<S, P, O>: 
- 给定一个si，给出它所有的P和O，<si, P, O> 
- 给定一个oi, 给出它所有的S和P，<S, P,oi> 
- 给定两个p1,p2, 给出同时拥有它们的S，<S, p1, *>, <S, p2, *> 
- 给定一个oi, 给出拥有这样oi最多的S 

~~~ redis 1.482851505279541, 0.7749776840209961, 7.836097955703735, 0.9336750507354736

~~~ mongodb 4.7268853187561035, 5.469435691833496, 9.937621831893921, 5.627211570739746
~~~ mongodb index 0.014734029769897461, 0.9819574356079102, 0.11789941787719727, 1.0129597187042236
~~~ [(b'England', b'isCitizenOf'), (b'England', b'wasBornIn'), (b'Philosophers_Behaving_Badly', b'created'), (b'male', b'hasGender'), (b'http://mel-thompson.co.uk', b'hasWebsite'), (b'England', b'livesIn')]
~~~ 155781
~~~ 172
~~~ (b'William_Goodwin_(cricketer)', 3


test_redis
{b'livesIn': [b'England'], b'hasWebsite': [b'http://mel-thompson.co.uk'], b'wasBornIn': [b'England'], b'hasGender': [b'male'], b'isCitizenOf': [b'England'], b'created': [b'Philosophers_Behaving_Badly']}
155781
3810
(b'Charles_Calvert,_5th_Baron_Baltimore', 3)
[1.3506970405578613, 0.7790884971618652, 8.378276824951172, 1.024606704711914]

test_mongodb
[(b'England', b'isCitizenOf'), (b'England', b'wasBornIn'), (b'Philosophers_Behaving_Badly', b'created'), (b'male', b'hasGender'), (b'http://mel-thompson.co.uk', b'hasWebsite'), (b'England', b'livesIn')]
155781
3810
(b'John_Robinson_(merchant)', 3)
[0.02207207679748535, 1.210127830505371, 0.9823455810546875, 1.045980453491211]

test_mongodb noindex
[(b'England', b'isCitizenOf'), (b'England', b'wasBornIn'), (b'Philosophers_Behaving_Badly', b'created'), (b'male', b'hasGender'), (b'http://mel-thompson.co.uk', b'hasWebsite'), (b'England', b'livesIn')]
155781
3810
(b'Joseph_Hall_(metallurgist)', 3)
[10.410542488098145, 5.799297571182251, 10.253386735916138, 6.1108808517456055]

[('livesIn', 'England'), ('wasBornIn', 'England'), ('hasGender', 'male'), ('isCitizenOf', 'England'), ('created', 'Philosophers_Behaving_Badly'), ('hasWebsite', 'http://mel-thompson.co.uk')]
155781
b'graduatedFrom'
3810
('Thomas_Anson_(cricketer)', 3)
[0.040230751037597656, 30.792487382888794, 14.629387855529785, 24.278236865997314]

