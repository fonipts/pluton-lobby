import sys
import os
import re
app_setting_var = {
    "default": {
        "import":[".health"],
        "value":[],
        "append":[]
    },
    "graphbox": {
        "import":[],
        "value":["graphene_django","graph_schema.myapp","graph_schema.myproject"],
        "append":[]
    },
    "drf": {
        "import":[],
        "value":[".apphealth"],
        "append":[]
    }

}

def main():
    
    types = sys.argv[1]
    package_name = sys.argv[2]
    arguments = sys.argv[3]
    directory = os.getcwd()

    if types == "setting_app":
        file_loc = os.path.join(
                directory, package_name,package_name, "settings.py"
            )
        app_import = app_setting_var[arguments]["import"]
        app_value = app_setting_var[arguments]["value"]
        app_append = app_setting_var[arguments]["append"]
        with open(file_loc,"r") as read_file:
            content  =read_file.read()
            results = re.findall(r"(INSTALLED_APPS[\s\n]{0,}\=[\s\n]{0,}\[\n[\n\s\'\"\w\.\,]{0,}\])",content)
            if len(results) >0:
                get_replace_install = results[0]

                content_replace  = get_replace_install.replace("\n]","\n"+",\n".join([ '    "'+x+'"' for x in app_value])+"\n]")
                content  = content.replace(get_replace_install,content_replace)
                content =content+"\n".join([x for x in app_append])+"\n"
                write_file(file_loc,content)

def write_file(file,content):
    with open(file, "w", encoding="utf-8") as f_write:
        f_write.write(content)
        f_write.close()
if __name__ == "__main__":
    main()
