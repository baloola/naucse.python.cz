
# *Or* & *and*

بالإضافة إلى المشغلين (operators) الذين رأيناهم في درس المقارنة ، سنضيف الآن 3 مشغلات منطقية (بوليانية) (boolean) أخرى إلى الجدول:

<table class="table">
    <tr>
        <th>الرمز</th>
        <th>مثال</th>
        <th>وصف</th>
    </tr>
    <tr>
        <td><code>and</code></td>
        <td><code>x and y</code></td>
        <td>صحيح إذا كان كلا العاملين صحيحًا</td>
    </tr>
    <tr>
        <td><code>or</code></td>
        <td><code>x or y</code></td>
        <td>صحيح إذا كان أحد العاملين صحيحًا</td>
    </tr>
    <tr>
        <td><code>not</code></td>
        <td><code>not x</code></td>
        <td>صحيح إذا كان العاملان خاطئًا<br>
        (إنه ينفي العامل)</td>
    </tr>
</table>


```python
# This program gives naive life advice.

print('Answer "yes" or "no".')
happy_status = input('Are you happy?')
if happy_status == 'yes':
    happy = True
elif happy_status == 'no':
    happy = False
else:
    print('I do not understand!')

rich_status = input('Are you rich?')
if rich_status == 'yes':
    rich = True
elif rich_status == 'no':
    rich = False
else:
    print('I do not understand!')

if rich and happy:
    # rich and at the same time.
    print('Congratulations!')
elif rich:
    # rich but not "rich and happy",
    #so must be only rich.
    print('Try to smile more.')
elif happy:
    # must be only happy.
    print('Try to spend less.')
else:
    # neither happy nor rich.
    print("I'm sorry for you.")

```

> [note]
> ماذا يحدث إذا أجبت بشيء آخر غير "نعم" أو "لا"؟
>
> لن يتم تعيين المتغيرين `happy` و `rich` ، وفي وقت لاحق عندما تكون هناك حاجة إليهما ، سينتهي البرنامج بـ خطأ.
>
> سنتعلم كيفية التعامل مع الأخطاء [في المرة القادمة]({{ lesson_url('beginners-en/exceptions') }}).