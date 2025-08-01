import os

def create_project_structure(project_name):
    base_path = os.path.abspath(project_name)
    os.makedirs(base_path, exist_ok=True)

    # Top-level files
    with open(os.path.join(base_path, "documentparser.py"), "w") as f:
        f.write("# documentparser.py\n")

    with open(os.path.join(base_path, "main.py"), "w") as f:
        f.write("# main.py\n")

    # prompts/
    prompts_path = os.path.join(base_path, "prompts")
    os.makedirs(prompts_path, exist_ok=True)
    with open(os.path.join(prompts_path, "prompts.py"), "w") as f:
        f.write("# prompts.py\n")

    # vectorstore/
    vectorstore_path = os.path.join(base_path, "vectorstore")
    os.makedirs(vectorstore_path, exist_ok=True)
    with open(os.path.join(vectorstore_path, "vectorstore.py"), "w") as f:
        f.write("# vectorstore.py\n")

    # llmops/
    llmops_path = os.path.join(base_path, "llmops")
    os.makedirs(llmops_path, exist_ok=True)
    with open(os.path.join(llmops_path, "llms.py"), "w") as f:
        f.write("# llms.py\n")

    # knowledge_base/
    kb_path = os.path.join(base_path, "knowledge_base")
    os.makedirs(kb_path, exist_ok=True)

    for sub in ["pdf", "csv", "excel"]:
        sub_path = os.path.join(kb_path, sub)
        os.makedirs(sub_path, exist_ok=True)

        if sub == "pdf":
            with open(os.path.join(sub_path, "sample.pdf"), "wb") as f:
                f.write(b"%PDF-1.4\n%Dummy PDF\n")
        elif sub == "csv":
            with open(os.path.join(sub_path, "sample.csv"), "w") as f:
                f.write("id,name\n1,Example\n")
        elif sub == "excel":
            try:
                from openpyxl import Workbook
                wb = Workbook()
                ws = wb.active
                ws.append(["id", "name"])
                ws.append([1, "Example"])
                wb.save(os.path.join(sub_path, "sample.xlsx"))
            except ImportError:
                with open(os.path.join(sub_path, "sample.xlsx"), "w") as f:
                    f.write("Install openpyxl to generate Excel file\n")

    print(f"✅ Project '{project_name}' created successfully!")
