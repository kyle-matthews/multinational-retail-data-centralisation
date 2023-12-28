# Multinational Retail Data Centralisation 
<div align='center'> 

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![Postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)  ![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white) ![VSCode](	https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)</div>

---
### Contents

1. Introduction
2. Installation Instructions
3. Usage Instructions
4. File Structure
5. License Information
6. Lessons Learned

---

### 1. Introduction
By trade I am currently a Primary School Teacher in the UK, but I am massively keen on reskilling and retraining to become a cloud/data engineer of some sort. The task is rather daunting with two young kittens and an extortionate mortgage to pay off, but here we are. I will begin with the words that I often use to sell outrageous or unbelievable ideas to my class with, 'lets say...'

*Lets say,* that I am employed by a multinational corporation that sells various goods across the globe. You want it, they've got it. Much like PepsiCo or Nestle, they have their fingers in a lot of pies.

Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

In an effort to become more data-driven, the organisation would like to make its sales data accessible from one centralised location.

My first aime is to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data.

I will then query the database to get up-to-date metrics for the business.

---

### 2. Installation Instructions

This program will run straight from your command line so the directory containing all of the files needs to be saved somewhere where you can find it. 

**(Warning: If you remove/move any Python files, it will most likely result in the program no longer working.)**

---

### 3. Usage Instructions

The program runs directly from the command line. 
- cd into the directory that the folder is saved into and open `main.py`.
- From there everything should be handled automatically. 
- The data will be taken from the remote AWS RDS server and added directly to your own SQL server. 

---

### 4. File Structure

The file structure is contained within one folder. `main.py` is the file that pulls classes and their methods from `data_cleaning.py`, `database_utils.py` and `data_extractor.py` in order to get work done. It works out of the box as all of the dependencies are within the same folder. If you start messing with that then you will suddenly find that things will stop working! 

---

### 5. License Information

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

---

### 6. Lessons Learned
