from RTG import RandomTextGenerator

rtg = RandomTextGenerator()
filename = "./data/CNN_title_data.txt"
rtg.train(filename)
my_texts = rtg.generate_multiple(5)

for t in my_texts:
    print(t)
