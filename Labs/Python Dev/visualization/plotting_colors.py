import matplotlib.pyplot as plt
views = [534,689,258,401,724,689,350]
days = range(1,8)

plt.plot(days, views, 
         label='Youtube Views', 
         color='r',
         marker='D',
         markerfacecolor='m',
         linestyle='-.',
         linewidth=2
         )
plt.xlabel('Day No')
plt.ylabel('Views')
plt.title('Youtube views on daily basis')
plt.legend(loc = 'lower right')
plt.show()