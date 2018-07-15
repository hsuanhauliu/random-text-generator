from NTG import NewsTitleGenerator

ntg = NewsTitleGenerator()
filename = "./data/CNN_title_data.txt"
ntg.train(filename)
ntg.generate_multiple()
