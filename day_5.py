if __name__ == '__main__':
    def part_1():
        def create_dic(line: str, dic: dict):
            if [ord(c) for c in line] == [10]:
                dic["toggle"] = False
                return

            destination, source, r = [int(val) for val in line.split()]
            dic['values_map'].append({'source': source, 'destination': destination, 'range': r})

        file_path = 'input.txt'
        lines = []
        seeds = []

        categories = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light',
                      'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

        string_to_map = {}
        for category in categories:
            string_to_map[category] = {'toggle': False, 'values_map': []}

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if 'seeds' in line:
                        s, seeds = line.split(':')
                        seeds = [int(c) for c in seeds.strip().split(' ')]

                    for key, val in string_to_map.items():
                        if key in line:
                            val['toggle'] = True
                            break

                        if val['toggle']:
                            create_dic(line, val)

        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")

        locations = []
        for seed in seeds:
            seed_location = seed
            for string_to_map_dic in string_to_map.values():
                mapped_values = string_to_map_dic['values_map']

                for interval_dic in mapped_values:
                    source = interval_dic['source']
                    range_val = interval_dic['range']
                    if source <= seed_location <= (source + range_val - 1):
                        destination = interval_dic['destination']

                        seed_location = seed_location - source + destination
                        break

            locations.append(seed_location)
        print(min(locations))
    #part_1()

    def part_2():
        def create_dic(line: str, dic: dict):
            if [ord(c) for c in line] == [10]:
                dic["toggle"] = False
                return

            destination, source, r = [int(val) for val in line.split()]
            dic['values_map'].append({'source': source, 'destination': destination, 'range': r})

        file_path = 'input.txt'

        seeds = []
        category_labels = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light',
                      'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
        categories = {}
        for category in category_labels:
            categories[category] = {'toggle': False, 'values_map': []}

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if 'seeds' in line:
                        s, seeds_str = line.split(':')
                        seeds_list = [int(val) for val in seeds_str.strip().split(' ')]
                        for i in range(0, len(seeds_list), 2):
                            seeds.append((seeds_list[i], seeds_list[i] + seeds_list[i + 1] - 1))

                    for key, val in categories.items():
                        if key in line:
                            val['toggle'] = True
                            break

                        if val['toggle']:
                            create_dic(line, val)

        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")

        categories_list = []
        for label in categories:
            category = []
            for val in categories[label]['values_map']:
                category.append((val['destination'], val['source'], val['range']))
            categories_list.append(category)

        for category in categories_list:
            sources = []

            while seeds:
                seed = seeds.pop()

                for destination, source, r in category:
                    seed_start, seed_end = seed
                    end = source + r - 1

                    intersection_start = max(seed_start, source)
                    intersection_end = min(seed_end, end)

                    if intersection_start < intersection_end:
                        destination_start = destination + intersection_start - source
                        destination_end = destination + intersection_end - source
                        sources.append((destination_start, destination_end))
                        if seed_start < intersection_start:
                            seeds.append((seed_start, intersection_start))
                        if seed_end > intersection_end:
                            seeds.append((intersection_end, seed_end))
                        break
                else:
                    sources.append(seed)
            seeds = sources
        print(min(seeds)[0])
    part_2()









