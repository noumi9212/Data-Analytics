import matplotlib.pyplot as plt
fb_views = [534,489,358,401,424,689,445,523,442,700,404,505,550,654]
yt_views = [200,609,458,201,524,389,245,323,242,200,504,605,650,354]

days = range(1,15,1)

plt.bar([a-0.25 for a in days] , 
        fb_views, 
        width=0.25,
         label = 'Facebook Views',
         align='edge'
         )
plt.bar([a+0.25 for a in days],
         yt_views,
         width=-0.25,
         label = 'Youtube Views',
         align='edge'
         )

plt.xlabel('Day')
plt.ylabel('Views')
plt.xticks(days)
plt.grid(True,
         color='r',
         linestyle='-.'
         )
plt.title('Daily views for marketing channel')
plt.legend(loc = 'upper left')

plt.show()