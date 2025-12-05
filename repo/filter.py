import os
import time

allowed = ('.py', '.js','.tsv','.ts', '.go', '.rs', '.md', '.txt', '.yml','.ipynb')

def filter_files(dirname):
    count = 0
    total = 0
    t1 = time.time()
    allowed_files = []
    for root,_,files in os.walk(dirname):
        for file in files:
            total+=1
            if str(file).endswith(allowed):
                allowed_files.append(file)
                count+=1
            else:
                os.remove(os.path.join(root,file))
    t2 = time.time()
    print("--------------------------------------------------------------------------------------------------------------------")
    print(f"Total files :: {total} ")
    print(f"Time took to filtering -----   {t2-t1} Seconds")
    print(f"Total got {count} files after filtering")
    print(f"Remaining files : {allowed_files}")
    print("--------------------------------------------------------------------------------------------------------------------")

