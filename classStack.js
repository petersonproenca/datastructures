class Stack {
  
  constructor(c) {
    globalThis.capacidade = c
    globalThis.stack = new Array(self.capacidade) 
    //inicalizando um vetor vazio
    globalThis.inicio = 0  
    globalThis.fim = 0    
    return globalThis.stack;
  }
  
   insert (x) {
    if (globalThis.fim == globalThis.capacidade) {
      return "Stack Overflow";
    }
    else {
      globalThis.fim += 1
      globalThis.stack.push(x)
      return globalThis.stack;
    }
  }

   delete () {
    if (globalThis.fim == 0) {
      return "Empty Stack";
    }
    else {
      let a = globalThis.stack[globalThis.fim];
      globalThis.fim -= 1
      globalThis.stack.pop()
      return globalThis.stack , a;
    }
  }


   len(){
   return globalThis.fim;
  }
  
   /*print(){
    let i;
    for (i of globalThis.stack) {
      document.write(i);
    }
  }*/
  
}
