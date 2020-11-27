
import os
from pathlib import Path
import file_formats1
import sort_by_time1
import organize_files1

paath = str(input("enter directory to organize example for E drive document folder enter as E:/document"))
sort_by_time1.sort_by_time1(paath)
formatas_type = file_formats1.get_file_formats1()
organize_files1.organize_files1(paath,formatas_type)
  
