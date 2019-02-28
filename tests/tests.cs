// test 1
//a

// test 2
/* this
is
a
multiline
commment */

// test 3
int num1;

// test 4
 public const double Pi = 3.14159;

// test 5
a a a a

// test 6
    int = 1;
    float = 1.0;
    bool = true;
    string = 'a';

// test 7
bool a;
if (i % 2 == 0) {
    if(i%3){
        a=true;
    } else {
        a=false;
    }

} else {
    a=true;
}



// test 8
Console.Read();
Console.Write("this string");


// test 9
// all the instructions you have defined.

string fileName;
if (length > 0 && length < 200)||(length >= 200 && length <= 400)
{
    fileName = arg[0];
}
else
{
    fileName = "phoneBook.txt";
}
StreamReader r = File.OpenText(fileName);
string line = r.ReadLine();
while (line != null)
{
    int pos = line.IndexOf('=');
    string name = line.Substring(0, pos).Trim();
    long phone = Convert.ToInt64(line.Substring(pos + 1));
    tab[name] = phone;
    line = r.ReadLine();
}
r.Close();
while (line != null)
{
    Console.Write("Name : ");
    string name = Console.ReadLine();
    if (name == "")
        break;
    object phone = tab[name];
    if (phone == null)
        Console.WriteLine("-- Not Found in Phone Book");
    else
        Console.WriteLine(phone);
}


@
// test 10
// variable definition on the wrong place and in the wrong order.

float a = 'a';
a = float 1.0;

// test 11
// string, variable and constant on a place that is not allowed.
string int const = 2;
int = 1 string, const;

while (1==1){
    const a = 2;
}

// test 12
// loop defined using a wrong grammar
while while (1 == 1){
    const while (1 == 1){
        return false;
    }
}
