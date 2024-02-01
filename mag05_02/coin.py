import matplotlib.pyplot as plt
import numpy as np

num_throws = 100_000
result = []

for _ in range(num_throws):
    # 0 - heads, 1 - tails
    flip = np.random.randint(0, 2)
    result.append(flip)

print(result)
probabilities = np.cumsum(result) / np.arange(1, num_throws + 1)
print(probabilities[-1])

plt.figure(figsize=(10, 6))
plt.plot(probabilities)
plt.xlabel('Throws')
plt.ylabel('Probability')
plt.title('Coin Flip')
plt.xlim(0, num_throws)
plt.ylim(0, 1)
plt.grid(True)
plt.show()
