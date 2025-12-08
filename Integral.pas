Program integral;
uses crt;

function f(x:real):real;
begin
  f := power(x,3) + x + 11;
end;

procedure uslovie;
begin
  clrscr;
  writeln('Дана формула кривой: x^3 + x + 11');
  writeln('Решить используя метод правых прямоугольников.');
  readkey;
end;

procedure predel(var a,b:real; var n:integer; var ok:boolean);
begin
  clrscr;
  write('Введите a: '); readln(a);
  write('Введите b: '); readln(b);

  if a>=b then begin
    writeln('Ошибка: a должно быть меньше b');
    ok := false;
    readkey;
    exit;
  end;

  write('Введите количество отрезков n: ');
  readln(n);
  
  if n <= 0 then begin
    writeln('Ошибка: n не может быть отрицательным или нулевым');
    ok := false;
    readkey;
    exit;
  end;
  writeln('Пределы успешно заданы!');
  ok := true;
  readkey;
end;

procedure otvet(a,b:real; n:integer; var y:real);
var dx,x:real; i:integer;
begin
  dx := (b-a)/n;
  y := 0;
  for i := 1 to n do
  begin
    x := a + i*dx;
    y := y + f(x);
  end;
  y := y * dx;
  
  
end;

var
  num,n: integer;
  a,b,y1,y2,y3,eps: real;
  limit: boolean;
begin
  limit := false;

  repeat
    clrscr;
    gotoXY(9,1);
    writeln('Меню');
    gotoXY(1,3);
    writeln('1. Условия');
    gotoXY(1,6);
    writeln('2. Ввод ограничений');
    gotoXY(1,9);
    writeln('3. Расчёт интеграла');
    gotoXY(1,12);
    writeln('4. Выход');
    gotoXY(1,15);
    write('Введите пункт: ');
    readln(num);
    

    case num of
      1: uslovie;

      2: predel(a,b,n,limit);

      3: if not limit then begin
           writeln('Сначала задайте пределы!');
           readkey;
         end else begin
           otvet(a,b,n,y1);
           clrscr;
           writeln('Интеграл = ', y1:4:4);
           otvet(a,b,2*n,y2);
           writeln('Интеграл с 2n = ', y2:4:4);
           y3 := 2 * y2 - y1;
           writeln('Улучшенный интеграл = ', y3:4:4);
           eps := abs(y2 - y1);
           writeln('Погрешность = ', eps:4:4);
           readkey;
         end;

    end;

  until num=4;

end.
