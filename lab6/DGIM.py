import math


class Bucket:
    def __init__(self, timestamp, size=1):
        self.size = size
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.size}, {self.timestamp}"


def query(query_size, context):
    limit = context.current_timestamp - query_size

    last_size = 0
    total = 0

    for bucket in context.buckets.__reversed__():
        if bucket.timestamp <= limit:
            break

        total += bucket.size
        last_size = bucket.size

    print(total - int(math.ceil(last_size / 2)))


def remove_old_buckets(limit, buckets, bucket_counts):
    to_remove = []
    for bucket in buckets:
        if bucket.timestamp <= limit:
            to_remove.append(bucket)

    for bucket in to_remove:
        buckets.remove(bucket)
        bucket_counts[bucket.size] -= 1


def fix_buckets_count(buckets, bucket_counts):
    while 3 in bucket_counts.values():
        for i, bucket in enumerate(buckets):
            bucket_size = bucket.size

            if bucket_counts[bucket_size] != 3:
                continue

            second_overflow_bucket = buckets[i + 1]

            new_size = bucket_size * 2

            new_bucket = Bucket(second_overflow_bucket.timestamp, size=new_size)

            buckets.remove(second_overflow_bucket)
            buckets[i] = new_bucket

            if new_size not in bucket_counts:
                bucket_counts[new_size] = 0

            bucket_counts[new_size] += 1
            bucket_counts[bucket_size] -= 2

            break


def add_bucket(bucket, buckets, bucket_counts):
    buckets.append(bucket)
    size = bucket.size
    if size not in bucket_counts:
        bucket_counts[size] = 0
    bucket_counts[size] += 1


def add_bits(line, n, context):
    for bit in line:
        context.current_timestamp += 1
        if bit == "1":
            bucket = Bucket(context.current_timestamp)
            add_bucket(bucket, context.buckets, context.bucket_counts)
            fix_buckets_count(context.buckets, context.bucket_counts)
            remove_old_buckets(context.current_timestamp - n, context.buckets, context.bucket_counts)


class Context:
    def __init__(self):
        self.current_timestamp = 0
        self.buckets = []
        self.bucket_counts = {}


def main():
    n = int(input())

    context = Context()

    line = input()
    while len(line.strip()) > 0:

        if line.startswith("q"):
            query(int(line.replace("q ", "")), context)
        else:
            add_bits(line.strip(), n, context)

        try:
            line = input()
        except EOFError:
            break


if __name__ == '__main__':
    main()
