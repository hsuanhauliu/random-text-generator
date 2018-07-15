from RTG import RandomTextGenerator

rtg = RandomTextGenerator()
filename = "./data/CNN_title_data.txt"
rtg.train(filename)
rtg.generate_multiple()
