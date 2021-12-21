def collatzIter(var):

    while True:                                 #loop to calculate the collatz sequence

        if var[len(var)-1]%2 == 0:              #if even divide by 2
            var.append(var[len(var)-1]/2)
            
        if (var[len(var)-1] == 1):              #if equal to 1 break out of loop
            break
        
        if var[len(var)-1]%2 == 1:              #if odd multiply by 3 and add 1
            var.append(3*var[len(var)-1]+1)

seq_start = [25]                                #the sequence starting number - used a list because they're dynamic and mutable
collatzIter(seq_start)                          #call the function calculating the sequence
print ("The sequence is: {}".format(seq_start)) #prints the sequence and the one below prints length of the sequence
print ("The sequence length is: {}".format(len(seq_start)))