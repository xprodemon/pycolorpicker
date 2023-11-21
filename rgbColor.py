import matplotlib.pyplot as plt

def plot_rgb_color(r, g, b, plot_size=1):
    color = [r / 255.0, g / 255.0, b / 255.0] 
   
    # Set the figure size based on the plot size
    fig, ax = plt.subplots(figsize=(plot_size, plot_size))
   
    ax.imshow([[color]])
    ax.axis('off')
    plt.show()

def explore_rgb_colors(plot_size=0.5):
    for r in range(0, 256, 32):
        for g in range(0, 256, 32):
            for b in range(0, 256, 32):
                plot_rgb_color(r, g, b, plot_size)
                print('#',r,g,b)

if __name__ == "__main__":
    explore_rgb_colors(plot_size=0.5)
