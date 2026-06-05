#f = open("myfile.text", "x")
with open("myfile.text", "w") as f:
    f.write("kiss my ass good bie bie bie")

with open("myfile.text", "r") as f:
    print(f.read())
with open("myfile.text", "a") as f:
    f.write("these is hello world")

with open("myfile.text", "a") as f:
    f.write("kick ur ass")