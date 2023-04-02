import sys
year_in = int(sys.argv[1])
population = [
    144_963_650,  # 2003
    144_168_205,
    143_474_219,
    142_753_551,
    142_220_968,
    142_008_838,
    141_903_979,
    142_856_536,
    142_865_433,
    143_056_383,
    143_347_059,
    143_666_931,
    146_267_288,
    146_544_710,
    146_804_372,
    146_880_432,
    146_780_720,
    146_748_590  # 2020
]
x = 0 - 2003
y = x + year_in
years = []
for years_lit in population:
    if population[y] <= years_lit:
        years.append(population.index(years_lit) + 2003)
print(', '.join(list(map(str, years))))

