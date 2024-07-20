import matplotlib.pyplot as plt
fb_views = [534,689,258,401,724,689,4045]
tw_views = [123,342,700,304,405,650,6543]
yt_views = [202,209,176,415,824,389,3987]
days = range(1,8)
plt.plot(days, yt_views, 
         label = 'Youtube Views',
         marker='o',
         markerfacecolor='b'
         )
plt.plot(days, fb_views, 
         label = 'Facebook Views',
         marker='o',
         markerfacecolor='orange'
         )
plt.plot(days, tw_views, 
         label = 'Twitter Views',
         marker='o',
         markerfacecolor='g'
         )
plt.xlabel('Day')
plt.ylabel('Views')
plt.grid(True,
         color='r',
         linestyle='-.'
         )
plt.title('Daily views for marketing channel')
plt.legend(loc = 'upper left')
plt.xlim(1,5)
plt.ylim(100,900)
plt.show()