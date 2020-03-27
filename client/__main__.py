#!/usr/bin/env python3

import queue

import grpc

import job_api_pb2
import job_api_pb2_grpc

while True:
    print("Connecting...")
    channel = grpc.insecure_channel("localhost:50051")
    try:
        grpc.channel_ready_future(channel).result(timeout=5)
    except grpc.FutureTimeoutError as exc:
        channel.close()
        raise Exception("Error connecting to server") from exc
    print("connected.")

    stub = job_api_pb2_grpc.JobAPIStub(channel)
    q = queue.SimpleQueue()
    q.put(job_api_pb2.TrainJobRequest())
    stream = stub.TrainJob(iter(q.get, None))
    try:
        for _ in stream:
            if random.random() > 0.7:
                raise Exception("")
            output_req = job_api_pb2.TrainJobRequest()
            q.put(output_req)
            q.put(None)
    except:
        pass
    finally:
        print("channel.close()...")
        channel.close()
        print("closed.")
