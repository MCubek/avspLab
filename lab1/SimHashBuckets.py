import hashlib

k = 128
b = 8
r = k / b

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

def parse_query(candidates, query, hashes):
    nums = query.split(" ")

    i = int(nums[0])
    k = int(nums[1])

    result = 0

    for candidate_id in candidates[i]:
        candidates_hash = hashes[candidate_id]

        if calculate_diference(hashes[i], candidates_hash) <= k:
            result += 1

    return result

def hash2int(belt, hash):
    start = belt * 16
    end = start + 16

    binary = hex_to_bits(hash)[start:end]

    return int(binary, 2)


def create_candidates_lsh(sim_hashes):
    candidates = {}
    for belt in range(b):
        slots = {}
        for curr_id, curr_hash in enumerate(sim_hashes):
            value = hash2int(belt, curr_hash)

            if value in slots:
                in_slot = slots[value]
                for text_id in in_slot:
                    if curr_id not in candidates:
                        candidates[curr_id] = set()
                    if text_id not in candidates:
                        candidates[text_id] = set()

                    candidates[curr_id].add(text_id)
                    candidates[text_id].add(curr_id)
            else:
                in_slot = []

            in_slot.append(curr_id)
            slots[value] = in_slot

    return candidates


def main():
    n = int(input())

    sim_hashes = []

    for i in range(n):
        sim_hashes.append(simhash(input()))

    candidates = create_candidates_lsh(sim_hashes)

    q = int(input())

    for i in range(q):
        query = input()
        result = parse_query(candidates, query, sim_hashes)
        print(result)


if __name__ == '__main__':
    main()
