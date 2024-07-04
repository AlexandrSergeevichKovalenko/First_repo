from pprint import pprint

resuld_lst = list()
def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                content_line_from_file = line.strip().split(",")
                cats_keys = ["id", "name", "age"]
                cat_info_dict = dict()
                for i in range(len(content_line_from_file)):
                    cat_info_dict[cats_keys[i]] = content_line_from_file[i]
                resuld_lst.append(cat_info_dict)
        pprint(resuld_lst)
    except FileNotFoundError:
        print("The file has not been found")


get_cats_info("text.txt")



        





    
