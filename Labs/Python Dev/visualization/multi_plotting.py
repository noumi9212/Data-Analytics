import matplotlib.pyplot as plt
fb_views = [534,689,258,401,724,689,350]
tw_views = [123,342,700,304,405,650,325]
yt_views = [202,209,176,415,824,389,550]
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
plt.title('Daily views for marketing channel')
plt.legend(loc = 'lower right')
plt.show()