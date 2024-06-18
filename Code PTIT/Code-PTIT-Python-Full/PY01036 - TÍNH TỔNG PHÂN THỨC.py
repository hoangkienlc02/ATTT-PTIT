def calculate(sequence):
    nums = [int(x) for x in sequence.strip()]
    even_num = sum(nums[1::2])
    odd_product = 1
    for num in nums[::2]:
        odd_product *= num
    
    if even_num == 0:
        return "INVALID"
    return "{:.6f}".format(odd_product / even_num)
if __name__ == "__main__":
    num_test = int(input())
    for _ in range(num_test):
        sequence = input()
        print(calculate(sequence))