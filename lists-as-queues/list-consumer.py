import redis 
import sys

REDIS_HOST = 'localhost'
REDIS_PORT = 6379 
QUEUE_NAME = 'my-queue'
 
def main(): 
    r = redis.StrictRedis(REDIS_HOST, REDIS_PORT, charset="utf-8", decode_responses=True)

    ### Producer uses RPOP to immediately grab an available item from the List (Queue)  
    ### Note: will return nil if no items in queue 
    res = r.rpop(QUEUE_NAME)

    print(f'List Consumer grabbed task {res}')

if __name__ == "__main__":
    queue_num = '1'
    print(str(sys.argv))
    if (len(sys.argv) > 1):
        queue_num = str(sys.argv[1])
    QUEUE_NAME = f'{QUEUE_NAME}:{queue_num}'
    main()    