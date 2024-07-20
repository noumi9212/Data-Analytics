import matplotlib.pyplot as plt
fb_views = [534,489,358,401,724,689,445,523,442,700,404,505,550,654]
yt_views = [200,689,458,201,524,389,245,323,242,200,504,605,650,354]

days = range(1,15)

plt.scatter(days, fb_views, 
         label = 'Facebook Views'
         )
plt.scatter(days, yt_views,
         label = 'Youtube Views'
         )

plt.xlabel('Day')
plt.ylabel('Views')
plt.grid(True,
         color='r',
         linestyle='-.'
         )
plt.title('Daily views for marketing channel')
plt.legend(loc = 'upper left')

plt.show()