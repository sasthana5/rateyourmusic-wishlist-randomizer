# RateYourMusic Wishlist Randomizer
**Steps:**
1. Extract *main.py* and the rest of the files to their own folder
2. Go to your [RateYourMusic](https://www.rateyourmusic.com) profile page
3. Scroll to the bottom and click **Export your data**
4. Save the generated file to the same directory as *main.py*, (make sure the exported file's name is *user_albums_export.csv*, you may have to add the *.csv* to the end of the file)
5. Run *main.py*. A random album will be picked and printed in the command line. All the albums + artists will be outputted together to *output.txt*. 
This **ONLY** will output and randomly select from albums on your wishlist. To see others, replace the "w" in line 10 of *main.py* with one of the following letters:
>w = wishlist
>
>o = owned
>
>n = rated

(these may not be all of the letters RYM uses, and I'm mostly guessing as to which corresponds to which. W and O are accurate, N is most likely accurate)

Example:
    `if row[8] == "o":`

If you want all 3 combined you can put *or* between them

Example:
    `if row[8] == "w" or "o" or "n":`
You could also remove that if statement and the indent.
