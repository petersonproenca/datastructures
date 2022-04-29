class Stack {
  
  constructor(c) {
    this.capacidade = c
    this.stack = new Array(this.capacidade) 
    //inicalizando um vetor vazio
    this.inicio = 0  
    this.fim = 0    
    return this.stack;
  }
  
  insert (x) {
    if (this.fim == this.capacidade) {
      return "Stack Overflow";
    }
    else {
      this.fim += 1
      this.stack.push(x)
      return this.stack;
    }
  }
  
  delete () {
    if (this.fim == 0) {
      return "Empty Stack";
    }
    else {
      let a = this.stack[this.fim];
      this.fim -= 1
      this.stack.pop()
      return a;
    }
  }
  
  
  len(){
   return this.fim;
  }
  
  /*print(){
    let i;
    for (i of this.stack) {
      document.write(i);
    }
  }*/
  
}
