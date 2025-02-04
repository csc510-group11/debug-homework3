import subprocess

def random_array(arr):
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True)
        arr[i] = int(shuffled_num.stdout)
    return arr


print(random_array([2,6,1,9,0,3]))