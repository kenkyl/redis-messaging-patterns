import redis
import time
import sys

REDIS_HOST = 'localhost'
REDIS_PORT = 6379 
STREAM_NAME = 'process-stream'
 
def main(): 
    r = redis.StrictRedis(REDIS_HOST, REDIS_PORT, charset="utf-8", decode_responses=True)

    ### Streams Consumer uses XREVRANGE to read the 10 most recent messags in the stream 
    res = r.xrevrange(STREAM_NAME, '+', '-', count=10)

    # Calculate and print the average completeion value 
    total = 0
    num_messages = len(res)
    for message in res:
        total = total + int(message[1].get('completion-value'))
        
    if (num_messages > 0):
        avg = total / num_messages
        print(f'The average completion value of the last 10 proceses in stream {STREAM_NAME} is: {avg}')
    else:
        print(f'Stream {STREAM_NAME} is empty...')

if __name__ == "__main__":
    stream_num = '1'
    if (len(sys.argv) > 1):
        stream_num = str(sys.argv[1])
    STREAM_NAME = f'{STREAM_NAME}:{stream_num}'
    main()    

