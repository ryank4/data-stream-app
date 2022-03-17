import time

import grpc

import data_stream_pb2
import data_stream_pb2_grpc

import redis

SERVER_ADDRESS = "data_stream:50051"
CLIENT_ID = 1


age_groups = ['Under 20', '20-30', '30-40', '40-50', '50-60', '60+']
age_group_violations = {a: 0 for a in age_groups}

conn = redis.StrictRedis(host='redis', port=6379)

times = []


def calc_age_group_violations(age):
    if age < 20:
        age_group_violations['Under 20'] += 1
    if 20 <= age < 30:
        age_group_violations['20-30'] += 1
    if 30 <= age < 40:
        age_group_violations['30-40'] += 1
    if 40 <= age < 50:
        age_group_violations['40-50'] += 1
    if 50 <= age < 60:
        age_group_violations['50-60'] += 1
    if age >= 60:
        age_group_violations['60+'] += 1


def get_violations_in_last_minute():
    violations_in_last_minute = 0
    current_time = int(time.time())

    for t in times:
        if (current_time - t) < 60:
            violations_in_last_minute += 1

    return violations_in_last_minute


def server_streaming_method(stub):
    print("--------------Call ServerStreamingMethod Begin--------------")
    request = data_stream_pb2.Data(client_id=CLIENT_ID)
    response_iterator = stub.DataStreamingService(request)
    drugs = 0
    arrests = 0
    for response in response_iterator:
        params_list = response.response_data.split(",")
        if len(params_list) != 0:
            age = params_list[5]
            if age.isdigit():
                calc_age_group_violations(int(age))

            drugs_related = params_list[14]
            if drugs_related == "TRUE":
                drugs += 1

            is_arrested = params_list[12]
            if is_arrested == "TRUE":
                arrests += 1

            t = response.timestamp
            times.append(t.seconds)
            num_violations_last_minute = get_violations_in_last_minute()

        try:
            conn.set("ArrestsMade", arrests)
            conn.set("DrugsRelated", drugs)
            conn.set("ViolationsLastMinute", num_violations_last_minute)
            most_violations = max(age_group_violations, key=age_group_violations.get)
            conn.set("AgeGroupMostViolations", most_violations)
        except Exception as ex:
            print('Error:', ex)

    print("--------------Call ServerStreamingMethod Over---------------")


def main():
    channel = grpc.insecure_channel(SERVER_ADDRESS)
    stub = data_stream_pb2_grpc.DataStreamStub(channel)
    server_streaming_method(stub)


if __name__ == '__main__':
    main()
