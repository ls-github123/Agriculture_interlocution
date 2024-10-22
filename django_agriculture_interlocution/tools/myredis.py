from redis import Redis, ConnectionPool
class Mredis:
    def __init__(self, host='localhost', port=6379, db=0, password=None):
        # 创建连接池并设置密码
        pool = ConnectionPool(host=host, port=port, db=db, password=password)
        # 使用连接池创建 Redis 实例
        self.redis = Redis(connection_pool=pool)
    def str_set(self, key, value):
        return self.redis.set(key, value)
    def str_get(self, key):
        return self.redis.get(key)
    def str_del(self, key):
        return self.redis.delete(key)
    # list add
    def list_add(self, key, value):
        return self.redis.rpush(key, value)

    # list pop
    def list_pop(self, key):
        return self.redis.rpop(key)

    # list lrange
    def list_lrange(self, key, min, max):
        return self.redis.lrange(key, min, max)

    # list llen
    def list_llen(self, key):
        return self.redis.llen(key)

    # list lrem
    def list_lrem(self, key, value):
        return self.redis.lrem(key, -1, value)

    # list rpoplpush
    def list_rpoplpush(self, list1, list2):
        return self.redis.rpoplpush(list1, list2)

# 创建 Mredis 实例，并提供 Redis 服务器的密码
mredis = Mredis(password='123456')

# 添加元素到列表
# mredis.list_add('bdlist1', '1001')
# mredis.list_add('bdlist1', '1002')
# mredis.list_add('bdlist1', '1003')
# mredis.list_lrem('bdlist1','1001')
# 获取并打印列表内容
# list_content = mredis.list_lrange('bdlist1', 0, -1)
# print(list_content)