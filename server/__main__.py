#!/usr/bin/env python3

from concurrent import futures

import grpc

import job_api_pb2
import job_api_pb2_grpc

class JobAPIServicer(job_api_pb2_grpc.JobAPIServicer):
    def TrainJob(self, request, context):
        context.abort(grpc.StatusCode.NOT_FOUND, "not found")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
job_api_pb2_grpc.add_JobAPIServicer_to_server(JobAPIServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
