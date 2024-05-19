import math
inp = input()
inp = inp.split(" ")
so_tao = int(inp[0])
so_hoc_sinh = int(inp[1])
so_tao_duoc_chia = so_tao // so_hoc_sinh
so_tao_du = so_tao % so_hoc_sinh
print(f"{so_tao_duoc_chia} {so_tao_du}")
