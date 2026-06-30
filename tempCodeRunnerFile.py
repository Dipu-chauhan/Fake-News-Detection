data = data.sample(frac=1).reset_index(drop=True)

print(data.head())
print(data.shape)