for quant in range(5,0,-1):
    if(quant > 1):
        print(quant," Bottles of beer on the wall", quant," Bottles of beer")
        if(quant>2):
              suffix=str(quant)+ ";) bottles of beer on the wall"
        else:
              suffix="1 bottle of beer on the wall"
    elif quant == 1:
        print("1 bottle beer on the wall--, 1 bottle of beer--")
        suffix="No more beer on the wall"

    print("Take one down and pass it around", suffix)
    print("----")
              
              
  
