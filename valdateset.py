import os
import shutil
 
 
def main():
    path = r"D:\mygit\examples\imagenet\tiny-imagenet-200\val\images"
    newPath = r"D:\mygit\examples\imagenet\tiny-imagenet-200\val\%s"
    f1 = open(r'D:\mygit\examples\imagenet\tiny-imagenet-200\val\val_annotations.txt','r')
    rec={}
    for (root, dirs, files) in os.walk(path):
        for filename in files:
            a=f1.readline().split()
            if rec.setdefault(a[1])==None:
                rec[a[1]]=0
            else:
                rec[a[1]]=rec[a[1]]+1
            
            singleFile = os.path.join(root, filename)
            newFileDirs = newPath % (a[1]);
            if not os.path.exists(newFileDirs):
                os.mkdir(newFileDirs)
            p=newFileDirs+'\\image'
            if not os.path.exists(p):
                os.mkdir(p)
            shutil.copy(singleFile, p + "\\" + a[1]+'_'+str(rec[a[1]])+'.JPEG')
            f2=open('D:\\mygit\\examples\\imagenet\\tiny-imagenet-200\\val\\'+a[1]+'\\'+a[1]+'.txt','a+')
            num=a[1]
            a.pop(0)
            name=[num,'_',str(rec[num]),'.Jpeg']
            a[0]=''.join(name)
            a.append('\n')
            f2.write('\t'.join(a))
            f2.close()
    pass
 
 
if __name__ == '__main__':
    main()
