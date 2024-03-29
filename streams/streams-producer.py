import redis
import random
import time
import sys

REDIS_HOST = 'localhost'
REDIS_PORT = 6379 
STREAM_NAME = 'process-stream'
 
def main(): 
    r = redis.StrictRedis(REDIS_HOST, REDIS_PORT, charset="utf-8", decode_responses=True)

    while True:
        # Generatre pseduo random process id and completion number
        pid = random.randint(1000,10000)
        num = random.randint(0,100)
        message = { 'pid': pid, 'completion-value': num}

        ### Publisher uses XADD to send a message to Subscribers on the Channel ###
        res = r.xadd(STREAM_NAME, message)

        print(f'Streams Producer sent \"{message}\" to stream {STREAM_NAME}')
        time.sleep(3)

if __name__ == "__main__":
    stream_num = '1'
    if (len(sys.argv) > 1):
        stream_num = str(sys.argv[1])
    STREAM_NAME = f'{STREAM_NAME}:{stream_num}'
    main()    