import hashlib


def hex_to_bits(hex):
    return bin(int(hex, 16))[2:].zfill(128)


def simhash(text: str) -> str:
    sh = [0] * 128
    words = text.strip().split(" ")

    for word in words:
        word_hash = hashlib.md5(str.encode(word)).hexdigest()

        for i, bit in enumerate(hex_to_bits(word_hash)):
            if int(bit) == 1:
                sh[i] += 1
            else:
                sh[i] -= 1

    sh_2 = []
    for bit in sh:
        if bit >= 0:
            sh_2.append(1)
        else:
            sh_2.append(0)

    return hex(int(''.join(map(str, sh_2)), 2))[2:]


def calculate_diference(hash1, hash2):
    result = int(hash1, 16) ^ int(hash2, 16)
    return bin(result)[2:].count("1")


def parse_query(sim_hashes: [str], query: str):
    nums = query.split(" ")

    i = int(nums[0])
    k = int(nums[1])

    result = 0
    query_hash = sim_hashes[i]

    for counter, hash in enumerate(sim_hashes):
        if hash != query_hash:
            if calculate_diference(query_hash, hash) <= k:
                result += 1

    return result


def main():
    n = int(input())

    sim_hashes = []

    for i in range(n):
        sim_hashes.append(simhash(input()))

    q = int(input())

    for i in range(q):
        query = input()
        result = parse_query(sim_hashes, query)
        print(result)


if __name__ == '__main__':
    main()
