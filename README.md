<center> 
  [![Typing SVG](https://readme-typing-svg.demolab.com/?lines=MergeJSON)](https://git.io/typing-svg) 
</center>

This is a small program that allows you to merge two backup JSON files for Instander/MyInsta applications (https://t.me/instasmash) created by blupapilte.

This mini-program simply uses the JSON python library to merge the 2 desired files. For the moment the program merges the two files by taking the parameters contained in these two files and merges them, as for the parameters which appear in the two files, it keeps the value "True" of this parameter for the final version (the merged final file).
This means that if the program puts for example "34567": [0: :false] in first file and in the other it reads "34567": [0: :true] in the final merge file it will keep the setting "34567": [0: :true] .

It also uses the TK library of python in order to have a pleasant and efficient graphical interface.


This program is in beta at the moment and is subject to change from time to time.

Photo about this mini-programe : 

![image](https://github.com/Zeldrox-dev/MergerJSON/assets/123584533/b5655acc-8f80-469e-b1e8-c728f068b117)
