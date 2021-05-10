import redis 
import time
import sys

REDIS_HOST = 'localhost'
REDIS_PORT = 6379 
QUEUE_NAME = 'my-queue'
 
def main(): 
    r = redis.StrictRedis(REDIS_HOST, REDIS_PORT, charset="utf-8", decode_responses=True)

    while True:
        ### Producer uses BRPOP to grab an available message from the List (Queue)  
        ### Note: will block for specified timeout until a message is available (0=infinite) 
        res = r.brpop(QUEUE_NAME, timeout=0)

        if (res):
            print(f'List Blocking Consumer grabbed task {res}')
        # sleep to simulate processing of the item
        time.sleep(1)

if __name__ == "__main__":
    queue_num = '1'
    print(str(sys.argv))
    if (len(sys.argv) > 1):
        queue_num = str(sys.argv[1])
    QUEUE_NAME = f'{QUEUE_NAME}:{queue_num}'
    main()    