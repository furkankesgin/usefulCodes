import os

project_path = r"C:\Users\furkan\Documents\JAVA\ch-doc-will-check-Copy"
controller_abstracts_path=os.path.join("Controller","abstracts")
controller_concreates_path=os.path.join("Controller","concreates")
entity_path = "Entity"
services_abstracts_path = os.path.join("Service","abstracts")
services_concreates_path = os.path.join("Service","concreates")
repository_path = os.path.join("Repository","abstracts")


paths=[controller_abstracts_path,
       controller_concreates_path,
       entity_path,
       services_abstracts_path,
       services_concreates_path,
       repository_path
       ]
def create_spring_template_folder(project_path):
    
    starting_path=""
    for root, subdirs, files in os.walk(os.path.join(project_path,"src","main", "java")):
        print(root)
        print(subdirs)
        print(files)
        starting_path = root
        print("---------")

    print(starting_path)
    for i in paths:
        path = os.path.join(starting_path,i)
        if not os.path.exists(path):
            os.makedirs(path)
    print("Tamamlandi")
create_spring_template_folder(project_path)

