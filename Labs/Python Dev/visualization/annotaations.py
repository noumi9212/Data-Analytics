import matplotlib.pyplot as plt

fb_views = [534,489,358,401,424,689,445,523,442,700,404,505,550,654]
x_axis = range(1,15)
min_y = min(fb_views)
x_min_index = x_axis[fb_views.index(min_y)]
max_y = max(fb_views)
x_max_index = x_axis[fb_views.index(max_y)]


plt.plot(x_axis, fb_views,
         label='Facebook Views',
         marker='o'
         )


plt.xlabel('Day')
plt.ylabel('Views')
plt.legend(loc='upper left')
plt.grid(True,
         linewidth='1',
         linestyle='-.'
         )
plt.title('Daily views of Marketing Channel')
plt.annotate(text='Lowest Value', 
             xy=(x_min_index, min_y),
             xytext=(x_min_index+2, min_y+30),
             arrowprops=dict(facecolor='black', shrink=0.05)
             )
plt.annotate(text='Highest Value', 
             xy=(x_max_index, max_y),
             xytext=(x_max_index+2, max_y-30),
             arrowprops=dict(facecolor='black', shrink=0.05)
             )

plt.show()