# While

بالإضافة إلى حلقة `for` ، لدينا نوع ثانٍ من الحلقات ، وهو حلقة `while`.
على عكس `for` ، حيث *نعرف عدد التكرارات* مسبقًا ، يتم استخدام `while` عندما يعتمد ذلك على بعض الشروط. يتم تكرار جسم (ما بداخل) الحلقة حتى يتم استيفاء الشرط.

```python
response = input('Say aaa!')
while response != 'aaa':
	print('Incorrect, try again')
	response = input('Say aaa!')
```

ولكن انتبه! من السهل جدًا كتابة حلقة بشرط صحيح دائمًا.
سيؤدي هذا النوع من الحلقات إلى التكرار إلى الأبد.

```python
from random import randrange

while True:
    print('The number is', randrange(10000))
    print('(Wait for the computer to get tired…)')
```

ولكن انتبه! من السهل جدًا كتابة حلقة بشرط صحيح دائمًا.
سيؤدي هذا النوع من الحلقات إلى التكرار إلى الأبد.**يمكن مقاطعة البرنامج باستخدام**
<kbd>Ctrl</kbd>+<kbd>C</kbd>.

> [note]
> سيؤدي هذا الاختصار إلى إثارة خطأ
> وسينتهي البرنامج - مثل بعد كل خطأ.

أخيرًا ، لدينا الأمر `break` ، والذي سيُرسل إشارة إلى العملية "للخروج" من الحلقة ،
وسيتم تنفيذ الأوامر بعد الحلقة على الفور.


```python

while True:
    response = input('Say aaa!')
    if response == 'aaa':
        print('Good')
        break
    print('Incorrect, try again')

print('Yay and it did not even hurt')
```

الأمر `break` يمكن استخدامه فقط داخل حلقة (`while` أو `for`) ،
وإذا كان لدينا حلقات متداخلة ، فسوف يخرج فقط من الحلقة التي تم استخدامها فيها.

```python
for i in range(10):  # Outer loop
    for j in range(10):  # Inner loop
        print(j * i, end=' ')
        if i <= j:
            break
    print()
```
`سيؤدي الأمر `break` إلى الخروج من الحلقة الداخلية والعودة إلى الحلقة الخارجية عندما يكون <var>i</var> أصغر من أو يساوي <var>j</var>.

لنعد للحديث عن `while` مجددا!

هل يمكنك كتابة البرنامج التالي؟

## 21

* تبدأ برصيد 0 نقطة
* في كل جولة ، يعرض الكمبيوتر عدد النقاط التي لديك ، ويسأل عما إذا كنت تريد المتابعة
* إذا أجبت "لا" ، تنتهي اللعبة.
* إذا أجبت "نعم" ، فإن الكمبيوتر "يقلب بطاقة" (يختار رقمًا عشوائيًا من 2 إلى 10) ويضيف قيمته إلى النقاط الحالية.
* إذا تجاوزت 21 ، تخسر
* الهدف من اللعبة هو الحصول على أكبر عدد ممكن من النقاط ، لكنك تفوز فقط إذا حصلت على 21.

{% filter solution %}
```python
from  random  import  randrange

sum = 0
while sum < 21:
    print('You have', sum, 'points.')
    answer = input('Turn card? ')
    if answer == 'yes':
        card = randrange(2,11)
        print("You've got number", card)
        sum = sum + card
    elif answer == 'no':
        break
    else:
        print('I do not understand! Answer "yes" or "no"' )

if sum == 21:
    print('Congratulations! You won!')
elif sum > 21:
    print('Bad luck!', sum, 'points is too much!')
else:
    print('So close! You missed', 21 - sum, 'points!')
```
{% endfilter %}
