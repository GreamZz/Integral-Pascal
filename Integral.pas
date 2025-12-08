Program integral;
uses crt;
label menu,formula,predel,ends,raschet,otvet;

function f(x:real):real;

begin

f := (1 * power(x,3) + 0 * power(x,2) + 1 * x + 11)

end;

var num,n,predels: integer;
a,b,dx,x,y:real;
begin
predels := 0;
menu:
clrscr;
gotoXY(14,1);
writeln('Меню');
gotoXY(2,4);
writeln('1. Посмотреть условия');
gotoXY(2,7);
writeln('2.Ввести пределы интегрирования');
gotoXY(2,10);
writeln('3.Рассчитать интеграл');
gotoXY(1,13);
write('Выберите пункт для продолжения: ');
readln(num);
if num = 1 then goto formula
else if num = 2 then goto predel
else if num = 3 then goto raschet
else begin
  clrscr;
  writeln('Ошибка ввода. Нажмите любую клавишу для возвращения в меню.');
  readkey;
  goto menu;
end;

formula:
clrscr;
writeln('Дана формула кривой: x³ + 0 * x² + 1 * x + 11');
writeln('Необходимо численно вычислить определенный интеграл с использованием метода правых прямоугольников.');
gotoXY(1,4);
writeln('Нажмите любую клавишу для возвращения в меню.');
readkey;
goto menu;
predel:
clrscr;
write('Введите a: ');
readln(a);
write('Введите b: ');
readln(b);

if a > b then begin
gotoXY(1,4);
writeln('Ошибка: a не может быть больше чем b.');
gotoXY(1,7);
writeln('Нажмите любую клавишу чтобы ввести пределы заново.');
readkey;
goto predel;
end;

if a = b then begin
gotoXY(1,4);
writeln('Ошибка: пределы не могут быть равны');
gotoXY(1,7);
writeln('Нажмите любую клавишу чтобы ввести пределы заново.');
readkey;
goto predel;
end;

write('Введите количество отрезков n: ');
readln(n);
gotoXY(1,6);
writeln('Пределы успешно заданы!');
predels := 1;
gotoXY(1,9);
writeln('Нажмите любую клавишу для возвращения в меню.');
readkey;
goto menu;

raschet:
clrscr;
if predels = 0 then begin
writeln('Вы не задали пределы интегрирования. Это можно сделать в меню в пункте 2.');
gotoXY(1,4);
writeln('Нажмите любую клавишу для возвращения в меню.');
readkey;
goto menu;
end;

dx := (b-a)/n;
y := 0;
x:= a + dx;
while x <= b do begin

  y := y + f(x);
  x := x + dx;

end;

y := y * dx;
otvet:
clrscr;
writeln('Интеграл равен: ',y:3);
gotoXY(1,4);
writeln('1. Вернуться в меню');
gotoXY(1,7);
writeln('2. Оценка погрешности');
gotoXY(1,10);
writeln('3. Закрыть программу');
gotoXY(1,13);
write('Выберите пункт для продолжения: ');
readln(num);

if num = 1 then goto menu
else if num = 2 then writeln('В разработке...')
else if num = 3 then goto ends
else begin
  clrscr;
  writeln('Ошибка ввода. Нажмите любую клавишу для повторного выбора.');
  readkey;
  goto otvet;
  end;

ends:
end.
