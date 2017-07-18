# -*- coding:utf-8 -*-

import redis
import configparser

Config = configparser.ConfigParser()
Config.read("../config/redis.ini")
print(Config['redis']['host'])

redisHost = Config.get("redis", "host")
redisPort = Config.get("redis", "port")
redisDb = Config.get("redis", "db")
redis = redis.Redis(redisHost, redisPort, redisDb)

print(redis)

redis.set("erbi", "fengfeng")
redis.set("sanpao", "guoguo")
name = redis.get("erbi")
print(name)
