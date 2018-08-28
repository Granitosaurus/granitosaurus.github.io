Title: How to fix redis busy
Date: 2018-08-28
Tags: linux, guide, redis, python
Slug: redis-busy
Summary: How to fix annoying redis busy error when working with redis lua scripts and multiple clients

Imagine scenario where you have a single redis server (which is single threaded) and you have multiple clients:

![redis structure]({filename}/images/redis-busy1.png)

Eventhough redis is single-threaded it has no problem handling this setup since it's blazing fast and knows how to manage it's task queue.  
However if we ask redis server to perform a lua script evaluation it might take a while, which ends up with clients getting this nasty error:

> redis.exceptions.ResponseError: BUSY Redis is busy running a script. You can only call SCRIPT KILL or SHUTDOWN NOSAVE

![redis structure]({filename}/images/redis-busy2.png)


# The Fix

Thi fix this we need to apply a fix to the client side - make it wait and retry this `ResponseError`:
 
To do this lets patch `Redis` class in python's `redis-py` client:

```
from redis import Redis

class MyRedis(Redis):
    lua_retry_time = 120  # how many times to retry

    # override execute to retry busy errors 
    def execute_command(self, *args, **options):
        if not self.lua_retry_time:
            return super().execute_command(*args, **options)
        wait_time = 0
        while wait_time < self.lua_retry_time:
            try:
                return super().execute_command(*args, **options)
            except ResponseError as e:
                if 'busy redis is busy' not in ''.join(e.args).lower():
                    raise e
                if wait_time == 0:  # only print once
                    print('Redis is busy, waiting up to 120 seconds...')
                time.sleep(2)
                wait_time += 2
        return super().execute_command(*args, **options)
```

Since every command in this client goes through `execute_command` method we can override it to keep retrying `Redis BUSY` errors for a fixed amount of time.

With this patch Redis client will retry the connection every 2 seconds if redis is busy evaluating LUA.

![redis final structure]({filename}/images/redis-busy3.png)

# Conclusion

I've been trying to find some in-built solution for this and couldn't believe there's no official approach, neither with redis itself nor python's redis client.   
The internet resources are very scarce around this issue too, so I figured I'd try and remedy this.
