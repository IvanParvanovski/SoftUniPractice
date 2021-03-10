from project.system import System


def zero_test():
    sys = System()
    sys.register_power_hardware("HDD", 200, 200)
    sys.register_heavy_hardware("SSD", 400, 400)
    print(sys.analyze())
    sys.register_light_software("HDD", "Test", 0, 10)

    print(sys.register_express_software("HDD", "Test2", 100, 100))

    # sys.register_express_software("HDD", "Test3", 50, 100)
    # sys.register_light_software("SSD", "Windows", 20, 50)
    # sys.register_express_software("SSD", "Linux", 50, 100)
    # sys.register_light_software("SSD", "Unix", 20, 50)

    print(sys.analyze())
    sys.release_software_component("SSD", "Linux")
    print(sys.system_split())


if __name__ == "__main__":
    zero_test()
