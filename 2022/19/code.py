from tqdm import tqdm


def add_items(robots, items):
    for robot, number in robots.items():
        items[robot] += number


def valid_robots(blueprint, items):
    valid_robot = []
    for robot, recipe in blueprint.items():
        valid = True
        for ingredient, quantity in recipe.items():
            if quantity > items[ingredient]:
                valid = False
        if valid:
            valid_robot.append(robot)
    return valid_robot


def build_robot(robot, blueprint, robots, items):
    for ingredient, quantity in blueprint[robot].items():
        if items[ingredient] < quantity:
            raise Exception(f'Not enough {ingredient} ({items[ingredient]}) to build {robot} robot, need {quantity}.')
        items[ingredient] -= quantity
    robots[robot] += 1


def find_max_geodes_w_exclude(minute, robots, items, blueprint, robot_exclude_list):
    # if minute == 24:
    if minute == 32:
        return items['geode']
    valid_robots_list = valid_robots(blueprint, items)
    add_items(robots, items)
    max_geode_list = []
    for valid_robot in valid_robots_list:
        if valid_robot not in robot_exclude_list:
            items_copy = items.copy()
            robots_copy = robots.copy()
            build_robot(valid_robot, blueprint, robots_copy, items_copy)
            max_geode_list.append(find_max_geodes_w_exclude(minute + 1, robots_copy, items_copy, blueprint, []))
    max_geode_list.append(find_max_geodes_w_exclude(minute + 1, robots, items, blueprint, valid_robots_list))
    return max(max_geode_list)


# def find_max_geodes(minute, robots, items, blueprint):
#     if minute == 24:
#         return items['geode']
#     valid_robots_list = valid_robots(blueprint, items)
#     add_items(robots, items)
#     max_geode_list = []
#     for valid_robot in valid_robots_list:
#         items_copy = items.copy()
#         robots_copy = robots.copy()
#         build_robot(valid_robot, blueprint, robots_copy, items_copy)
#         max_geode_list.append(find_max_geodes(minute + 1, robots_copy, items_copy, blueprint))
#     max_geode_list.append(find_max_geodes(minute + 1, robots.copy(), items.copy(), blueprint))
#     return max(max_geode_list)


blueprints = []
with open('input.txt') as f:
    for li in f.readlines():
        curr_robots = {}
        robots_str = li.removesuffix('\n').split(':')[-1]
        for robot_str in robots_str.split('.'):
            if robot_str != '':
                robot_str_split = robot_str.split(' robot ')
                robot_recipe = {}
                for ingredient_str in robot_str_split[1].removeprefix('costs ').split(' and '):
                    robot_recipe[ingredient_str.split(' ')[-1]] = int(ingredient_str.split(' ')[0])
                curr_robots[robot_str_split[0].split(' ')[-1]] = robot_recipe
        blueprints.append(curr_robots)

# s = 0
# for i, blueprint in tqdm(enumerate(blueprints), total=len(blueprints)):
#     item_inventory = {
#         'ore': 0,
#         'clay': 0,
#         'obsidian': 0,
#         'geode': 0
#     }
#     robot_inventory = {
#         'ore': 1,
#         'clay': 0,
#         'obsidian': 0,
#         'geode': 0
#     }
#
#     s += (i + 1) * find_max_geodes_w_exclude(0, robot_inventory, item_inventory, blueprint, [])

s = 1
for i, blueprint in tqdm(enumerate(blueprints[:3]), total=3):
    item_inventory = {
        'ore': 0,
        'clay': 0,
        'obsidian': 0,
        'geode': 0
    }
    robot_inventory = {
        'ore': 1,
        'clay': 0,
        'obsidian': 0,
        'geode': 0
    }

    s *= find_max_geodes_w_exclude(0, robot_inventory, item_inventory, blueprint, [])
