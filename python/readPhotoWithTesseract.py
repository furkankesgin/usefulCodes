import os 
  
# Function to rename multiple files 
def main(): 
    path = "/Users/furkan/Desktop/final/all"
    for count, filename in enumerate(os.listdir(path)): 
        dst ="pdf" + str(count) + ".jpg"
        src =os.path.join(path,filename)
        dst =os.path.join(path,dst) 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
    stream1 = os.popen('for f in '+str(path)+'/*jpg; do tesseract -l tur "$f" "$(basename)"$f;done')
    output1 = stream1.read()
    print(output1)
    stream2 = os.popen('for f in '+str(path)+'/*txt; do cat "$f" "$(basename)"$f >> "'+str(path)+'/tetete.txt";done')
    output2 = stream2.read()
    print(output2)
    stream3 = os.popen('')
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 

