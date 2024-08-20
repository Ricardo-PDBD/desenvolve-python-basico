s = int (input("Digite quantos sapos foram utilizados em 1 ano: "))
r = int (input("Digite quantos ratos foram utilizados em 1 ano: "))
c = int (input("Digite quantos coelhos foram utilizados em 1 ano: "))

total = s + r + c
perc_s = (100 / total) * s
perc_r = (100 / total) * r
perc_c = (100 / total) * c

print(f"Total: {total} cobaias.")
print(f"Tatal de sapos: {s} sapos.")
print(f"Total de ratos: {r} ratos.")
print(f"Total de coelhos: {c} coelhos.")
print(f"Percentaul de sapos: {float(perc_s):.2f}%.")
print(f"Percentual de ratos: {float(perc_r):.2f}%.")
print(f"Percentual de coelho: {float(perc_c):.2f}%.")