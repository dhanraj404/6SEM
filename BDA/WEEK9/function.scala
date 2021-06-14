

object function {
      //function definition
    def getLargestNumber(x: Int, y: Int) : Int ={
        var largestNumber: Int=0;
        if(x>y)
            largestNumber=x;
        else
            largestNumber=y;
        
        return largestNumber;
    }
    
    def main(args: Array[String]) {
        var a: Int=10;
        var b: Int=20;
        
        //function calling
        println("Largest number from "+ a+" and "+ b +" is: "+ getLargestNumber(a,b));
        
    }
}