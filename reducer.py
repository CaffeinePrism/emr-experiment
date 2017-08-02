#!/home/hadoop/anaconda/bin/python
import imageio
import sys
with imageio.get_writer('output.gif', mode='I') as writer:
    filenames = read_input(sys.stdin)
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
