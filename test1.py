//Q1

a = "text!@#"
a1 =a.replace("!@#","")
print(a1)

//Q2

st_rng = 2
end_rng = 20
for a in range(st_rng, end_rng + 1):
   if a > 1:
      for i in range(2, a):
         if (a % i) == 0:
            break
      else:
         print(a)
 
//Q3

txt = "information technology information networks";
    
print("Duplicate chars are: ");  
for i in range(0, len(txt)):  
    count = 1;  
    for j in range(i+1, len(txt)):  
        if(txt[i] == txt[j] and txt[i] != ' '):  
            count = count + 1;  
            txt = txt[:j] + '0' + txt[j+1:];  
    
    if(count > 1 and txt[i] != '0'):  
        print(txt[i]," - ",count);
