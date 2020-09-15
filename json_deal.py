import json
import sys


def deal_dict(config_list, json_src, file_ptr, parent=""):
    for i in json_src:
        print("in dict:\n" + i + str(json_src[i]))
        this_config = parent + i
        duplicate_flag = 0
        for it_config in config_list:
            if it_config == this_config:
                duplicate_flag = 1
                break
        if duplicate_flag == 0:
            if type(json_src[i]) == list:
                formal_type = "array"
            elif type(json_src[i]) == str:
                formal_type = "string"
            elif type(json_src[i]) == int:
                formal_type = "int"
            elif type(json_src[i]) == bool:
                formal_type = "bool"
            else:
                print("unexpected type: " + str(type(json_src[i])))
                formal_type = str(type(json_src[i])).split(' ')[1].strip('>').strip("'")
            file_ptr.write("|" + this_config + "| |" + formal_type + "||\n")
            config_list.append(this_config)
        if type(json_src[i]) == list:
            deal_list(config_list, json_src[i], file_ptr, parent + i + "::")
        if type(json_src[i]) == dict:
            deal_dict(config_list, json_src[i], file_ptr, parent + i + "::")


def deal_list(config_list, json_src, file_ptr, parent=""):
    if type(json_src[0]) == list:
        for i in json_src:
            deal_list(config_list, i, file_ptr, parent)
    if type(json_src[0]) == dict:
        for i in json_src:
            print("in list to dict:\n" + str(i))
            deal_dict(config_list, i, file_ptr, parent)


def deal_json(json_src, file_ptr):
    config_list = []
    if type(json_src) == dict:
        deal_dict(config_list, json_src, file_ptr)
    if type(json_src) == list:
        deal_list(config_list, json_src, file_ptr)


def trans_json(file_path="./json_src.txt"):
    rfile = open(file_path, "r", encoding='utf-8')
    json_src = ""
    for line in rfile:
        line = line.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")
        json_src += line
    print(json_src)
    dict_json = json.loads(json_src)
    wfile = open("./form_dst.txt", "a")
    deal_json(dict_json, wfile)


if __name__ == "__main__":
    arg_list = sys.argv[1:]
    trans_json(*arg_list)