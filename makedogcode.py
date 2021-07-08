import os

dogs = ["max", "rocky", "other"]
for dog in dogs:  # takes ya back to the days when you first learned for loops
    print(dog)
    for filename in os.listdir(f"{dog}/"):
        print(f"<li><img src=/{dog}/{filename}></li>")

    print()