import matplotlib.pyplot as plt
fb_views = [534,489,358,401,424,689,445,523,442,700,404,505,550,654]
yt_views = [200,609,458,201,524,389,245,323,242,200,504,605,650,354]

days = range(1,15)
bin = [100,200,300,400,500,600,700,800,900,1000]

plt.hist(fb_views, bin, label='Facebook Views')

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