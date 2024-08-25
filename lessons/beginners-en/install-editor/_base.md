# Installation التثبيت {% block name_gen %} editor {{ var('editor_name') }} {% endblock %}


{% block install %}

قم بتنزيل {{ editor_name }}
من [webpage]({{ editor_url }})
وقم بتثبيته.

{% endblock %}

## Settings الخطوات

{% block setup %}


{% endblock %}


## تمرين **المسافة (indentation)**

من المهم في بايثون مقدار المسافات التي يتم فيها استطالة سطر ما.
لذلك علينا أن نتعلم  سريعا كيفية التحكم بالمسافات لقطعة من النص.

أولاً، انسخ النص التالي في **المحرر (editor)** الخاص بك.


```
OPHELIA:
Good my lord,
How does your honour for this many a day?
HAMLET:
I humbly thank you; well, well, well.
OPHELIA:
My lord, I have remembrances of yours,
That I have longed long to re-deliver;
I pray you, now receive them.
HAMLET:
No, not I;
I never gave you aught.
OPHELIA:
My honour'd lord, you know right well you did;
And, with them, words of so sweet breath composed
As made the things more rich: their perfume lost,
Take these again; for to the noble mind
Rich gifts wax poor when givers prove unkind.
There, my lord.
```

<small>Hamlet, W. Shakespeare</small>


هذا النص غير مرتب جيدًا، لذلك سنقوم ب ضبط فراغاته على النحو التالي:

```
OPHELIA:
    Good my lord,
    How does your honour for this many a day?
HAMLET:
    I humbly thank you; well, well, well.
OPHELIA:
    My lord, I have remembrances of yours,
    That I have longed long to re-deliver;
    I pray you, now receive them.
HAMLET:
    No, not I;
    I never gave you aught.
OPHELIA:
    My honour'd lord, you know right well you did;
    And, with them, words of so sweet breath composed
    As made the things more rich: their perfume lost,
    Take these again; for to the noble mind
    Rich gifts wax poor when givers prove unkind.
    There, my lord.
```

لتنظيم مسافات سطر واحد، ضع المؤشر في بداية السطر واضغط على <kbd>Tab</kbd>. مع كل ضغطة، ستزيد المسافات بمقدار أربعة فراغات.

إذا قمت بزيادة المسافات أكثر من اللازم، اضغط على <kbd>Shift</kbd>+<kbd>Tab</kbd>.

إذا كنت تريد تنظيم مسافات عدة أسطر، فما عليك سوى تحديدها واضغط على <kbd>Tab</kbd>.

 لإلغاء التغيير، اضغط على <kbd>Shift</kbd>+<kbd>Tab</kbd>.
