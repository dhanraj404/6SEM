

object forloop {
     def main(args: Array[String]) {
      var counter: Int=0;
      
      for(counter <- 1 to 100)
        print(counter + " ");
    
      // to print new line
      println();
   }
}