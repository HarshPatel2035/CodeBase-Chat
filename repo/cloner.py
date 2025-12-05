import os
from git import Repo
import shutil

def clone_git_repo(url,dirname = '/Users/harshpatel/Desktop/CodeBase Chat ( RAG + LLM )/git_clone'):
    try :
        shutil.rmtree(dirname)
        print("Copying repositery and storing it into git_clone folder....")
        Repo.clone_from(url,dirname)
        print('Git Repositery Suceessfully Cloned and Saved in git_clone folder')

    except Exception as e:
        print(f"Got error in cloning the repositery -- {e}")
