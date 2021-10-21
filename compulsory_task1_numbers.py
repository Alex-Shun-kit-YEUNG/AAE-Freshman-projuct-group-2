def show_cost(type,part1,part2,part3,final):
    print (f'PolyU-{type} cost part1->  {part1}')
    print (f'PolyU-{type} cost part2->  {part2}')
    print (f'PolyU-{type} cost part3->  {part3}')
    print (f'Find goal with cost of ->  {final}')
    print ()

show_cost('A380','1.2','10.4','10','3028.7323512413177')
show_cost('A381','1.8','16.200000000000003','10','3823.7178777134127')
show_cost('A382','2.4','22.0','10','4617.520561473031')
show_cost('A383','3.0','25.5','10','5405.409031670279')

type_list = ['A380', 'A381', 'A382', 'A383']
cost_list = [3028.7323512413177, 3823.7178777134127, 4617.520561473031, 5405.409031670279]

min_cost = min (cost_list)
min_index = cost_list.index(min_cost)

print ('by comparing the final cost of the aircraft types')
print ('the aircraft type with the lowest cost:',type_list[min_index])