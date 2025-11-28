with open("./txt/sample.txt","a") as f:
    for i in range(1,21):
        f.write(f"\nSquare of {i} is {i*i}")
