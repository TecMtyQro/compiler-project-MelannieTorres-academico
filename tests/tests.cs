// test 1 A small program with variable definition.
static void Main { int i = 1; i = 2;}

// test 2 A small program with constant definition.
static void Main { const int a = 2;}

// test 3 A small program with the loop and conditional instruction.
static void Main { if(1>2){if(3<1){return 1;}} while (1 == 1){while (1 == 1){return false;}}}

//test 4 A small program with the input and output instruction.
static void Main {  Console.Read(); Console.Write("this string"); Console.Write(a);}

//test 5 A program with all the instructions you have defined.
static void Main { int i = 1; i = 2; const int a = 2; if(1>2){if(3<1){return -1 + 2 + 1 * 3;}} if(1>2){if(3<=1){return 2 - 1;}} else if (4>=2) {return 2; } else{ return 3;} while (1 == 1){while (1 != 1){return false;}} Console.Read(); Console.Write("this string"); Console.Write('this string');  Console.Write(a);}

//test 6 A small program with a variable definition on the wrong place and in the wrong order.
static void Main { while i int = 1; i = 2;}
static void Main { i int = 1; i = 2;}

//test 7 A small program using a string, variable and constant on a place that is not allowed.
static void Main { int i = 'hello';}
static void Main { int i const = 'hello';}

//test 8 A small program with a loop defined using a wrong grammar.
static void Main { const while (1 == 1){return 1;}}

//test 9 Assigning a value to a variable that does not match with its type.
static void Main { int a; a = 'hello';}

//test 10 doesnt apply since is not OOP
//test 11 variable outside scope
static void Main { if( a == b){int result = 0;} Console.Write(result);}

/* this
is
a
multiline
commment */
